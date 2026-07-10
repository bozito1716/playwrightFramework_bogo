from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    BASE_URL = os.getenv("BASE_URL")

    EMAIL = os.getenv("EMAIL")

    PASSWORD = os.getenv("PASSWORD")