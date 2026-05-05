from backend.services.youtube_service import get_latest_videos
from backend.services.transcript_service import get_transcript
from backend.services.ai_analysis_service import analyze_video
from backend.services.trend_service import compute_trends
from backend.services.youtube_service import get_video_stats

CHANNELS = [
    {"name": "Fireship", "id": "UCsBjURrPoezykLs9EqgamOA"},
    {"name": "Two Minute Papers", "id": "UCbfYPyITQ-7l4upoX8nvctg"}
]


def run_pipeline():

    all_videos = []

    print("\nFetching videos...\n")

    for channel in CHANNELS:

        videos = get_latest_videos(channel["id"])

        for item in videos.get("items", []):

            video_id = item["id"].get("videoId")

            if not video_id:
                continue

            title = item["snippet"]["title"]

            print(f"Processing: {title}")

            transcript = get_transcript(video_id)

            if not transcript:
                print("No transcript, skipping\n")
                continue

            analysis = analyze_video(transcript)

            video_data = {
                "video_id": video_id,
                "channel_id": channel["name"],
                "title": title,
                "views": get_video_stats(video_id),
                "topic": analysis["topic"]
            }

            all_videos.append(video_data)

    print("\nComputing trends...\n")

    trends = compute_trends(all_videos)

    return trends


if __name__ == "__main__":

    trends = run_pipeline()

    print("\n🔥 TRENDING TOPICS:\n")

    for t in trends:
        print(f"{t['topic']} → Score: {t['trend_score']}")