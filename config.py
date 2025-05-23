# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26729193"))
API_HASH = getenv("API_HASH", "a94598ef642481e35466292df95f251e")
BOT_TOKEN = getenv("BOT_TOKEN", "7609700133:AAG6TqHDZt3Mdi3Za5XKaP-xfcu0HFjwxTA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1012164907").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Uploaderbot:Uploaderbot@cluster0.mkxbrre.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002607015025")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002607015025"))
