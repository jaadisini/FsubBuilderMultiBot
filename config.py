import os
import sys

import dotenv

dotenv.load_dotenv(sys.argv[1] if len(sys.argv) > 1 else ".env")


API_ID = int(os.getenv("API_ID", "28932643"))
API_HASH = os.getenv("API_HASH", "3fb38bb53a7d33fb42ea208c6f77830b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8594970718:AAFdEWYFvlE_DQH7bMp0ioC8h6_aKnmiZ6o")
OWNER_ID = int(os.getenv("OWNER_ID", "1816904396"))
DB_NAME = os.getenv("DB_NAME", "vip")
DB_KEY = os.getenv("DB_KEY", "vip")
FILE_KEY = os.getenv("FILE_KEY", "my_s3cr3t_k3y_@2024")
