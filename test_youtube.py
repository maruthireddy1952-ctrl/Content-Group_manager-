from backend.services.youtube_service import get_latest_videos
#channel you need 
channel_id = "UCsBjURrPoezykLs9EqgamOA"

videos = get_latest_videos(channel_id)

print(videos)