import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import schedule
from threading import Thread
import os
from dotenv import load_dotenv

from parse import anime_news
from parse import anime_getting
from database import Database
load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database()
 
# loop = asyncio.get_event_loop() 
# asyncio.set_event_loop(loop)


@dp.message_handler(commands='news')
async def get_anime(message: types.Message):
    news = anime_news()
    if not news:
        await message.answer('❌Не має нових новин:(❌')
    else:
        for new in news:
            title = new['title']
            description = new['description']
            time = new['time']
            msg = (f'📰Новини📰:\n\nЗагалом: {title}\n\nДетальніше: {description}\n\n{time}')
            await message.answer(text=msg, disable_web_page_preview=True)


@dp.message_handler(commands='start')
async def start_process(message):
    user = await db.check_user(message.from_id)
    if not user:
        await db.register_user(
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_id,
        )
        
        await message.answer('Дякую за реєстрацію!👍')
    else:
        await message.answer('Ви вже зарегестровані!✔️')    
    await message.answer('Привіт! Введи аніме яке хочеш подивитися🍿')



@dp.message_handler(content_types='text')
async def get_anime(message: types.Message):
    query = message.text.lower().strip()
    animes = anime_getting(query)
    if not animes:
        await message.answer('❌Сталася помилка , або ви не правильно ввели пошуковий запит❌')
    else:
        for anime in animes:
            name = anime['name']
            url = anime['url']
            genre = anime['genre']
            description = anime['description']
             
            msg = (f'Аніме: {name}\nЖанр: {genre}\nОпис: {description}\nПосилання:{url}')
            await message.answer(text=msg, disable_web_page_preview=True)



# def notify():
#     send_mess =asyncio.run_coroutine_threadsafe(anime_news(), loop)
#     send_mess.result()


# def run_schedule():
#      schedule.every().day.at('14:45').do(notify)
#      while True:
#         schedule.run_pending()

if __name__ == '__main__':
    executor.start_polling(dp)  