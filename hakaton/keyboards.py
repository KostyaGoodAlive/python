from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import tarifs , tarif2 , tarif3 , tarif4
question1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton('/Поїхали')

question1.add(b1)




question2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

asn1 = KeyboardButton('1')
asn2 = KeyboardButton('2')
asn3 = KeyboardButton('3')
question2.row(asn1, asn2, asn3,)





question3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

an1 = KeyboardButton('1')
an2 = KeyboardButton('2')
an3 = KeyboardButton('3')

question3.row(an1, an2, an3,)





question4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
asn1 = KeyboardButton('1')
asn2 = KeyboardButton('2')
asn3 = KeyboardButton('3')

question4.row(asn1, asn2, asn3)







asn1 = KeyboardButton('Мобільний Інтернет')
asn2 = KeyboardButton('Висока вартість дзвінків')
asn3 = KeyboardButton('Неможливість використання роумінгу')
asn4 = KeyboardButton('Обмеження використання послуги в певні часи')
question5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
question5.add(asn1)
question5.add(asn2)
question5.add(asn3)
question5.add(asn4)


tarif_choice1 = InlineKeyboardMarkup()
for tarif in tarifs:
    button = InlineKeyboardButton(text=tarif, callback_data=tarifs)
    tarif_choice1.add(button)




tarif_choice2 = InlineKeyboardMarkup()
for tarif in tarif2:
    button = InlineKeyboardButton(text=tarif, callback_data=tarif2)
    tarif_choice2.add(button)


tarif_choice3 = InlineKeyboardMarkup()
for tarif in tarif3:
    button = InlineKeyboardButton(text=tarif, callback_data=tarif3)
    tarif_choice3.add(button)


tarif_choice4 = InlineKeyboardMarkup()
for tarif in tarif4:
    button = InlineKeyboardButton(text=tarif, callback_data=tarif4)
    tarif_choice4.add(button)