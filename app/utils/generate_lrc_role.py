from pyannote.audio import Pipeline
import torch
from faster_whisper import WhisperModel
import re
from generate_lrc import write_lrc
# 后边再完善
def _generate_lrc_role(read_file_path, write_file_path):
    # 1. 使用 faster-whisper 生成文字
    model = WhisperModel(
        "small", device="cuda" if torch.cuda.is_available() else "cpu"
    )  # 或 tiny
    segments, info = model.transcribe(
        read_file_path,
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=1000),
    )
    whisper_results = []
    for seg in segments:
        whisper_results.append(
            {"start": seg.start, "end": seg.end, "text": seg.text.strip()}
        )
    # 2. 使用 pyannote 生成说话人
    HF_TOKEN = ""
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization@2.1", use_auth_token=HF_TOKEN
    )
    print("pipeline", pipeline)
    diarization = pipeline(read_file_path)
    print("diarization", diarization)
    speaker_segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print("turn", turn)
        print("speaker", speaker)
        speaker_segments.append(
            {"start": turn.start, "end": turn.end, "speaker": speaker}
        )

    # 3. 对齐 (把文字分配给说话人)
    results = []
    for wseg in whisper_results:
        # 找到时间重叠的 speaker 段
        speaker = None
        for sseg in speaker_segments:
            if sseg["start"] <= wseg["start"] < sseg["end"]:
                speaker = sseg["speaker"]
                break
        results.append(
            {
                "speaker": speaker or "Unknown",
                "start": wseg["start"],
                "end": wseg["end"],
                "text": wseg["text"],
            }
        )
    # 4. 合并相同说话人的段落
    merged_results = []
    for r in results:
        if merged_results and merged_results[-1]["speaker"] == r["speaker"]:
            # 合并到上一条
            merged_results[-1]["end"] = r["end"]
            merged_results[-1]["text"] += " " + r["text"]
        else:
            merged_results.append(r)
    write_lrc(merged_results, write_file_path)
