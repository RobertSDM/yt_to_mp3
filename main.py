import asyncio
import os
import sys

from utils import clean_url, download_audio, is_url_valid


async def download(sem: asyncio.Semaphore, url: str, outpath: str):
    async with sem:
        try:
            await download_audio(url, outpath)
            print("Audio downloaded successfully")
        except Exception:
            print("Url: ", url, " [FAILED]")


async def main():
    argv = sys.argv[1:]

    if len(argv) < 2 or len(argv) > 2:
        print("Usage: <outpath> <url>")
        return

    sem = asyncio.Semaphore(4)

    outpath, url = argv
    urls = []

    if len(m := url.split(",")) > 1:
        urls = m
    else:
        urls.append(url)

    if not os.path.exists(outpath):
        os.mkdir(outpath)

    async with asyncio.TaskGroup() as tg:
        for u in urls:
            if u == "":
                continue
            if not is_url_valid(u):
                print("Url: ", u, " [NOT SUPPORTED]")
                continue

            fmt_u = clean_url(u)
            tg.create_task(download(sem, fmt_u, outpath))


if __name__ == "__main__":
    asyncio.run(main())
