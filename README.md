# 📺 Subtitle TV App

A simple Python application that generates subtitles from audio and displays them like a TV app.

---

## Features
- 🎤 Convert speech from `.wav` audio files to subtitles using OpenAI Whisper
- ⏱️ Auto-sync subtitles with audio timing (like TV or karaoke)
- 🖥️ Simple, clean TV-style GUI using Tkinter
- 📝 Outputs standard `.srt` subtitle files

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/tranhao-wq/Subtitle-App-Python.git
   cd Subtitle-App-Python
   ```
2. **Install Python dependencies**
   ```bash
   pip install openai-whisper tkinter ffmpeg-python
   ```
   - You may also need to [install ffmpeg](https://ffmpeg.org/download.html) for audio processing.

---

## Usage

1. **Place your audio file** (e.g. `YourAudio.wav`) in the project folder.
2. **Generate subtitles:**
   ```bash
   python generate_subtitles.py
   ```
   - This will create `subtitles.srt` from your audio file.
3. **Display subtitles like a TV app:**
   ```bash
   python tv_app.py
   ```
   - A window will open and show the subtitles in sync with the audio timing.

---

## Demo

![TV Subtitle Demo](https://em-content.zobj.net/source/microsoft-teams/363/television_1f4fa.png)

---

## Credits
- Inspired by [OpenAI Whisper](https://github.com/openai/whisper)
- Project template: [Subtitle-App-Python](https://github.com/tranhao-wq/Subtitle-App-Python)

---

## License
MIT 