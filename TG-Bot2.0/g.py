import logging
from aiogram.types import KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv


TOKEN = '6257746141:AAHhVorU0dfctS-wQ9ya1WCp-sUjwB1_gqg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привіт!\nЯ спробую допомогти знайти тобі якусь книгу для читання!\nОбери категорію яка тебе цікавить.')

    start = '/start'
    genre = '/genre'

    await message.answer(f'За допомогою команд {start} та {genre} можешь кирувати ботом')


@dp.message_handler(commands='genre')
async def start(message: types.Message, state:FSMContext):
    kb = [

        [types.KeyboardButton("Найпопулярніші книги 2023 року")],
        [types.KeyboardButton("Детективи")],
        [types.KeyboardButton("Романи")],
        [types.KeyboardButton("Жахи")],
        [types.KeyboardButton("Трилери")],
        [types.KeyboardButton("Фентезі")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
    await message.answer('Яка категорія тобі більш подобається?', reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
   
    if (message.text == "Найпопулярніші книги 2023 року"):
        await message.answer("Ось топ 10 популярних книжок з цієї теми")

        categorie_1 = {

            1: 'Тисяча сяйливих сонць',
            2: 'Фабула',
            3: 'Ворошиловград',
            4: 'Шлях до несвободи',
            5: 'Месопотамія',
            6: 'Місто',
            7: 'Брама Європи',
            8: 'Припини це',
            9: 'Подолати минуле',
            10: 'Задивляюсь у твої зіниці'

        }
        await message.answer(f'1:{categorie_1[1]}\n2:{categorie_1[2]}\n3:{categorie_1[3]}\n4:{categorie_1[4]}\n5:{categorie_1[5]}\n6:{categorie_1[6]}\n7:{categorie_1[7]}\n8:{categorie_1[8]}\n9:{categorie_1[9]}\n10:{categorie_1[10]}')

        kb_1 = [

            [KeyboardButton(text="Тисяча сяйливих сонць")],
            [KeyboardButton(text="Фабула")],
            [KeyboardButton(text="Шлях до несвободи")],
            [KeyboardButton(text="Ворошиловград")],
            [KeyboardButton(text="Месопотамія")],
            [KeyboardButton(text="Місто")],
            [KeyboardButton(text="Брама Європи")],
            [KeyboardButton(text="Припини це")],
            [KeyboardButton(text="Подолати минуле")],
            [KeyboardButton(text="Задивляюсь у твої зіниці")],

        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True, selective=True)
        await message.answer('Вибирай , яка тобі до впотоби', reply_markup=keyboard)


    if (message.text == "Тисяча сяйливих сонць"):
            name = 'Тисяча сяйливих сонць'
            author = 'Халед Госсейні'
            cover = 'https://cdn.vogue.ua/i/original/media/image/63c/a40/076/63ca40076862e.jpg.webp'
            description = '"Тисяча сяйливих сонць" зображує історію дорослішання та дружбу двох дівчат, Маріам і Лейли, яких об`єднують спільні драми (обидві дівчатка виходять заміж у 15 за значно старших чоловіків), боротьба (роман зображує прихід талібів до влади в Кабулі) та, звісно, любов, що здатна перемогти всі руйнування.'
            all = f"Назва: {name}\nАвтор: {author}\nПро книгу: {description}\nОбкладинка: {cover}"
            await bot.send_message(message.from_user.id, all, parse_mode="html")


if __name__ == '__main__':
    executor.start_polling(dp)











@dp.message_handler(content_types=['text'])
async def start(message: types.Message,state:FSMContext):
    if(message.text == "Боевик"):
       await message.answer("Окей сейчас найдем тебе что-то")
        
       anime_1 = {
          1:'Пламенная бригада пожарных🔥',
          2:'Самурай Чамплу🗡️ ',
          3:'Корона Грешника👑',
          4:'Биско-ржавоед',
          5:'Убийца гоблинов👺',
          6:'Клинков бесконечный край⚔️',
          7:'Класс убийц🏫💀',
          8:'Ковбой Бибоп🤠',
          9:'Пожиратель душ ',
          10:'Гуррен-Лаганн'
       } 
       await message.answer(f'1:{anime_1[1]}\n2:{anime_1[2]}\n3:{anime_1[3]}\n4:{anime_1[4]}\n5:{anime_1[5]}\n6:{anime_1[6]}\n7:{anime_1[7]}\n8:{anime_1[8]}\n9:{anime_1[9]}\n10:{anime_1[10]}') 
     
    
     
       kb_1 = [
          
               [KeyboardButton(text ="Пламенная бригада пожарных🔥")],
               [KeyboardButton(text ="Самурай Чамплу🗡️")],
               [KeyboardButton(text ="Корона Грешника👑")],
               [KeyboardButton(text ="Биско-ржавоед")],
               [KeyboardButton(text ="Убийца гоблинов👺")],
               [KeyboardButton(text ="Клинков бесконечный край⚔️")],
               [KeyboardButton(text ="Класс убийц🏫💀")],
               [KeyboardButton(text ="Ковбой Бибоп🤠")],
               [KeyboardButton(text ="Пожиратель душ")],
               [KeyboardButton(text ="Гуррен-Лаганн")],
               [types.KeyboardButton("⬅️Назад")],
          
         ]
       keyboard_1 = types.ReplyKeyboardMarkup(keyboard=kb_1 , resize_keyboard=True)
       
       await message.answer('Вот список, выбирай',reply_markup=keyboard_1)


    if (message.text == "Пламенная бригада пожарных🔥"):
          name = 'Пламенная бригада пожарных'
          site_url='https://rezka.ag/animation/adventures/31532-ognennaya-brigada-pozharnyh-tv-1-2019.html'
          description = 'Несколько лет назад в Токио появились необычные люди, которые несли большую опасность общественности. С этими особыми происходило нечто мистическое, а именно спонтанное воспламенение. Огонь появлялся из тел этих людей, и всё вокруг сгорало от разрушительного пожара. Никто не мог объяснить странный феномен, и граждане города боялись появления новых самовозгорающихся особей. В скором времени их начали называть инферналами. Спустя несколько лет произошла эволюция неизученных существ и теперь этих монстров не так боятся как прежде.'
          rating = '7,7/10'
          mes = f"Название : {name}\nСайт с анимэ: {site_url}\nПро анимэ: {description}\nРейтинг:{rating}"
    if(message.text == "Сёнэн"):
        await message.answer("Окей сейчас найдем тебе что-то")
        
        anime_2 = {
           1:'Ван-Пис',
           2:'Доктор Стоун: Новый мир⚗️',
           3:'Клинок, рассекающий демонов👹🗡️',
           4:'Токийские мстители🏍️',
           5:'Моя геройская академия🏫🦸‍♂️',
           6:'Атака титанов🤺',
           7:'Наруто🍜',
           8:'Блич🗡️',
           9:'Мобильный воин Гандам📱',
           10:'Семь смертных грехов'
        }      