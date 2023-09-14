import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from state import *
from database import Database
TOKEN='6199291765:AAFgTT2G1Nx6BAMURfQQ9-BZQr_ALjuu6JI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_proces(message: types.Message):
    await message.answer('Wlcome!\nEnter your name.')
    await Registration.set_name.set()

@dp.message_handler(state=Registration.set_name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('Nice\nNow enter your age.')
    await Registration.set_age.set()


@dp.message_handler(state=Registration.set_age)
async def set_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer('Good!\nNow enter your email.')
    await Registration.set_email.set()

@dp.message_handler(state=Registration.set_email)
async def set_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        name = data['name']
        age = data['age']
        email = message.text

    await db.register_student(name , age , email)    
    await message.answer('You have successfully registred.')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)