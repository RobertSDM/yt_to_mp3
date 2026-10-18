import asyncio
import shutil


def check_for_dependencies():
    path = shutil.which("yt-dlp")
    if path is None:
        raise RuntimeError("yt-dlp is not installed or not in PATH")

    path = shutil.which("ffmpeg")
    if path is None:
        raise RuntimeError("ffmpeg is not installed or not in PATH")


async def download_audio(url: str, out: str):
    args = f"yt-dlp -t mp3 --no-playlist --no-warnings -o %(title)s.mp3 -P {out} {url}".split(
        " "
    )

    proc = await asyncio.create_subprocess_exec(*args)

    await proc.wait()

    if proc.returncode != 0:
        raise RuntimeError(f"yt-dlp failed with code {proc.returncode}")


def clean_url(url: str) -> str:
    return url.split("&")[0].strip()


def is_url_valid(url: str) -> bool:
    if url.startswith("https://youtube.com/watch") or url.startswith(
        "https://www.youtube.com/watch"
    ):
        return True

    return False
