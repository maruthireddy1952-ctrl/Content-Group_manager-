from backend.database.models import Analysis, Video
from backend.database.db import SessionLocal


def save_video(video_data):

    db = SessionLocal()

    existing = db.query(Video).filter(
        Video.video_id == video_data["video_id"]
    ).first()

    if existing:
        db.close()
        return

    video = Video(**video_data)

    db.add(video)

    db.commit()

    db.close()

def get_unprocessed_videos():

    db = SessionLocal()

    videos = db.query(Video).filter(
        Video.processed == False
    ).all()

    db.close()

    return videos
def mark_video_processed(video_id):

    db = SessionLocal()

    video = db.query(Video).filter(
        Video.video_id == video_id
    ).first()

    if video:

        video.processed = True

        db.commit()

    db.close()
    
def save_analysis(data):

    db = SessionLocal()

    existing = db.query(Analysis).filter(
        Analysis.video_id == data["video_id"]
    ).first()

    if existing:
        db.close()
        return

    analysis = Analysis(**data)

    db.add(analysis)

    db.commit()

    db.close()