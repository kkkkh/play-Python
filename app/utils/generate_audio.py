from gtts import gTTS


def generate_audio(text, file_path):
    tts = gTTS(text=text, lang="zh")
    tts.save(file_path)
    print("音频已生成：chahua_nv.mp3")
