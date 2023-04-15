import logging
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup , InlineKeyboardButton
from aiogram import Bot , Dispatcher, executor,types
from anime import *
TOKEN='6052786623:AAEREYK7XcIZ97mH0I2k9_0o_SQz6brVrJw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    
     await message.answer('Привет! я бот который ищет аниме по твоим предпочтениям')
     start = '/start'
     genre = '/genre' 
          
     
     await message.answer(f'Команды {start} и {genre} помогут тебе с этим')

@dp.message_handler(commands='genre')
async def start(message: types.Message):

     kb = [
          
               [types.KeyboardButton("Боевик")],
               [types.KeyboardButton("Сёнэн")],
               [types.KeyboardButton("Боевые искуства")],
               [types.KeyboardButton("Военные")],
               [types.KeyboardButton("Гарем")],
               [types.KeyboardButton("Демоны")],
               [types.KeyboardButton("Детектив")],
               [types.KeyboardButton("Драма")],
               [types.KeyboardButton("Идолы")],
               [types.KeyboardButton("Исекай")],
               [types.KeyboardButton("Киберпанк")],
               [types.KeyboardButton("Комедия")],
               [types.KeyboardButton("Магия")],
               [types.KeyboardButton("машины")],
               [types.KeyboardButton("Повседневность")],
               [types.KeyboardButton("Постапокалиптика")],
               [types.KeyboardButton("Приключения")],
               [types.KeyboardButton("Психологический")],
               [types.KeyboardButton("Романтика")],
               [types.KeyboardButton("Спокон")],
               [types.KeyboardButton("Суперсила")],
               [types.KeyboardButton("Триллер")],
               [types.KeyboardButton("Фантастика")],
               [types.KeyboardButton("Экшн")],
          
     ]
     keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
     await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)

     


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    if(message.text == "Боевик"):
       await message.answer("Окей сейчас найдем тебе что-то")
        
       anime_1 = {
          1:'Пламенная бригада пожарных',
          2:'Самурай Чамплу ',
          3:'Корона Грешника',
          4:'SABIKUI BISCO',
          5:'Убийца гоблинов',
          6:'Клинков бесконечный край',
          7:'Класс убийц',
          8:' Ковбой Бибоп',
          9:'Пожиратель душ ',
          10:'Гуррен-Лаганн'
       } 
       await message.answer(f'1:{anime_1[1]}\n2:{anime_1[2]}\n3:{anime_1[3]}\n4:{anime_1[4]}\n5:{anime_1[5]}\n6:{anime_1[6]}\n7:{anime_1[7]}\n8:{anime_1[8]}\n9:{anime_1[9]}\n10:{anime_1[10]}') 
     
    
     
       kb_1 = [
          
               [KeyboardButton(text ="Пламенная бригада пожарных")],
               [KeyboardButton(text ="Самурай Чамплу ")],
               [KeyboardButton(text ="Корона Грешника")],
               [KeyboardButton(text ="SABIKUI BISCO")],
               [KeyboardButton(text ="Убийца гоблинов")],
               [KeyboardButton(text ="Клинков бесконечный край")],
               [KeyboardButton(text ="Класс убийц")],
               [KeyboardButton(text =" Ковбой Бибоп")],
               [KeyboardButton(text ="Пожиратель душ")],
               [KeyboardButton(text ="Гуррен-Лаганн")],
          
         ]
       keyboard_1 = types.ReplyKeyboardMarkup(keyboard=kb_1 , resize_keyboard=True)
       
       await message.answer('Вот список, выбирай',reply_markup=keyboard_1)

