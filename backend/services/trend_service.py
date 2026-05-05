from collections import defaultdict


def compute_trends(video_analyses):

    topic_data = defaultdict(list)

    for video in video_analyses:

        topic = video["topic"]

        topic_data[topic].append(video)

    trends = []

    for topic, videos in topic_data.items():

        frequency = len(videos)

        avg_views = sum(v["views"] for v in videos) / frequency

        channels = len(set(v["channel_id"] for v in videos))

        trend_score = (
            0.5 * frequency +
            0.3 * (avg_views / 100000) +
            0.2 * channels
        )

        trends.append({
            "topic": topic,
            "frequency": frequency,
            "avg_views": avg_views,
            "channels": channels,
            "trend_score": round(trend_score, 2)
        })

    trends.sort(key=lambda x: x["trend_score"], reverse=True)

    return trends