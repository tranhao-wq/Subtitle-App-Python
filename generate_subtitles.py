import whisper
import os

def transcribe_to_srt(audio_path, srt_path):
    model = whisper.load_model('base')
    result = model.transcribe(audio_path, word_timestamps=False)
    segments = result['segments']
    
    def format_timestamp(seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds - int(seconds)) * 1000)
        return f"{h:02}:{m:02}:{s:02},{ms:03}"

    with open(srt_path, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(segments, 1):
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])
            text = seg['text'].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

if __name__ == "__main__":
    audio_file = "Bí Quyết Học Đâu Nhớ Đó.wav"
    srt_file = "subtitles.srt"
    transcribe_to_srt(audio_file, srt_file)
    print(f"Đã tạo file subtitle: {srt_file}") 