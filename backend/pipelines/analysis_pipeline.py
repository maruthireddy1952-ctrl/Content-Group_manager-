from backend.database.crud import (

    get_unprocessed_videos,

    mark_video_processed,

    save_analysis
)
from backend.services.clustering_service import (
    normalize_topic
)
from backend.services.ai_analysis_service import (
    analyze_video
)


def run_analysis():

    videos = get_unprocessed_videos()
    
    print(f"\nFound {len(videos)} unprocessed videos\n")

    for video in videos:

        print(f"Analyzing: {video.title}")

        result = analyze_video(video.transcript)
        normalized = normalize_topic(result["topic"])
        
        analysis_data = {

            "video_id": video.video_id,

            "topic": result["topic"],

            "normalized_topic": normalized,

            "keywords": ",".join(
                result["keywords"]
            ),

            "category": result["category"],

            "trend_score": result["trend_score"]
        }

        save_analysis(analysis_data)

        mark_video_processed(video.video_id)

        print("Saved analysis.\n")

    print("Analysis pipeline completed.")