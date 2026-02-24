import subprocess

def get_web_stream(url: str):
    cmd = [
        "yt-dlp",
        "--cookies", "cookies.txt",
        "--js-runtimes", "node",
        "--remote-components", "ejs:github",
        "-f", "(bestaudio)[protocol^=http]/best",
        "--no-playlist",
        "-g",
        url
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("ERROR:", result.stderr)
        return None

    return result.stdout.strip().split("\n")[0]


async def ytdl_audio(url: str):
    stream_url = get_web_stream(url)

    if not stream_url:
        return False, "Failed to get audio stream URL"

    return True, stream_url
