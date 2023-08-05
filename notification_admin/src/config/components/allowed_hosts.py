import os

from dotenv import load_dotenv

load_dotenv()
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]").split(",")
