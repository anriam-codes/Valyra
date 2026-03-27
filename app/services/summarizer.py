# Core pipeline: URL → transcript → chunk → summarize → combine

from app.utils.youtube import extract_video_id
from app.utils.chunking import chunk_text

# TEMP: fake transcript (replace later with real YouTube transcript)
def get_transcript(video_id: str) -> str:
    return "This is a sample transcript of a video. " * 200


# TEMP: fake summarization (replace with OpenAI later)
def summarize_chunk(chunk: str) -> str:
    return f"Summary of chunk: {chunk[:50]}..."


def summarize_video_pipeline(url: str):
    # Step 1: Extract video ID
    video_id = extract_video_id(url)

    # Step 2: Get transcript
    transcript = get_transcript(video_id)

    # Step 3: Chunk transcript
    chunks = chunk_text(transcript)

    # Step 4: Summarize each chunk
    summaries = []
    for chunk in chunks:
        summaries.append(summarize_chunk(chunk))

    # Step 5: Combine summaries
    final_summary = " ".join(summaries)

    return {
        "video_id": video_id,
        "summary": final_summary
    }