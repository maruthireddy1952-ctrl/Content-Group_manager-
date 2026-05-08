from backend.database.db import SessionLocal

from backend.database.models import (
    Analysis,
    Video
)

from backend.services.trend_service import (
    compute_trends
)


def run_trends():

    db = SessionLocal()

    analyses = db.query(
        Analysis,
        Video
    ).join(
        Video,
        Analysis.video_id == Video.video_id
    ).all()

    data = []

    for analysis, video in analyses:

        data.append({

            "normalized_topic":
                analysis.normalized_topic,

            "views":
                video.views,

            "channel_id":
                video.channel_name,

            "published_at":
                video.published_at
        })

    trends = compute_trends(data)
    print(data)
    db.close()

    return trends