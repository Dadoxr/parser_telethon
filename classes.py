from telethon.tl.types import MessageEntityTextUrl
from telethon.tl import types
from config import *
import logging
import re

logging.basicConfig(level=logging.INFO, filename='logging.log', format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')

class Post:
    def __init__(self, event, client):
        self.event = event.message
        self.client = client
        self.url = [i.url for i in event.entities if isinstance(i, MessageEntityTextUrl)] if event.entities is not None else []
        self.stopwords = STOP_WORDS
        self.change_words = CHANGE_WORDS

    async def check_lenth(self):
        try:
            event_text = self.event.text if isinstance(self.event, types.Message) else self.event
            print(len(event_text))
            return len(event_text) <= 4096
        except Exception as error:
            logging.critical(f"Не смог посчитать длину сообщения ---> {error}")
            return False
    
    def check_stopwords_and_empty_message(self):
        try:
            if self.event is not None:
                self.event_str = self.event.text if isinstance(self.event, types.Message) else self.event
                if any(stopword in self.event_str.lower() for stopword in self.stopwords):
                    for stopword in self.stopwords:
                        if stopword in self.event_str.lower():
                            print(f"Найдено стоп-слово: {stopword}")
                    self.event = None
            if self.url is not None:
                url_str = " ".join(self.url)
                if any(stopword in url_str.lower() for stopword in self.stopwords):
                    for stopword in self.stopwords:
                        if stopword in url_str.lower():
                            print(f"Найдено стоп-слово в URL: {stopword}")
                    self.event = None
            if self.event is not None and len(self.event_str) == 0:
                self.event = None
            if self.event is not None:
                for word in self.change_words:
                    self.event_str = self.event_str.replace(word, ' ')

                    self.event_str = re.sub(r'https?://sth_to_find\.ru/\S+', '', self.event_str)

                    # Удаляем все хэштеги
                    self.event_str = re.sub(r'#\w+', '', self.event_str)

                    self.event.text = self.event_str
        except Exception as error:
            logging.critical(f"Не смог check_stopwords_and_empty_message ---> {error}")
            self.event = None


    async def send_post(self):
        try:
            if self.event is not None:
                await self.client.send_message(DESTINATION_CHANNEL, self.event)
        except Exception as error:
            logging.critical(f"Не смог отправить сообщение ---> {error}")
