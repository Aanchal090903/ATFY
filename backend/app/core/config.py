import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "AI Tools Platform"
    ENV = os.getenv("ENV", "dev")
    ADMIN_SECRET = os.getenv("ADMIN_SECRET", "dev-secret")

settings = Settings()
