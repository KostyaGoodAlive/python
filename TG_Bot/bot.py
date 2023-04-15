import logging


from aiogram import Bot , Dispatcher, executor,types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import *


TOKEN='5993367115:AAFbFtjGqQkEQl0cEAgliyFfQYMFXUHjDLs'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot , storage=MemoryStorage)
films = {
    'Джон Уік 4': {
    'site_url':'https://planetakino.ua/movies/john-wick-chapter-4/#today',
    'photo':'https://planetakino.ua/res/get-poster/00000000000000000000000000002667/jw4-vend.jpg',
    'description':'Кримінальний бойовик «Джон Уік 4» є продовженням однойменних фільмів, що виходять на екрани починаючи з 2014 року. Незмінним виконавцем головної ролі залишається Кіану Рівз.',
    'rating':'8.3/10'
},
 'Крід IІI: Спадок Роккі Бальбоа (16+)': {
    'site_url':'https://planetakino.ua/movies/creed-iii/#today',
    'photo':'https://planetakino.ua/res/get-poster/00000000000000000000000000003784/vend2.jpg',
    'description':'Спортивна драма «Крід IІI: Спадок Роккі Бальбоа» є прямим продовженням однойменних фільмів, що вийшли на екрани у 2015 та 2018 роках, а також девятою частиною франшизи «Роккі».',
    'rating':'7.1/10'
},
'Шазам! Лють Богів': {
    'site_url':'https://planetakino.ua/movies/shazam-fury-of-the-gods/#today',
    'photo':'https://planetakino.ua/res/get-poster/00000000000000000000000000002506/shazam2-vend4.jpg',
    'description':'Комедійне фентезі «Шазам! Лють Богів» – це новий, 12-й фільм з розширеного кіно всесвіту коміксів DC та пряме продовження фільму 2019 року про цього героя.',
    'rating':'6.4/10'
},
'Зупинити Голіафа (12+)': {
    'site_url':'https://planetakino.ua/movies/against-all-odds/#today',
    'photo':'https://planetakino.ua/res/get-poster/00000000000000000000000000003970/goliaf-vend.jpg',
    'description':'Фільм відповідає на питання, як Україна змогла протистояти Росії, незважаючи на те, що світові експерти давали їй не більше 3 днів. І як вона практично змусила Росію відмовитися від початкових планів бліцкригу захоплення ',
    'rating':'8.4/10'
},
'Ейр (12+)': {
    'site_url':'https://planetakino.ua/movies/air/#today',
    'photo':'https://planetakino.ua/res/get-poster/00000000000000000000000000003921/air-vend.jpg',
    'description':'Драма «Ейр» має у своїй основі реальні події. Головний герой фільму Сонні Ваккаро підписав доленосний контракт з Джорданом у 1984 році. Відтоді випущено 37 моделей кросівок Air Jordan та кілька модифікованих лінійок. Сценарій до фільму було написано у 2021 році і він очолив список кращих нереалізованих сценаріїв року.',
    'rating':'7.4/10'
}
    
    }
    
@dp.message_handler(commands='start')
async def start(message: types.Message):
     await message.answer('Привіт! Я - бот-кіноафіша🍿\nОбери фільм', reply_markup=film_choice) 

ADMINS = [1340618751]
@dp.callback_query_handler()
async def get_film_info(callback_query: types.CallbackQuery):
    if callback_query.data in films.keys():
       await bot.send_photo(callback_query.message.chat.id, films[callback_query.data]["photo"])
       url= films[callback_query.data]["site_url"]
       film_rating = films[callback_query.data]["rating"]
       film_description = films[callback_query.data]["description"]
       message = f"Film url: {url}\nAbout: {film_description}\nRate:{film_rating}" 
       await bot.send_message(callback_query.message.chat.id, message, parse_mode="html")
    else:
        await bot.send_message(callback_query.message.chat.id, "Фільм не знайдено")  


file = open('TG_Bot/films.txt' , 'w')
@dp.message_handler(commands='add_film')
async def add_new_film(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in ADMINS:       
        await message.answer(text='Введи назву фільму , якого хочешь додати')
        await state.set_state('set_film_name')
        file.write(message)
    else:
        await message.answer(text='У вас не достатньо прав для цієї операції')   


film_name = ''

@dp.message_handler(state='set_film_name')
async def set_film_name(message: types.Message, state:FSMContext):
    if len(message.text) > 64:
        message.answer(text='На жалб я не можу доодати цей фільм адже довжина його назви не має бути більше за 64 символи')
    else:
        film_name = message.text
        films[film_name] = {}
        await state.set_state('set_site_url')
        await message.answer(text='Добре, тепер введи посилання на вебсайт')   
        file.write(message)
@dp.message_handler(state='set_site_url')
async def set_film_name(message: types.Message, state:FSMContext):
    global film_name
    film_site_url = message.text
    films[film_name]['site_url'] = film_site_url
    await state.set_state('set_description')
    await message.answer(text='Чудово тепер напиши щось про цей фільм')
    file.write(message)
@dp.message_handler(state='set_description')
async def set_film_name(message: types.Message, state:FSMContext): 
    global film_name
    film_desription = message.text
    films[film_name]['description'] = film_desription
    await state.set_state('set_rating')
    await message.answer (text='Чудово тепер введи рейтинг фільму') 
    file.write(message)
@dp.message_handler(state='set_ratig')
async def set_film_name(message: types.Message, state:FSMContext): 
    global film_name
    film_rating = message.text
    films[film_name]['rating'] = film_rating
    await state.set_state('set_photo')
    await message.answer (text='Чудово тепер дай посилання на банер фільму')
    file.write(message)
@dp.message_handler(state='set_photo')
async def set_film_name(message: types.Message, state:FSMContext): 
    global film_name
    film_photo = message.text
    films[film_name]['photo'] = film_photo
    print(films)
    await state.finish()
    await message.answer (text='Супер! новий фільм створено')     
    file.write(message)
file.close()     
if __name__ == '__main__':
    executor.start_polling(dp)

