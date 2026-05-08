from sqlalchemy import Column, Integer, String, Text, Float,Boolean
from .db import Base
from sqlalchemy import DateTime
from datetime import datetime

class Channel(Base):

    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    channel_id = Column(String)


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    video_id = Column(String, unique=True, index=True)

    channel_name = Column(String)

    title = Column(String)

    description = Column(Text)

    transcript = Column(Text)

    views = Column(Integer)

    processed = Column(Boolean, default=False)
    published_at = Column(DateTime)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Analysis(Base):

    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True)

    video_id = Column(String, unique=True)

    topic = Column(String)

    normalized_topic = Column(String)

    keywords = Column(Text)

    category = Column(String)

    trend_score = Column(Float)

    created_at = Column(
                DateTime,
                default=datetime.utcnow
                )

class TopicCluster(Base):

    __tablename__ = "topic_clusters"

    id = Column(Integer, primary_key=True)

    topic_name = Column(String, unique=True)

    embedding = Column(Text)