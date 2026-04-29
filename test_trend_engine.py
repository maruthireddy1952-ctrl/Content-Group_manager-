from backend.services.trend_service import compute_trends


videos = [

{"topic": "AI Agents", "views": 120000, "channel_id": "fireship"},
{"topic": "AI Agents", "views": 90000, "channel_id": "twp"},
{"topic": "Vision AI", "views": 60000, "channel_id": "veritasium"}

]

trends = compute_trends(videos)

print(trends)