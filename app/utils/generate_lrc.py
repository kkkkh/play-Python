# faster_whisper 在 Windows 上更快或避免依赖问题
from faster_whisper import WhisperModel
import re
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import os


def write_lrc(segments, write_file_path):
    with open(write_file_path, "w", encoding="utf-8") as f:
        for seg in segments:
            # 如果 seg.start = 73.45 秒：
            # 分钟 m = 1
            # 秒数 s = 13
            # 百分之一秒 cs = 45
            start = seg["start"] # seg.start：该片段的起始时间（单位：秒，浮点数）。
            m = int(start // 60)  # m：分钟数。
            s = int(start % 60) # s：秒数（整数）。
            cs = int((start - int(start)) * 100)  # cs：小数部分，取到 2 位（百分之一秒）。
            f.write(f"[{m:02d}:{s:02d}.{cs:02d}] {seg['text'].strip()}\n")
            # print(f"[{s['start']:.2f} - {s['end']:.2f}] {s['text']}")

def slice_segments(segments):
    new_segments = []
    for seg in segments:
        # seg.words 是逐词结果，包含 start, end, word
        buffer = []
        start_time = None

        for w in seg.words:
            if start_time is None:
                start_time = w.start

            buffer.append(w.word)

            # 如果遇到标点，就切分
            if re.search(r"[.!?。！？]", w.word):
            # if re.search(r"[,.!?，。！？]", w.word):
                text = "".join(buffer).strip()
                if text:
                    new_segments.append(
                        {"start": start_time, "end": w.end, "text": text}
                    )
                buffer = []
                start_time = None

        # 如果结尾还有残余
        if buffer:
            text = "".join(buffer).strip()
            if text:
                new_segments.append({"start": start_time, "end": seg.end, "text": text})
    return new_segments

def generate_lrc(read_file_path, write_file_path):
    model = WhisperModel("small", device="cpu")
    segments, info = model.transcribe(
        read_file_path,
        beam_size=5,  # beam_size=5 表示使用 Beam Search 搜索时考虑 5 个候选结果，通常能提高准确率（代价是速度变慢）。
        vad_filter=True,  # 开启语音活动检测（Voice Activity Detection），会自动在停顿处切分片段
        vad_parameters=dict(min_silence_duration_ms=300),  # 停顿超过 300ms 就切分
        word_timestamps=True,  # 获取逐词时间戳
        # max_segment_length=3,  # 控制单个 segment 的最长秒数，例如 10 秒。
    )
    new_segments = slice_segments(segments)
    write_lrc(new_segments, write_file_path)

def join_path(save_dir,group_id,id,ext):
    file_name = f'{group_id}_{id}.{ext}'
    return os.path.join(save_dir, file_name)

def join_audio_path(num):
    return f'./app/resource/englishpod_0{str(num).zfill(3)}pb.mp3'
def join_lrc_path(num):
    return f'./app/resource/englishpod_0{str(num).zfill(3)}pb.lrc'


def batch_generate_lrc(*params,save_dir = "./app/resource",group_id=1 ):
    # audio_list = list(map(lambda num: join_audio_path(num), range(*params)))
    # lrc_list = list(map(lambda num: join_lrc_path(num), range(*params)))
    audio_list = []
    lrc_list = []
    (start,end) = params
    for id in range(start, end + 1):
        audio_list.append(join_path(save_dir, group_id, id, 'mp3'))
        lrc_list.append(join_path(save_dir, group_id, id, 'lrc'))
    # print(audio_list)
    # print(lrc_list)
    desc = f"生成序号：{start}-{end}"
    with ProcessPoolExecutor(max_workers=2) as executor:
        for result in tqdm(executor.map(generate_lrc, audio_list, lrc_list), total=len(audio_list),desc=desc):
            print(result)



