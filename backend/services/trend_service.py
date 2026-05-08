from collections import defaultdict
from datetime import datetime, timedelta


def compute_trends(analyses):

    grouped = defaultdict(list)

    for item in analyses:

        grouped[item["normalized_topic"]].append(item)

    trends = []

    now = datetime.utcnow()

    for topic, videos in grouped.items():

        frequency = len(videos)

        avg_views = sum(
            v["views"] for v in videos
        ) / frequency

        channels = len(set(
            v["channel_id"] for v in videos
        ))

        recent_count = 0

        for v in videos:

            age_hours = (
                now - v["published_at"]
            ).total_seconds() / 3600

            if age_hours <= 48:
                recent_count += 1

        momentum = recent_count / max(frequency, 1)

        trend_score = (

            0.35 * frequency +

            0.25 * (avg_views / 100000) +

            0.20 * channels +

            0.20 * momentum * 10
        )

        trends.append({

            "topic": topic,

            "frequency": frequency,

            "avg_views": avg_views,

            "channels": channels,

            "momentum": round(momentum, 2),

            "trend_score": round(trend_score, 2)
        })

    trends.sort(
        key=lambda x: x["trend_score"],
        reverse=True
    )

    return trends