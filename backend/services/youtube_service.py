import requests
from config.settings import YOUTUBE_API_KEY


def get_latest_videos(channel_id):

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "key": YOUTUBE_API_KEY,
        "channelId": channel_id,
        "part": "snippet",
        "order": "date",
        "maxResults": 5
    }

    response = requests.get(url, params=params)

    return response.json()
def get_video_stats(video_id):

    url = "https://www.googleapis.com/youtube/v3/videos"

    params = {
        "key": YOUTUBE_API_KEY,
        "id": video_id,
        "part": "statistics"
    }

    response = requests.get(url, params=params)

    data = response.json()

    try:
        return int(data["items"][0]["statistics"]["viewCount"])
    except:
        return 0