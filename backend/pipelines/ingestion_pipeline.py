from backend.services.youtube_service import (
    get_latest_videos,
    get_video_stats
)

from backend.services.transcript_service import (
    get_transcript
)

from backend.database.crud import save_video
from backend.api.channels import CHANNELS

from datetime import datetime


def run_ingestion():

    print("\nStarting ingestion pipeline...\n")

    total_saved = 0

    for channel in CHANNELS:

        print(f"Fetching channel: {channel['name']}")

        videos = get_latest_videos(channel["id"])

        for item in videos.get("items", []):

            video_id = item["id"].get("videoId")

            if not video_id:
                continue

            snippet = item["snippet"]

            title = snippet["title"]

            description = snippet["description"]

            published_at = snippet["publishedAt"]

            # Convert YouTube datetime format
            published_at = datetime.fromisoformat(
                published_at.replace("Z", "+00:00")
            )

            print(f"\n▶ Processing: {title}")

            # Fetch transcript
            transcript = get_transcript(video_id)

            if not transcript:

                print("⚠ No transcript found. Skipping.")

                continue

            # Fetch real views
            views = get_video_stats(video_id)

            video_data = {

                "video_id": video_id,

                "channel_name": channel["name"],

                "title": title,

                "description": description,

                "transcript": transcript,

                "views": views,

                "published_at": published_at
            }

            # Save to DB
            save_video(video_data)

            total_saved += 1

            print("Saved successfully.")

    print(f"\nIngestion completed. Total saved: {total_saved}")