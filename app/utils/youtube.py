# Extract video ID from YouTube URL
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)

    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [""])[0]

    if "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")

    return ""