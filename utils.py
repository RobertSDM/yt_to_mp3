import asyncio


async def download_audio(url: str, out: str):
    args = f"yt-dlp -t mp3 --no-playlist --no-warnings -o %(title)s.mp3 -P {out} {url}".split(
        " "
    )

    proc = await asyncio.create_subprocess_exec(*args)

    await proc.wait()


def clean_url(url: str) -> str:
    return url.split("&")[0].strip()


def is_url_valid(url: str) -> bool:
    if url.startswith("https://youtube.com/watch") or url.startswith(
        "https://www.youtube.com/watch"
    ):
        return True

    return False
