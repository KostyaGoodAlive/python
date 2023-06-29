import logging
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram import Bot , Dispatcher, executor,types
from aiogram.dispatcher import FSMContext
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from steps import TrafficLights , Flow
from keyboards import lights_all , read_kb , yellow_kb , green_kb , traffic_off_kb , request1
load_dotenv()


TOKEN=os.getenv('TOKEN')



logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привіт! я бот із машинами станів . Давайте вас зареєструємо!', reply_markup=request1)


@dp.message_handler(text ='Давайте')
async def name(message: types.Message):
        await Flow.Name.set()
        await message.answer("Напишіть своє ФІО")
        file = open('after_hakaton/registr.txt', 'w')
        file.write(f'{message.text}\n')
@dp.message_handler(text ='Ні не хочу')
async def name(message: types.Message):
     await message.answer('Якщо не ви не зареєструєтесь , то бот не буде працювати')


@dp.message_handler(content_types='text' , state=Flow.Name) 
async def Email(message: types.Message):
    await Flow.Email.set()
    await message.answer('Введіть свій Email у форматі - Uk_rAin65e@gmail.com')
    file = open('after_hakaton/registr.txt', 'a')
    file.write(f'{message.text}\n')
@dp.message_handler(content_types='text' , state=Flow.Email) 
async def pasword(message: types.Message):
    await Flow.pasword.set()
    await message.answer('Введіть свій пароль')
    file = open('after_hakaton/registr.txt', 'a')
    file.write(f'{message.text}\n')
@dp.message_handler(content_types='text' , state=Flow.pasword) 
async def repeat(message: types.Message):
    await Flow.end.set()
    await message.answer('Ви зараєстровані, дякую за реєстрацію!')
@dp.message_handler(commands='start', state =Flow.end)
async def start(message: types.Message):
    await message.answer('Ви вже прошли процес реєстрації')



# @dp.message_handler(commands='traffic_light_on', state='*')
# async def traffic_light_on(message: types.Message):
#     await TrafficLights.stateOn.set()
#     await message.answer('Ви увімкнули світлофор\n'
#                          'Тепер ви можете увімкнути будь-яке світло:',
#                          reply_markup=lights_all)

# @dp.message_handler(text ='🔴',state= TrafficLights.stateOn)
# async def traffic_red(message: types.Message):
#     await TrafficLights.stateRed.set()
#     await message.answer('Ви увімкнули червоне світло🔴 \nтепер ви можете увімкнути жовте',reply_markup=yellow_kb)

# @dp.message_handler(text ='🟡',state= TrafficLights.stateRed)
# async def traffic_red(message: types.Message):
#     await TrafficLights.stateYellow.set()
#     await message.answer('Ви увімкнули жовте світло🟡 \nтепер ви можете увімкнути зелене',reply_markup=green_kb)

# @dp.message_handler(text ='🟢',state= TrafficLights.stateYellow)
# async def traffic_red(message: types.Message):
#     await TrafficLights.stateGreen.set()
#     await message.answer('Ви увімкнули зелене світло🟢 \nтепер ви можете вимкнути світофор',reply_markup=traffic_off_kb)

# @dp.message_handler(text ='Завершити',state= TrafficLights.stateGreen)
# async def traffic_red(message: types.Message):
#     await dp.current_state().reset_state()
#     await message.answer('Ви вимкнули світофор\n'
#                          'Щоб увімкнути натисніть - /traffic_light_on')

if __name__ == '__main__':
    executor.start_polling(dp)