import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
 
#Каналы

DESTINATION_CHANNEL = os.getenv("DESTINATION_CHANNEL")
SOURCE_CHANNELS_1 = os.getenv("SOURCE_CHANNELS_1")
SOURCE_CHANNELS_2 = os.getenv("SOURCE_CHANNELS_2")
SOURCE_CHANNELS_3 = os.getenv("SOURCE_CHANNELS_3")
SOURCE_CHANNELS_4 = os.getenv("SOURCE_CHANNELS_4")
SOURCE_CHANNELS_5 = os.getenv("SOURCE_CHANNELS_5")
STOP_WORDS = []
CHANGE_WORDS = []