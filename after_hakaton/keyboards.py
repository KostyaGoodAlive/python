from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton




red = KeyboardButton('🔴')
yellow = KeyboardButton('🟡')
green = KeyboardButton('🟢')
traffic_off = KeyboardButton('Завершити')

lights_all = ReplyKeyboardMarkup(resize_keyboard=True).row(red,yellow,green)
read_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(red)
yellow_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(yellow)
green_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(green)
traffic_off_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(traffic_off)



request1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(text = 'Давайте'),KeyboardButton(text = 'Ні не хочу')) 
