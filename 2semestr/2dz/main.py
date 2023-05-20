import logging
import requests
from weather import parse_weather
from aiogram import Bot , Dispatcher, executor,types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN='5848915657:AAH4LthR6KurQzdKgXfhGclGdTBo_IgKvuo'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types='text')
async def get_weather(message: types.Message):

    world_weather = parse_weather(city=message.text)
    min_temperature = round(world_weather['main']['temp_min'] - 273)
    max_temperature = round(world_weather['main']['temp_max'] - 273)
    temperature = round(world_weather['main']['temp'] - 273)
    wind_speed = round(world_weather['wind']['speed'] * 3.6)    
    humidity =  round(world_weather['main']['humidity'])
    await message.answer(f"В місті - {message.text}\nМінімальна температура - {min_temperature}\nМаксимальна температура - {max_temperature}\nТемпература - {temperature}\nШвидкість вітру - {wind_speed}\nВологість в місті - {humidity}")





if __name__ == '__main__':
    executor.start_polling(dp)
