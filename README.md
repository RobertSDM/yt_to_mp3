# Youtube video to MP3

Simple python binding to use `yt-dlp` and `asyncio` to download and convert youtube videos into high-quality MP3 files concurrently.

## Features

- **High Performance:** powered by Python's built-in `asyncio` package, allows up to **3** concurrent downloads, using the `asyncio.Semaphore`.

## Prerequisites

Before everything, you'll need to have `yt-dlp` and `ffmpeg` installed and added to the system's **PATH**

```bash
# Windows
choco install yt-dlp ffmpeg -y

# Linux/Mac
sudo apt install ffmpeg
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

## How to use

Clone the repo:

```bash
cd /path/to/download
git clone https://github.com/RobertSDM/yt_to_mp3
cd ./video_to_mp3
```

Create a virtual environment and run the script:

```bash
# Create a virtual environment
python -m venv venv

# Running
## Windows
.\venv\Scripts\python main.py <output_path> <urls>

## Linux/Mac
./venv/bin/python main.py <output_path> <urls>
```

## Examples

Download multiple links at once:

```bash
./venv/bin/python main.py ~/output/path "https://www.youtube.com/watch?v=abc123,https://www.youtube.com/watch?v=xyz789"
```
