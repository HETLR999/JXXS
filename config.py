import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "7330436352:AAHUJUNGytd9bTY1otHe7EVwJlN4km0usXw") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 20077058)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "349639880eb5b1cb0ff6c2b8a6f16717") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 6169288210) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://avdhez:2004@leech.pg1bvd7.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
