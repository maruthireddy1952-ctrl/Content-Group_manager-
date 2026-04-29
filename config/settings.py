from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

OLLAMA_MODEL = "deepseek-r1:8b"
EMBEDDING_MODEL = "nomic-embed-text"