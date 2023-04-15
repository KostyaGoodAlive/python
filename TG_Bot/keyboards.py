from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from bot import films

film_choice = InlineKeyboardMarkup()
for film in films:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choice.add(button)
    # inline_keyboard=[
#     [InlineKeyboardButton(text='Джон Уік 4', callback_data='Джон Уік 4')],
#     [InlineKeyboardButton(text='Крід IІI: Спадок Роккі Бальбоа', callback_data='Крід IІI: Спадок Роккі Бальбоа')]
#     ]
# 