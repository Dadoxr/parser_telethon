from config import *
from classes import Post 
from telethon import TelegramClient, events
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG, filename='logging.log', format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')

async def main():
    try:
        client = TelegramClient('parser', API_ID, API_HASH)
        async with client:
            await client.start()
            logging.info("Bot has been started")
            @client.on(events.NewMessage(chats=(SOURCE_CHANNELS_1,
                                                SOURCE_CHANNELS_2,
                                                SOURCE_CHANNELS_3,
                                                SOURCE_CHANNELS_4,
                                                SOURCE_CHANNELS_5)
                                        )
                        )
            async def forward_message(event):
                event_ = Post(event, client)
                if await event_.check_lenth():
                    event_.check_stopwords_and_empty_message()
                    await event_.send_post()
            await client.run_until_disconnected()
            logging.info("Bot has been stopped")
    except Exception as error:
        logging.critical(f'ПРОБЛЕМА\n\n{error}')


if __name__ == '__main__':
    asyncio.run(main())