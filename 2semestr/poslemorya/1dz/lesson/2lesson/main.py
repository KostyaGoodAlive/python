import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


import os
from dotenv import load_dotenv

from utils import check_query
from parse import get_vacancies
from registration import Database
load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database()
  

@dp.message_handler(commands='start')
async def start_process(message):
    user = await db.check_user(message.from_id)
    if not user:
        await db.register_user(
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.from_id
        )
        
        await message.answer('thx for registration')
    else:
        await message.answer('u already registred')    
    await message.answer('Привіт. Введи свій пошуковий запит.')


@dp.message_handler(content_types='text')
async def get_jobs(message: types.Message):
    if not check_query(message.text):
        await message.answer('Будь ласка, введи пошукий запит через пробіли.')
    else:
        query = message.text.lower().strip()
        vacancies = get_vacancies(query)
        for vacancy in vacancies:
            title = vacancy['title']
            company = vacancy['company']
            url = vacancy['url']
            description = vacancy['description']

            msg = (f'<b>Вакансія:</b> {title}\n<b>Компанія:</b> {company}\n<b>Опис:</b> {description}\n\n<b'
                   f'>Посилання:</b> {url}')
            await message.answer(text=msg, parse_mode='html', disable_web_page_preview=True)

   

if __name__ == '__main__':
    executor.start_polling(dp)