
from backend.database.db import engine
from backend.database.models import Base
from sqlalchemy import inspect


def init_db():

    Base.metadata.create_all(bind=engine)

    print("Database tables created")


if __name__ == "__main__":

    init_db()