@dp.callback_query_handler()
async def get_anime_info(callback_query: types.CallbackQuery):
    if (message.text == "Пламенная бригада пожарных"):
       await bot.send_photo(callback_query.message.chat.id, answer_1[callback_query.data]["photo"])
       url= answer_1[callback_query.data]["site_url"]
       anime_rating = answer_1[callback_query.data]["rating"]
       anime_description = answer_1[callback_query.data]["description"]
       message = f"Anime url: {url}\nAbout: {anime_description}\nRate:{anime_rating}" 
       await bot.send_message(callback_query.message.chat.id, message, parse_mode="html")
    else:
        await bot.send_message(callback_query.message.chat.id, "Аніме не знайдено")  

   #  if (message.text == "Пламенная бригада пожарных"):
   #    answer_1 = {
   #          'name': 'Пламенная бригада пожарных', 
   #          'site_url':'https://jut.su/enen-no-shouboutai/season-1/episode-1.html',
   #          'photo':'data:image/jpeg;base64,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',
   #          'description':'Несколько лет назад в Токио появились необычные люди, которые несли большую опасность общественности. С этими особыми происходило нечто мистическое, а именно спонтанное воспламенение. Огонь появлялся из тел этих людей, и всё вокруг сгорало от разрушительного пожара. Никто не мог объяснить странный феномен, и граждане города боялись появления новых самовозгорающихся особей. В скором времени их начали называть инферналами. Спустя несколько лет произошла эволюция неизученных существ и теперь этих монстров не так боятся как прежде. ',
   #          'rating':' 7,7/10'  
   #        }
             
     
      
     
      
  
        
     
        
    if(message.text == "Сёнэн"):
        await message.answer("Окей сейчас найдем тебе что-то")
        
        anime_2 = {
           1:'Ван-Пис',
           2:'Доктор Стоун: Новый мир',
           3:'Клинок, рассекающий демонов',
           4:'Токийские мстители',
           5:'Моя геройская академия',
           6:'Атака титанв',
           7:'Наруто',
           8:'Блич',
           9:'Мобильный воин Гандам ',
           10:'Семь смертных грехов'
        }
        await message.answer(f'1:{anime_2[1]}\n2:{anime_2[2]}\n3:{anime_2[3]}\n4:{anime_2[4]}\n5:{anime_2[5]}\n6:{anime_2[6]}\n7:{anime_2[7]}\n8:{anime_2[8]}\n9:{anime_2[9]}\n10:{anime_2[10]}')#      kb_2 = [
        kb_2 = [    
                [types.KeyboardButton("Ван-Пис")],
                [types.KeyboardButton("Доктор Стоун: Новый мир")],
                [types.KeyboardButton("Клинок, рассекающий демонов")],
                [types.KeyboardButton("Токийские мстители")],
                [types.KeyboardButton("Моя геройская академия")],
                [types.KeyboardButton("Атака титанв")],
                [types.KeyboardButton("Наруто")],
                [types.KeyboardButton("Блич")],
                [types.KeyboardButton("Мобильный воин Гандам")],
                [types.KeyboardButton("Семь смертных грехов")],
          
      ] 
        keyboard_2 = types.ReplyKeyboardMarkup(keyboard=kb_2 , resize_keyboard=True)
        await message.answer('Вот список, выбирай',reply_markup=keyboard_2)
     
    

 

    if(message.text == "Боевые искуства"):
        await message.answer("Окей сейчас найдем тебе что-то")
        anime_3 = {
           1:'Седьмой киллер',
           2:'Dragon Ball',
           3:'Кулак Северной звезды',
           4:'Боец Баки',
           5:'Кэнган Асура',
           6:'Отчёт о буйстве духов',
           7:'Эпоха смут',
           8:'Виртуальный боец',
           9:'Небо и земля: Бои без правил ',
           10:'Ящик предложений Мэдаки'
        }
        await message.answer(f'1:{anime_3[1]}\n2:{anime_3[2]}\n3:{anime_3[3]}\n4:{anime_3[4]}\n5:{anime_3[5]}\n6:{anime_3[6]}\n7:{anime_3[7]}\n8:{anime_3[8]}\n9:{anime_3[9]}\n10:{anime_3[10]}')
        kb_3 = [    
                [types.KeyboardButton("Седьмой киллер")],
                [types.KeyboardButton("Dragon Ball")],
                [types.KeyboardButton("Кулак Северной звезды")],
                [types.KeyboardButton("Боец Баки")],
                [types.KeyboardButton("Кэнган Асура")],
                [types.KeyboardButton("Отчёт о буйстве духов")],
                [types.KeyboardButton("Эпоха смут")],
                [types.KeyboardButton("Виртуальный боец")],
                [types.KeyboardButton("Небо и земля: Бои без правил")],
                [types.KeyboardButton("Ящик предложений Мэдаки")],
          
      ] 
        keyboard_3 = types.ReplyKeyboardMarkup(keyboard=kb_3 , resize_keyboard=True)
        await message.answer('Вот список выбирай',reply_markup=keyboard_3)

    if(message.text == "Военные"):
        await message.answer("Окей сейчас найдем тебе что-то")           
        anime_4 = {
           1:'Код Гиас',
           2:'Последний Серафим',
           3:'Военная хроника маленькой девочки',
           4:'Врата: там бьются наши воины',
           5:'Восемьдесят шесть',
           6:'Берсерк',
           7:'Стальная тревога',
           8:' Призрак в доспехах: Синдром одиночки',
           9:'Вальврейв Освободитель ',
           10:'Судный день'
        }
        await message.answer(f'1:{anime_4[1]}\n2:{anime_4[2]}\n3:{anime_4[3]}\n4:{anime_4[4]}\n5:{anime_4[5]}\n6:{anime_4[6]}\n7:{anime_4[7]}\n8:{anime_4[8]}\n9:{anime_4[9]}\n10:{anime_4[10]}')
        kb_4 = [    
                [types.KeyboardButton("Код Гиас")],
                [types.KeyboardButton("Последний Серафим")],
                [types.KeyboardButton("Военная хроника маленькой девочки")],
                [types.KeyboardButton("Врата: там бьются наши воины")],
                [types.KeyboardButton("Восемьдесят шесть")],
                [types.KeyboardButton("Берсерк")],
                [types.KeyboardButton("Стальная тревога")],
                [types.KeyboardButton("Призрак в доспехах: Синдром одиночки")],
                [types.KeyboardButton("Вальврейв Освободитель ")],
                [types.KeyboardButton("Судный день")],
          
      ] 
        keyboard_4 = types.ReplyKeyboardMarkup(keyboard=kb_4 , resize_keyboard=True)
        await message.answer('Вот список, выбирай',reply_markup=keyboard_4)
    if(message.text == "Гарем"):
        await message.answer("Окей сейчас найдем тебе что-то")            
        anime_5 = {
           1:'Пять невест',
           2:'Рандеву с жизнью',
           3:'Хроники непобеждённого Бахамута',
           4:'Мифический дух: Хроники',
           5:'Фермерская жизнь в ином мире',
           6:'Связанные небом',
           7:'Король магических стрел и Ванадис',
           8:'Маг-целитель: Новый старт',
           9:'Тотальный гарем ',
           10:'Старшая школа DxD'
        }
        await message.answer(f'1:{anime_5[1]}\n2:{anime_5[2]}\n3:{anime_5[3]}\n4:{anime_5[4]}\n5:{anime_5[5]}\n6:{anime_5[6]}\n7:{anime_5[7]}\n8:{anime_5[8]}\n9:{anime_5[9]}\n10:{anime_5[10]}')
        kb_5 = [    
                [types.KeyboardButton("Пять невест")],
                [types.KeyboardButton("Рандеву с жизнью")],
                [types.KeyboardButton("Хроники непобеждённого Бахамута")],
                [types.KeyboardButton("Мифический дух: Хроники")],
                [types.KeyboardButton("Фермерская жизнь в ином мире")],
                [types.KeyboardButton("Связанные небом")],
                [types.KeyboardButton("Король магических стрел и Ванадис")],
                [types.KeyboardButton("Маг-целитель: Новый старт")],
                [types.KeyboardButton("Тотальный гарем ")],
                [types.KeyboardButton("Старшая школа DxD")],
          
      ] 
        keyboard_5 = types.ReplyKeyboardMarkup(keyboard=kb_5 , resize_keyboard=True)
        await message.answer('Вот список ,выбирай',reply_markup=keyboard_5)
    if(message.text == "Демоны"):
        await message.answer("Окей сейчас найдем тебе что-то")      
        anime_6 = {
           1:'Синий экзорцист',
           2:'Повелитель тьмы на подработке!',
           3:'Дороро',
           4:'Магическая битва',
           5:'О моём перерождении в слизь',
           6:'Тёмный дворецкий',
           7:'Очень приятно, Бог',
           8:'Человек-бензопила',
           9:'Кровавый парень ',
           10:'Тетрадь дружбы Нацумэ'
        }
        await message.answer(f'1:{anime_6[1]}\n2:{anime_6[2]}\n3:{anime_6[3]}\n4:{anime_6[4]}\n5:{anime_6[5]}\n6:{anime_6[6]}\n7:{anime_6[7]}\n8:{anime_6[8]}\n9:{anime_6[9]}\n10:{anime_6[10]}')
        kb_6 = [    
                [types.KeyboardButton("Синий экзорцист")],
                [types.KeyboardButton("Повелитель тьмы на подработке!")],
                [types.KeyboardButton("Дороро")],
                [types.KeyboardButton("Магическая битва")],
                [types.KeyboardButton("О моём перерождении в слизь")],
                [types.KeyboardButton("Тёмный дворецкий")],
                [types.KeyboardButton("Очень приятно, Бог")],
                [types.KeyboardButton("Человек-бензопила")],
                [types.KeyboardButton("Кровавый парень")],
                [types.KeyboardButton("Тетрадь дружбы Нацумэ")],
          
      ] 
        keyboard_6 = types.ReplyKeyboardMarkup(keyboard=kb_6 , resize_keyboard=True)
        await message.answer('Вот список, выбирай',reply_markup=keyboard_6)
    if(message.text == "Детектив"):             
        await message.answer("Окей сейчас найдем тебе что-то")      
        anime_7 = {
           1:'Тетрадь смерти',
           2:'Монстр',
           3:'Ложные выводы',
           4:'Темный дворецкий ',
           5:'Обещаный Неверленд ',
           6:'Игра друзей',
           7:'Эхо терора',
           8:'Данганронпа: Школа отчаяния',
           9:'Амнезия ',
           10:'Когда плачут Цикады'
        }
        await message.answer(f'1:{anime_7[1]}\n2:{anime_7[2]}\n3:{anime_7[3]}\n4:{anime_7[4]}\n5:{anime_7[5]}\n6:{anime_7[6]}\n7:{anime_7[7]}\n8:{anime_7[8]}\n9:{anime_7[9]}\n10:{anime_7[10]}')
        kb_7 = [    
                [types.KeyboardButton("Тетрадь смерти")],
                [types.KeyboardButton("Монстр")],
                [types.KeyboardButton("Ложные выводы")],
                [types.KeyboardButton("Темный дворецкий")],
                [types.KeyboardButton("Обещаный Неверленд")],
                [types.KeyboardButton("Тёмный дворецкий")],
                [types.KeyboardButton("Эхо терора")],
                [types.KeyboardButton("Данганронпа: Школа отчаяния")],
                [types.KeyboardButton("Амнезия ")],
                [types.KeyboardButton("Когда плачут Цикады")],
          
      ] 
        keyboard_7 = types.ReplyKeyboardMarkup(keyboard=kb_7 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_7)

    if(message.text == "Драма"):
        await message.answer("Окей сейчас найдем тебе что-то") 
        anime_8 = {
           1:'Врата Штейна',
           2:'Атака титанов',
           3:'Стальной Алхимик:братство',
           4:'Форма голоса ',
           5:'Вайолет Эвергарден ',
           6:'Код Гиас',
           7:'Сага о Винланде',
           8:'Ходячий замок',
           9:'Евангелион ',
           10:'Идеальная Грусть'
        }
        
        await message.answer(f'1:{anime_8[1]}\n2:{anime_8[2]}\n3:{anime_8[3]}\n4:{anime_8[4]}\n5:{anime_8[5]}\n6:{anime_8[6]}\n7:{anime_8[7]}\n8:{anime_8[8]}\n9:{anime_8[9]}\n10:{anime_8[10]}')
        kb_8 = [    
                [types.KeyboardButton("Врата Штейна")],
                [types.KeyboardButton("Атака титанов")],
                [types.KeyboardButton("Стальной Алхимик:братство")],
                [types.KeyboardButton("Форма голоса")],
                [types.KeyboardButton("Евангелион")],
                [types.KeyboardButton("Вайолет Эвергарден")],
                [types.KeyboardButton("Код Гиас")],
                [types.KeyboardButton("Сага о Винланде")],
                [types.KeyboardButton("Ходячий замок ")],
                [types.KeyboardButton("Идеальная Грусть")],
          
      ] 
        keyboard_8 = types.ReplyKeyboardMarkup(keyboard=kb_8 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_8)
    if(message.text == "Идолы"):
        await message.answer("Окей сейчас найдем тебе что-то")   
        anime_9 = {
           1:'Рассвет идолов',
           2:'Дети идолов',
           3:'Music Girls',
           4:'Idol Incident',
           5:'Locodol',
           6:'Macross Delta',
           7:'Macross',
        
        }
        await message.answer(f'1:{anime_9[1]}\n2:{anime_9[2]}\n3:{anime_9[3]}\n4:{anime_9[4]}\n5:{anime_9[5]}\n6:{anime_9[6]}\n7:{anime_9[7]}')
        kb_9 = [    
                [types.KeyboardButton("Рассвет идолов")],
                [types.KeyboardButton("Дети идолов")],
                [types.KeyboardButton("Music Girls")],
                [types.KeyboardButton("Idol Incident")],
                [types.KeyboardButton("Locodol")],
                [types.KeyboardButton("Macross Delta")],
                [types.KeyboardButton("Macross")]
          
      ] 
        keyboard_9 = types.ReplyKeyboardMarkup(keyboard=kb_9 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_9)
    if(message.text == "Исекай"):
        await message.answer("Окей сейчас найдем тебе что-то")   
        anime_10 = {
           1:'Реинкорнация безработного',
           2:'Нет игры-нет жизни',
           3:'О моём перерождении в слизь',
           4:' Мастера меча онлайн ',
           5:'Возрождающие ',
           6:' Да я паук и что',
           7:'В другом мире со смартфоном',
           8:'Восхождение героя щита',
           9:'Лучший в мире убийца переродился в другом мире в аристократа ',
           10:'Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня'
        }
        await message.answer(f'1:{anime_10[1]}\n2:{anime_10[2]}\n3:{anime_10[3]}\n4:{anime_10[4]}\n5:{anime_10[5]}\n6:{anime_10[6]}\n7:{anime_10[7]}\n8:{anime_10[8]}\n9:{anime_10[9]}\n10:{anime_10[10]}')
        kb_10 = [    
                [types.KeyboardButton("Реинкорнация безработного")],
                [types.KeyboardButton("Нет игры-нет жизни")],
                [types.KeyboardButton("О моём перерождении в слизь")],
                [types.KeyboardButton("Мастера меча онлайн")],
                [types.KeyboardButton("Возрождающие")],
                [types.KeyboardButton("Да я паук и что")],
                [types.KeyboardButton("В другом мире со смартфоном")],
                [types.KeyboardButton("Восхождение героя щита")],
                [types.KeyboardButton("Лучший в мире убийца переродился в другом мире в аристократа ")],
                [types.KeyboardButton("Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня")],
          
      ] 
        keyboard_10 = types.ReplyKeyboardMarkup(keyboard=kb_10 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_10)
    if(message.text == "Киберпанк"):
        await message.answer("Окей сейчас найдем тебе что-то")
        anime_11 = {
           1:'Бегущий по краю',
           2:'Акира',
           3:'Эксперементы Лейн',
           4:'Призрак в Доспехах',
           5:'Психопаспорт',
           6:'Акудама Драйв',
           7:'Измерение W',
           8:'Метрополис',
           9:'Армитаж',
           10:'Технолайз'
        }
        await message.answer(f'1:{anime_11[1]}\n2:{anime_11[2]}\n3:{anime_11[3]}\n4:{anime_11[4]}\n5:{anime_11[5]}\n6:{anime_11[6]}\n7:{anime_11[7]}\n8:{anime_11[8]}\n9:{anime_11[9]}\n10:{anime_11[10]}')
        kb_11 = [    
                [types.KeyboardButton("Бегущий по краю")],
                [types.KeyboardButton("Акира")],
                [types.KeyboardButton("Эксперементы Лейн")],
                [types.KeyboardButton("Призрак в Доспехах")],
                [types.KeyboardButton("Психопаспорт")],
                [types.KeyboardButton("Акудама Драйв")],
                [types.KeyboardButton("Измерение W")],
                [types.KeyboardButton("Метрополис")],
                [types.KeyboardButton("Армитаж")],
                [types.KeyboardButton("Технолайз")],
          
      ] 
        keyboard_11 = types.ReplyKeyboardMarkup(keyboard=kb_11 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_11)                  
   #   if(message.text == "Комедия"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "Магия"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "машины"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "Повседневность"):
   #      await message.answer("Окей сейчас найдем тебе что-то")        

   #   if(message.text == "Постапокалиптика"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "Приключения"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "Психологический"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "Романтика"):
   #      await message.answer("Окей сейчас найдем тебе что-то")     

   #   if(message.text == "Спокон"):
   #      await message.answer("Окей сейчас найдем тебе что-то")  

   #   if(message.text == "Триллер"):
   #      await message.answer("Окей сейчас найдем тебе что-то")        

   #   if(message.text == "Фантастика"):
   #      await message.answer("Окей сейчас найдем тебе что-то")

   #   if(message.text == "Экшн"):
   #      await message.answer("Окей сейчас найдем тебе что-то")






















if __name__ == '__main__':
    executor.start_polling(dp)     