from sqlalchemy import Column, Integer, String, Text, Float
from .db import Base


class Channel(Base):

    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    channel_id = Column(String)


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    video_id = Column(String)
    channel_id = Column(String)

    title = Column(String)
    description = Column(Text)

    transcript = Column(Text)

    views = Column(Integer)


class Analysis(Base):

    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True)

    video_id = Column(String)

    topic = Column(String)
    keywords = Column(Text)
    category = Column(String)

    trend_score = Column(Float)