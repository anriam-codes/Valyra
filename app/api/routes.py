from fastapi import APIRouter
from app.models.summarize import SummarizeRequest, SummarizeResponse
from app.services.summarizer import summarize_video_pipeline

router = APIRouter()

# POST endpoint using real pipeline
@router.post("/summarize", response_model=SummarizeResponse)
def summarize_video(request: SummarizeRequest):
    result = summarize_video_pipeline(request.url)
    return result