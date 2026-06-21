import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

API_PREFIX: str = "/client"
SECRET_KEY: str = os.environ["SECRET_KEY"]
