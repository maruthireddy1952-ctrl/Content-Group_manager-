from backend.services.ai_analysis_service import analyze_video
from backend.services.embedding_service import generate_embedding
from backend.services.trend_service import compute_trends


def run_analysis(videos):

    analyses = []

    for video in videos:

        result = analyze_video(video["transcript"])

        analysis = {
            "video_id": video["video_id"],
            "channel_id": video["channel_id"],
            "views": video["views"],
            "topic": result["topic"]
        }

        analyses.append(analysis)

    trends = compute_trends(analyses)

    return trends