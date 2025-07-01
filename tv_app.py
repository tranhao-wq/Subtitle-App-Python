import tkinter as tk
import time
import threading
import re

# Đọc file SRT
class Subtitle:
    def __init__(self, start, end, text):
        self.start = start
        self.end = end
        self.text = text

def parse_srt(srt_path):
    with open(srt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+\n|\Z)', re.S)
    subs = []
    for match in pattern.finditer(content):
        start = srt_time_to_seconds(match.group(2))
        end = srt_time_to_seconds(match.group(3))
        text = match.group(4).replace('\n', ' ')
        subs.append(Subtitle(start, end, text))
    return subs

def srt_time_to_seconds(s):
    h, m, rest = s.split(':')
    s, ms = rest.split(',')
    return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000

class TVApp:
    def __init__(self, root, subtitles):
        self.root = root
        self.subtitles = subtitles
        self.label = tk.Label(root, text='', font=('Arial', 32), bg='black', fg='white', wraplength=900, justify='center')
        self.label.pack(expand=True, fill='both')
        self.start_time = None
        self.running = False

    def start(self):
        self.running = True
        self.start_time = time.time()
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        idx = 0
        while self.running and idx < len(self.subtitles):
            now = time.time() - self.start_time
            sub = self.subtitles[idx]
            if now >= sub.start and now <= sub.end:
                self.label.config(text=sub.text)
            elif now > sub.end:
                idx += 1
                self.label.config(text='')
            time.sleep(0.05)
        self.label.config(text='')

    def stop(self):
        self.running = False

if __name__ == "__main__":
    srt_file = "subtitles.srt"
    subtitles = parse_srt(srt_file)
    root = tk.Tk()
    root.title("App TV Subtitle")
    root.configure(bg='black')
    root.geometry('1000x200')
    app = TVApp(root, subtitles)
    app.start()
    root.mainloop() 