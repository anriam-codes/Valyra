from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    url: str  # YouTube URL

class SummarizeResponse(BaseModel):
    video_id: str
    summary: str