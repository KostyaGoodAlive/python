import logging
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram import Bot , Dispatcher, executor,types
from aiogram.dispatcher import FSMContext
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from steps import Flow
from keyboards import  request1, request
load_dotenv()


TOKEN=os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


count = 5000

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привіт! я бот банкомат')

@dp.message_handler(commands='bank')
async def card(message: types.Message):
    await Flow.Card.set()
    await message.answer("Введіть свою карту")
    

@dp.message_handler(content_types='text' , state=Flow.Card) 
async def pasword(message: types.Message):
    await Flow.pasword.set()
    await message.answer("Введіть пін-код від карти")

@dp.message_handler(content_types='text' , state=Flow.pasword) 
async def operation(message: types.Message):
    await Flow.operation.set()
    await message.answer("Виберіть операцію яку хочете провести", reply_markup=request1)

@dp.message_handler(text ='Перевірити баланс', state=Flow.operation)
async def operation(message: types.Message):
        global count
        await message.answer(f'{count} ваш поточний баланс')
@dp.message_handler(text ='Зняти готівку' ,state=Flow.operation)
async def operation(message: types.Message):
     global count
     await message.answer('Яку суму ви хочете зняти з карты')

@dp.message_handler(content_types='text')
async def operation(message: types.Message):     
     
     await message.answer(f'{count - message.text} ваш залишок')



if __name__ == '__main__':
    executor.start_polling(dp)     