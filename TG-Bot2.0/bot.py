import logging
from aiogram.types import  KeyboardButton
from aiogram import Bot , Dispatcher, executor,types
from aiogram.dispatcher import FSMContext
import os
from dotenv import load_dotenv


load_dotenv()


TOKEN=os.getenv('TOKEN')



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
               [types.KeyboardButton("Приключения")], 
               [types.KeyboardButton("Исекай")],
               [types.KeyboardButton("Киберпанк")],
               [types.KeyboardButton("Спокон")],
               [types.KeyboardButton("Комедия")],
               [types.KeyboardButton("Повседневность")], 
               [types.KeyboardButton("Фантастика")],
          
     ]
     keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
     await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)

     


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
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)       

    if (message.text == "Пламенная бригада пожарных🔥"):
          name = 'Пламенная бригада пожарных'
          site_url='https://rezka.ag/animation/adventures/31532-ognennaya-brigada-pozharnyh-tv-1-2019.html'
          description = 'Несколько лет назад в Токио появились необычные люди, которые несли большую опасность общественности. С этими особыми происходило нечто мистическое, а именно спонтанное воспламенение. Огонь появлялся из тел этих людей, и всё вокруг сгорало от разрушительного пожара. Никто не мог объяснить странный феномен, и граждане города боялись появления новых самовозгорающихся особей. В скором времени их начали называть инферналами. Спустя несколько лет произошла эволюция неизученных существ и теперь этих монстров не так боятся как прежде.'
          rating = '7,7/10'
          mes = f"Название : {name}\nСайт с анимэ: {site_url}\nПро анимэ: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/ncdd73599571euj10g93z.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html") 
    if (message.text == "Самурай Чамплу🗡️"):
          name = 'Самурай Чамплу'
          site_url='https://rezka.ag/animation/samurai/21045-samuray-champlu-2004.html'
          description = 'Аниме-сериал о дружбе, любви и благородстве. В период правления сёгуната Токугавы трое героев путешествуют по стране. Фуу – юная и непосредственная, ее мечта – встретить самурая, пахнущего подсолнухом. Она не знает, как он выглядит и не очень хорошо представляет себе, как на самом деле пахнут подсолнухи. Девочка обожает вкусненько поесть и способна очень быстро набирать вес. В ее кимоно живет Момо – белка, каждый раз покидающая свое убежище.'
          rating = '9.6/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/23/l8e14a3ee9111kg51l26y.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Корона Грешника👑"):
          name = 'Корона Грешника'
          site_url='https://rezka.ag/animation/drama/2414-korona-greshnika-korona-viny.html'
          description = 'Действие аниме-сериала «Корона грешника» происходит в 2039 году в Японии. Вот уже десять лет прошло с момента страшных событий, когда эпидемия вируса под названием «Апокалипсис» разорила многие страны, в том числе и Японию, и загнала ее практически в рабство.'
          rating = '9.24/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/11/23/sb8df3ad73162wr15b52x.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")
    if (message.text == "Биско-ржавоед"):
          name = 'Биско-ржавоед'
          site_url='https://rezka.ag/animation/fiction/45675-bisko-rzhavoed-2022.html'
          description = 'После огромного взрыва, разрушившего Токио, всю землю покрывает красная пыль, которая уничтожает всё на своём пути. Воздействие пыли вызывает у людей болезнь, которая распространяет по телу больного болячки цвета ржавчины и в конце концов убивает.'
          rating = '8.93/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/1/11/u7dcf869f7790kh28f58x.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")      
    if (message.text == "Убийца гоблинов👺"):
          name = 'Убийца гоблинов'
          site_url='https://rezka.ag/animation/fantasy/28612-ubiyca-goblinov-2018.html'
          description = 'Действие аниме разворачивается в фантастическом мире, похожем на компьютерную игру, где живут различные монстры. Местные жители, пытаясь заработать себе на жизнь, вступают в ряды авантюристов, чтобы получить доступ к заданиям различной сложности, за которые полагается вознаграждение.'
          rating = '9.34/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/z254b0c5369aazi27u88h.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")
    if (message.text == "Клинков бесконечный край⚔️"):
          name = 'Клинков бесконечный край'
          site_url='https://rezka.ag/animation/fantasy/17803-sudba-noch-shvatki-klinkov-beskonechnyy-kray-2010.html'
          description = 'Очередное фентезийное творение в японской анимации от режиссера Кенити Такесито.Юный герой Сиро Эмия спокойно проживал свою жизнь в огромном поместье, которое досталось ему в наследство от покойного отца. Он уже давно научился самостоятельно справляться со всеми трудностями и жить по совести и с честью. Скромный магический дар и верные друзья были его постоянными спутниками на протяжении всей его недолгой жизни.'
          rating = '8.53/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/8/3/fa7f43d72bb2fss33s98i.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  

    if (message.text == "Класс убийц🏫💀"):
          name = 'Класс убийц'
          site_url='https://rezka.ag/animation/comedy/12373-klass-ubiyc-2015.html'
          description = 'В один прекрасный момент над всей Землёй нависает ужасная катастрофа полного уничтожения. Всему виной оказывается с виду забавное существо по имени Коро, похожее на желтого осьминога, которое жутко обижается, когда его называют пришельцем, доказывая, что оно является коренным землянином.'
          rating = '9.29/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/3/29/bee3b3d88127abe89u88o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html") 

    if (message.text == "Ковбой Бибоп🤠"):
          name = 'Ковбой Бибоп'
          site_url='https://rezka.ag/series/fiction/43215-kovboy-bibop-2021.html'
          description = 'В недалеком будущем в результате крупной катастрофы Земля оказалась почти непригодна для жизни, что побудило человечество расселиться по всем планетам и небесным телам Солнечной системы. Воцарившиеся хаос и неразбериха привели к расцвету космической преступности, из-за чего возникла профессия охотников за головами, которые за награду отлавливают опасных нарушителей закона.'
          rating = '7.51/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/6/l54a7f3167337xg33j33h.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Пожиратель душ"):
          name = 'Пожиратель душ'
          site_url='https://rezka.ag/animation/fantasy/18964-pozhiratel-dush-2008.html'
          description = 'Как показывает практика, у большинства начинающих борцов со всевозможной нечистью порой возникают трудности даже с самыми безобидными монстрами, и лишь набив кучу шишек и синяков там, где они совсем не обязательны, такой страдалец в конце концов превращается в супергероя, если до этого знаменательного момента не отдаст богу душу.'
          rating = '9.44/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/9/2/o5d244ec12c07sv85e37p.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Гуррен-Лаганн"):
          name = 'Гуррен-Лаганн'
          site_url='https://rezka.ag/animation/drama/11055-gurren-lagann-2007.html'
          description = 'Действие фантастического аниме-сериала «Гуррен-Лаганн» происходит в мире, где люди вот уже на протяжении многих сотен лет влачат жалкое существование в подземных поселениях. А всему виной страх перед земными толчками и обвалами, которые в считанные секунды способны лишить человека жизни. Именно в одной из таких деревень, расположенных под землей, живут главные герои – мальчишка Симон вместе со своим духовным наставником в лице молодого парня по имени Камина.'
          rating = '9.53/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2019/2/12/ma4e434ffa36cux67g41l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Ван-Пис"):
          name = 'Ван-Пис'
          site_url='https://jut.su/oneepiece/episode-1.html'
          description = 'Легендарный Король Пиратов Гол Д. Роджер перед своей казнью произносит последние слова, в которых рассказывает, где спрятал награбленные за свои лихие годы сокровища. «Берите их, если сможете!», – с этим словами великий пират простился с жизнью, заставив этой фразой тысячи людей бросить свои дела и отправиться в далёкое плаванье на Гранд-Лайн, являющийся самым опасным местом на свете, в надежде обрести невероятное богатство.'
          rating = '9.11/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/4/4/f2b817e04c96ckh36p96s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Доктор Стоун: Новый мир⚗️"):
          name = 'Доктор Стоун: Новый мир'
          site_url='https://rezka.ag/animation/adventures/31319-doktor-stoun-tv-1-2019.html'
          description = 'События разворачиваются спустя почти четыре тысячелетия после того, как ослепительная вспышка света превратила всех людей на планете в каменные статуи. Одним из первых, кому удается избавиться от каменной оболочки, оказывается Сенку — гениальный парень, начинающий сразу разрабатывать грандиозный план спасения цивилизации. Спустя полгода к нему присоединяется старшеклассник Тайдзю, чья сила и доброта становятся недостающими винтиками, помогающими Сенку добиться значительного прогресса в осуществлении своего замысла...'
          rating = '9.21/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/wa3e7911ee525op50k25z.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")        


    if (message.text == "Клинок, рассекающий демонов👹🗡️"):
          name = 'Клинок, рассекающий демонов'
          site_url='https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html'
          description = 'После смерти отца юному Тандзиро пришлось взять на себя ответственность за содержание матери, братьев и сестер. Однажды он отправляется в город у подножия горы, где обычно торгует древесным углем, а затем остается там на ночь из-за пугающего предостережения местного жителя. Вернувшись домой, Тандзиро видит шокирующую картину — демоны-людоеды растерзали почти всю его семью, а оставшаяся в живых младшая сестренка превратилась в одну из этих тварей, однако не лишилась человеческих эмоций. Собрав волю в кулак, парень решает во что бы то ни стало исцелить сестру и отомстить демону, который разрушил его жизнь...'
          rating = '9.11/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/12/6/ve8c4c4bb1c02kr51p86h.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  



    if (message.text == "Токийские мстители🏍️"):
          name = 'Токийские мстители'
          site_url='https://rezka.ag/animation/adventures/38786-tokiyskie-mstiteli-tv-1-2021.html'
          description = 'Из новостей Ханагаки Такэмити узнает, что его подруга из средней школы, Татибана Хината, умерла. Единственная девушка, с которой он когда-либо встречался, была только что убита группировкой, известной как токийская банда Мандзи. Он живет в никудышной квартире с тонкими стенами, а его босс, на шесть лет младше Такэмити, обращается с ним как с идиотом. Да к тому же он девственник в свои двадцать шесть. Попав под поезд, Такэмити не лишается своей жалкой жизни, а непонятным образом переносится на двенадцать лет назад, в школьные годы. Чтобы спасти Хинату и изменить свою жизнь, заручившись поддержкой младшего брата Хинаты, Такэмити начинает свой путь к вершинам самой опасной группировки города.'
          rating = '9.01/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/12/28/z41834aa6f67eys40a60c.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Моя геройская академия🏫🦸‍♂️"):
          name = 'Моя геройская академия'
          site_url='https://rezka.ag/animation/comedy/15554-moya-geroyskaya-akademiya-tv-1-2016.html'
          description = 'В далеком будущем большая часть населения планеты обладает суперспособностями, известными как «причуды», а к людям, лишенным сверхчеловеческих навыков, относятся с презрением. В центре истории оказывается Изуку Мидория — ничем не примечательный школьник, не имеющий врожденных способностей, который мечтает стать супергероем, за что подвергается издевательствам. Однажды его судьба кардинально меняется, когда Изуку встречает могущественного супергероя, который впоследствии дает скованному пареньку шанс стать его преемником…'
          rating = '9.04/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/r272d68d69099ij78p56o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Атака титанов🤺"):
          name = 'Атака титанов'
          site_url='https://rezka.ag/animation/adventures/1973-ataka-titanov-tv-1-2013.html'
          description = 'Фэнтезийный аниме-сериал «Вторжение титанов» снят по мотивам одноименной манги Хадзимэ Исаямы.На протяжении долгих лет человечество вело борьбу с Гигантами – огромными существами, обладающими невероятной силой и довольно слабым интеллектом. Гиганты поедали людей тысячами, и получали от этого несказанное удовольствие. И вот однажды выжившим удается создать вокруг своего поселения стену, которую преодолеть было не под силу даже кровожадным Гигантам.'
          rating = '9.32/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/1/22/t3bbb34a29ccfxi97e15x.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Наруто🍜"):
          name = 'Наруто'
          site_url='https://rezka.ag/animation/fighting/12333-naruto-tv-1-2002.html#t:14-s:1-e:136'
          description = 'Давным-давно, когда на поселение напал жестокий демон, могущественный Девятихвостый Лис, глава деревни в неравном поединке ценой собственной жизни запечатывает монстра в теле своего ребёнка. Оставшись полной сиротой, малыш рос изгоем, презираемый людьми, боящимися, что в один прекрасный момент демон проснётся, и всё повторится вновь. Не имея друзей и хоть какой-нибудь поддержи за спиной, живший в постоянной ненависти со стороны односельчан, считающих его монстром во плоти, парень не сломался и вырос добродушным и очень наивным пареньком, потому что в нужный момент, после его поступления в академию ниндзя, рядом с ним появились верящие в него люди, всегда готовые подать руку помощи.'
          rating = '9.18/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/9/27/tdbdde7ea100dnw10x79n.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  

    if (message.text == "Блич🗡️"):
          name = 'Блич'
          site_url='https://rezka.ag/animation/comedy/2129-blich-tv-1-2004.html'
          description = 'Фэнтезийный аниме-сериал «Блич» является экранизацией одноименной манги Тайто Кубо, рассказывающей о пятнадцатилетнем школьнике, который случайным образом становится обладателем сверхъестественных сил богов смерти.Действие разворачивается в наши дни в Японии, где живет главный герой Ичиго Куросаки, с детства обладающий удивительной способностью видеть духов и призраков. Однажды в его комнате появляется девушка по имени Рукия Кучики, являющаяся так называемым «проводником душ». '
          rating = '9.24/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/9/29/r63cd6d7c0a3fup31x14s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Мобильный воин Гандам📱"):
          name = 'Мобильный воин Гандам'
          site_url='https://rezka.ag/animation/fiction/55636-mobilnyy-voin-gandam-vedma-s-merkuriya-tv-1-2022.htmll'
          description = 'Действие развивается в далеком будущем, когда человечество достигло значительного технологического прогресса и построило гигантскую экономическую систему в космосе. Сулетта — одинокая девушка с далекой планеты Меркурий, которая приняла решение перейти в известную технологическую школу, управляемую гигантской корпорацией.'
          rating = '8.83/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/3/5/saebc2873b44fbq74b45g.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  

    if (message.text == "Семь смертных грехов"):
          name = 'Семь смертных грехов'
          site_url='https://rezka.ag/animation/fantasy/18867-sem-smertnyh-grehov-tv-1-2014.html'
          description = 'Когда-то спокойствие могучего королевства Лионесс оберегала семерка непобедимых воинов, известных как «Семь Смертных Грехов». Но около десяти лет назад их обвинили в сговоре с целью свергнуть монарха, в результате чего в столице королевства началось нешуточное сражение, которое вскоре переросло в кровавую бойню. В тот день свою смерть увидели сотни Святых Рыцарей, защищавших короля, а «Семь Смертных Грехов» бесследно исчезли, после чего их до cих пор никто не видел.'
          rating = '9.21/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/wc4d645b373f5np93z32j.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


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
        await message.answer(f'1:{anime_2[1]}\n2:{anime_2[2]}\n3:{anime_2[3]}\n4:{anime_2[4]}\n5:{anime_2[5]}\n6:{anime_2[6]}\n7:{anime_2[7]}\n8:{anime_2[8]}\n9:{anime_2[9]}\n10:{anime_2[10]}')#      kb_2 = [
        kb_2 = [    
                [types.KeyboardButton("Ван-Пис")],
                [types.KeyboardButton("Доктор Стоун: Новый мир⚗️")],
                [types.KeyboardButton("Клинок, рассекающий демонов👹🗡️")],
                [types.KeyboardButton("Токийские мстители🏍️")],
                [types.KeyboardButton("Моя геройская академия🏫🦸‍♂️")],
                [types.KeyboardButton("Атака титанов🤺")],
                [types.KeyboardButton("Наруто🍜")],
                [types.KeyboardButton("Блич🗡️")],
                [types.KeyboardButton("Мобильный воин Гандам📱")],
                [types.KeyboardButton("Семь смертных грехов")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_2 = types.ReplyKeyboardMarkup(keyboard=kb_2 , resize_keyboard=True)
        await message.answer('Вот список, выбирай',reply_markup=keyboard_2)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)
                 
    
#########################################################################################################################################
    if (message.text == "Вечная воля"):
          name = 'Вечная воля'
          site_url='https://rezka.ag/animation/adventures/41759-vechnaya-volya-2020.html'
          description = 'В центре истории находится Бай Сяочунь — самоуверенный и добродушный, но надоедающий парень, которым движет страх смерти и сильнейшее желание обрести вечную жизнь. Умный, эксцентричный и хитрый Бай выглядит наивным простачком, однако для достижения собственной цели он готов совершать бессовестные и порой мерзкие поступки, а также не отступать перед трудностями. Постоянно попадая в различные переделки, Бай постепенно начинает приближаться к осуществлению заветной мечты, когда ему удается стать членом секты бессмертных…'
          rating = '8.87/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/1/3/j51bfcd70a847qy41m67s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html") 

    if (message.text == "Dragon Ball🐲"):
          name = 'Dragon Ball'
          site_url='https://rezka.ag/animation/fantasy/22712-drakoniy-zhemchug-super-2015.html'
          description = 'Жизнь героев никогда не отклоняется в сторону тихого и мирного существования, и Гоку уверен, что даже после победы над злейшим врагом не стоит расслабляться. Согласно сюжету аниме-сериала, продолжающего повествование о похождениях легендарного воителя, после поражения Маджина Буу прошло уже несколько месяцев, и люди постепенно возвращаются к привычному быту. Даже Чи-Чи делает все возможное, чтобы заставить своего приятеля оставить тренировки и забыть о сражениях, ведь впереди, по заверениям остальных, их ждет лишь безоблачное будущее без войн и трагедий.'
          rating = '9.31/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/11/22/d325e84303895id37h25s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Сумо Хиномару🥋"):
          name = 'Сумо Хиномару'
          site_url='https://jut.su/hinomaruzumou/'
          description = 'Один из самых мужественных видов спорта, который числится среди вечных символов Японии - сумо. Если раньше массивных бойцов изображали на традиционных гравюрах, то теперь нарисованные сумоисты сражаются в движении. По закону спортивного жанра главный герой Ушио Хиномару не имеет определённого таланта к сумо - вы не подумайте, он вполне хорошо сложен, вот только до габаритов типичных сумоистов явно не дотягивает; зато решительный настрой стремиться вверх и побеждать всегда при нём.'
          rating = '9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/17/x071c66d8cbbawt17g96o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  


    if (message.text == "Боец Баки🥊"):
          name = 'Боец Баки'
          site_url='https://rezka.ag/animation/fighting/20495-boec-baki-tv-1-2001.html'
          description = 'Анимационный сериал от режиссера Джереми Инмана. Аниме рассказывает о судьбе и жизни молодого человека Ханме Баки. Его отец самый сильный воин на Земле. Баки растет в мире постоянных боев и мечтает когда-нибудь стать лучшим, чтобы затмить своего деспотичного отца. Но мир воинов таит в себе множество опасностей. Каждый борец знает, что на любую силу, может прийти и другая сила, более мощная.'
          rating = '9.07 /10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/c3c3ee3f59d1cdg26z96y.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html") 

    if (message.text == "Кэнган Асура"):
          name = 'Кэнган Асура'
          site_url='https://rezka.ag/animation/adventures/31513-asura-kengana-2019.html'
          description = 'Во времена правления клана Токугавы состоятельные торговцы, желая урегулировать разногласия друг с другом, нанимали опытных бойцов, чтобы те представляли их интересы на гладиаторской арене, участвуя в жестоких рукопашных поединках. В современной Японии такие состязания являются очень прибыльным бизнесом для различных корпораций, которые готовы пойти на все ради победы. Токита Ома по прозвищу Асура – безжалостный боец, известный способностью с легкостью одолевать даже самых свирепых противников. Однажды Асура соглашается сражаться от имени главы крупной компании с соперником, который не представляется ему серьезным...'
          rating = '8.79 /10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/12/15/h8d7ef0e740a6os18x57s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html") 

    if (message.text == "Отчёт о буйстве духов"):
          name = 'Отчёт о буйстве духов'
          site_url='https://rezka.ag/animation/comedy/20558-otchet-o-buystve-duhov.html'
          description = 'Юсукэ Урамэси худший ученик в школе. Мальчишка воюет со всем миром, ссорится с преподавателями, не находит взаимопонимания с мамой, дерется со сверстниками, к счастью, благодаря умению метко работать кулаками, как правило, выходит победителем в уличных драках. А еще он не делает домашние задания и постоянно прогуливает уроки.В один из дней, когда Юсукэ шатался без дела по улицам, он бросился спасать из-под колес грузовика, маленького мальчика, а сам погиб, сбитый автомобилем.'
          rating = '9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/13/v8c804e79370age85o28o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")     

    if (message.text == "Эпоха смут"):
          name = 'Эпоха смут'
          site_url='https://jut.su/sengoku-basara/'
          description = 'В человеческой природе стремление к собственной мечте, но что делать, когда достижение поставленной задачи невозможно без страданий окружающих? Вот и приходится людям воевать друг с другом, навязывая остальным собственные идеалы, распространяя могущество и стараясь внести имя в историю. Подобные события происходят и в выдуманном мире, представленном в аниме «Эпоха смут: Последняя вечеринка», раздираемым нескончаемыми баталиями нескольких провинций.'
          rating = '8/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/8/8/na47f7087d4ecdw73t32o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Виртуальный боец"):
          name = 'Виртуальный боец'
          site_url='https://rezka.ag/animation/adventures/49694-virtualnyy-boec-1995.html'
          description = 'Акира Юки провел долгие годы, оттачивая навыки боевого искусства бацзицюань под руководством родного дедушки. Сейчас он жаждет увидеть созвездие восьми небесных звезд, которые открываются только тем, кто обладает настоящей силой. Это жгучее стремление побуждает Акиру отправиться в опасное путешествие, чтобы узнать подробности о звездах. Тем временем гнусный коварный ученый Ева Дюрикс планирует создать идеального солдата, и с этой целью она похищает Сару Брайант, подругу Акиры. Чтобы спасти Сару из плена, Акира должен на практике применить навыки владения боевыми искусствами…'
          rating = '8.33/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/6/23/v8b43014dbddamz87p34d.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Царь горы⛰️"):
          name = 'Царь горы'
          site_url='https://rezka.ag/animation/adventures/35728-bog-starshey-shkoly-2020.html'
          description = 'Когда-то давно милостивые Боги даровали людям силу, чтобы те могли противостоять злобным демонам, после победы над которыми человечество заслужило право оставить этот дар себе с условием не направлять его против божеств. Однажды загадочная корейская организация объявляет конкурс боевых искусств среди школьников под названием «Бог старшей школы», чтобы определить трех победителей для последующего мирового турнира. Одним из главных претендентов на первенство становится 17-летний Чин Мо-ри из Сеула, использующий собственную технику тхэквондо...'
          rating = '8.85/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/d2f2bacfb87b9vi36x89n.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Ящик предложений Мэдаки📦"):
          name = 'Ящик предложений Мэдаки'
          site_url='https://yummyanime.org/1901-jaschik-predlozhenij-mjedaki.html'
          description = 'Сюжет анимационного сериала развивается в пределах частной академии Хаконива. Здесь происходит нечто невероятное, ведь президентом школьного совета с большим перевесом голосов выбирают Медаку Куроками. Что в этом необычного? А то, что девушке всего шестнадцать лет и в эту школу она перевелась совсем недавно.Получив желанный титул, Медака устанавливает ящик предложений, куда каждый желающий может закинуть записку с пожеланиями относительно учебного процесса и жизни академии. Новый президент обещает выполнить все требования учащихся, даже если ей придется работать круглосуточно.'
          rating = '8.6/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://yummyanime.org/uploads/posts/2022-01/11761.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if(message.text == "Боевые искуства"):
        await message.answer("Окей сейчас найдем тебе что-то")
        anime_3 = {
           1:'Вечная воля',
           2:'Dragon Ball🐲',
           3:'Сумо Хиномару🥋',
           4:'Боец Баки🥊',
           5:'Кэнган Асура',
           6:'Отчёт о буйстве духов',
           7:'Эпоха смут',
           8:'Виртуальный боец',
           9:'Царь горы⛰️',
           10:'Ящик предложений Мэдаки📦'
        }
        await message.answer(f'1:{anime_3[1]}\n2:{anime_3[2]}\n3:{anime_3[3]}\n4:{anime_3[4]}\n5:{anime_3[5]}\n6:{anime_3[6]}\n7:{anime_3[7]}\n8:{anime_3[8]}\n9:{anime_3[9]}\n10:{anime_3[10]}')
        kb_3 = [    
                [types.KeyboardButton("Вечная воля")],
                [types.KeyboardButton("Dragon Ball🐲")],
                [types.KeyboardButton("Сумо Хиномару🥋")],
                [types.KeyboardButton("Боец Баки🥊")],
                [types.KeyboardButton("Кэнган Асура")],
                [types.KeyboardButton("Отчёт о буйстве духов")],
                [types.KeyboardButton("Эпоха смут")],
                [types.KeyboardButton("Виртуальный боец")],
                [types.KeyboardButton("Царь горы⛰️")],
                [types.KeyboardButton("Ящик предложений Мэдаки📦")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_3 = types.ReplyKeyboardMarkup(keyboard=kb_3 , resize_keyboard=True)
        await message.answer('Вот список выбирай',reply_markup=keyboard_3)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)        

        
############################################################################################################################################        
    if (message.text == "Код Гиас"):
          name = 'Код Гиас'
          site_url='https://rezka.ag/animation/drama/12016-kod-gias-vosstavshiy-lelush-2006.html'
          description = 'Сильнейшая в мире держава Священная Британская Империя, благодаря своей невероятной военной мощи захватившая около трети мира, объявляет войну Японии из-за продолжительного дипломатического конфликта. Впервые применив для наземных сражений передовую военную технологию – боевых человекообразных роботов Найтмер Фрейм, – британцы с лёгкостью сокрушила японскую армию, не сумевшую противостоять столь мощному оружию. В ходе скоротечного противостояния Япония была разгромлена и, утратив независимость, переименована в «Зону 11».'
          rating = '9.29/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/3/3/t64a520884b6dbw94c70v.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  

    if (message.text == "Последний Серафим"):
          name = 'Последний Серафим'
          site_url='https://rezka.ag/animation/adventures/22518-posledniy-serafim-2015.html'
          description = 'Действие разворачивается во времена, когда мир поражает искусственно выведенный вирус, убивающий всех без разбору людей, которым уже исполнилось больше тринадцати лет. Постепенно всё взрослое население планеты было истреблено. В то же время в мир приходят вампиры, сидевшие до сего времени в темноте преисподней и, воспользовавшись ситуацией, прибирают всё к своим рукам, а уцелевших сгоняют в приюты, расположенные под землёй. Дети для нетопырей становятся неиссякаемым источником свежей крови, которую ребята вынуждены сдавать регулярно в принудительном порядке.'
          rating = '9.35/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/11/16/wbc0330635330qp31w28m.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")    
    
    if (message.text == "Военная хроника маленькой девочки"):
          name = 'Военная хроника маленькой девочки'
          site_url='https://rezka.ag/animation/adventures/24422-voennaya-hronika-malenkoy-devochki-2017.html'
          description = 'Аниме-сериал поведает увлекательную историю о реинкарнации, в которую многие, в том числе и главный герой, не верят. Однако, как оказалось, после смерти жизнь существует…В центре запутанных и бурно развивающихся событий оказывается самый заурядный японский мужчина. Он жил себе обычной жизнью, преуспел в работе, добившись должности топ-менеджера серьезной фирмы. Будучи до мозга костей прагматиком и скептиком, он всегда сомневался в концепции бессмертия души и перерождении. Однажды бедолага попадает под сокращение, лишается работы и, не зная, как дальше быть, решает наложить на себя руки.'
          rating = '9.01/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2017/4/10/u5b897bb37c13qu67o99x.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")
    if (message.text == "Врата: там бьются наши воины"):
          name = 'Врата: там бьются наши воины'
          site_url='https://jut.su/gate/'
          description = 'Человечество множество раз переживало различные проблемы, но в этот раз произошло нечто невероятное, а именно открытие врат в параллельный мир. Правительство собрало всю военную мощь, чтобы преградить путь обитателям неизведанного измерения. Вскоре солдаты увидели мистических чудовищ, воинственных рыцарей, а также могущественных колдунов, которые собрались на них напасть. Первую атаку военным отбить удалось, но закрыть врата они не смогли. Правительство решило собрать лучших воинов и отправить по ту сторону врат, чтобы разведать обстановку.'
          rating = '9.11/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://animego.org/media/cache/thumbs_250x350/upload/anime/images/5a8d64491d3bf003815986.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")  

    if (message.text == "Восемьдесят шесть"):
          name = 'Восемьдесят шесть'
          site_url='https://rezka.ag/animation/adventures/38779-vosemdesyat-shest-tv-1-2021.html'
          description = 'Республика Сан-Магнолия. Долгое время эта страна подвергалась нападениям своего соседа, Империи, которая создала серию беспилотных военных машин под названием «Легион». В ответ на угрозу Республика успешно завершает разработку аналогичных военных технологий и отражает атаку врага, сумев обойтись без жертв.'
          rating = '8.99/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/4/11/qe5a916d2da77cj86a93h.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Берсерк😏"):
          name = 'Берсерк'
          site_url='https://rezka.ag/animation/adventures/10917-berserk-tv-1-1997.html'
          description = 'Приключенческий аниме сериал «Берсерк» снят по мотивам одноименной манги известного японского автора Кэнтаро Миура, которая по праву считается одним из лучших комиксов всех времен.Действие происходит в вымышленном мире, напоминающем Европу XIV—XV веков. В центре сюжета молодой воин-наемник Гатс. Он очень хорошо владеет боевыми искусствами, а также виртуозно управляется со своим огромным мечом. Однажды он присоединяется к отряду Ястребов, который возглавляет крайне амбициозный человек по имени Гриффит.'
          rating = '9.47/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2015/9/23/pffd98090189ecy43v83z.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")



    if (message.text == "Стальная тревога🔈"):
          name = 'Стальная тревога'
          site_url='https://rezka.ag/animation/mecha/20675-stalnaya-trevoga-2002.html'
          description = 'Однажды Сосукэ Сагара, отважный солдат, служащий в секретной антитеррористической организации «Мифрил», получил важное задание: он должен стать телохранителем 16-летней привлекательной школьницы Канамэ Тидори. Чтобы успешно выполнить ответственное поручение, герою предстоит оказаться в эпицентре смертоносных приключений, а также пройти через различные испытания.'
          rating = '9.55/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/d44a519d31650hp20w66s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Призрак в доспехах: Синдром одиночки🛡️"):
          name = 'Призрак в доспехах: Синдром одиночки'
          site_url='https://rezka.ag/animation/action/33943-prizrak-v-dospehah-sindrom-odinochki-2045-2020.html'
          description = 'События разворачиваются в 2045 году, после того как мировой экономический кризис привел к глобальному дефолту: деньги обесценились, валютные рынки рухнули, а страны «большой четверки» оказались в состоянии перманентного противостояния, именуемого «Устойчивой войной». В этом разоренном мире бывшие члены 9-го отряда общественной безопасности Японии, возглавляемые майором Мотоко, присоединились к «Призракам» — группе наемников, использующих современные разработки в кибернетике, чтобы заработать на жизнь.'
          rating = '6.03/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/4/20/p7f3a23f27707qo13m62i.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Вальврейв Освободитель"):
          name = 'Вальврейв Освободитель'
          site_url='https://rezka.ag/animation/fiction/2044-valvreyv-osvoboditel.html'
          description = 'Действие приключенческого аниме «Вальврейв-освободитель» разворачивается в далеком будущем, где большая часть человечества живет в космических городах-колониях. Власть в этом мире разделена между двумя сверхдержавами - Доруссийской Федерацией Военного Соглашения (ДФВС) и Соединёнными Штатами Атлантического Кольца (СШАК). На протяжении долгих лет между ними ведется противостояние, которое угрожает благополучию и спокойствию всего человечества.Но есть страны, которые стараются придерживаться нейтралитета, и делают все возможное, чтобы не оказаться втянутыми в конфликт этих двух государств.'
          rating = '9.2/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/9/10/h706858e9694dee66x68u.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Королевство🏰"):
          name = 'Королевство'
          site_url='https://rezka.ag/animation/adventures/43269-korolevstvo-tv-2-2013.html'
          description = 'Принц Ин Чжэн одолел заговорщиков и вернул себе трон царства Цинь, но почивать на лаврах преждевременно. У молодого правителя слишком мало верных сторонников, ведь многие погибли в бою, а большинство князей и сановников выжидают, желая знать, на что способен «этот юноша». Реальную власть в стране захватил бывший купец, авантюрист Люй Бувэй, интригами и подкупом пробившийся на пост регента и канцлера. На словах он лоялен Ин Чжэну, а на деле пытается сойтись с его матерью и собирает команду таких же талантливых и беспринципных людей, чтобы устранить принца и самому стать царем.'
          rating = '8.9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/17/f24b7c4aa070dxi45x45k.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if(message.text == "Военные"):
        await message.answer("Окей сейчас найдем тебе что-то")           
        anime_4 = {
           1:'Код Гиас',
           2:'Последний Серафим',
           3:'Военная хроника маленькой девочки',
           4:'Врата: там бьются наши воины',
           5:'Восемьдесят шесть',
           6:'Берсерк😏',
           7:'Стальная тревога🔈',
           8:'Призрак в доспехах: Синдром одиночки',
           9:'Вальврейв Освободитель',
           10:'Королевство🏰'
        }
        await message.answer(f'1:{anime_4[1]}\n2:{anime_4[2]}\n3:{anime_4[3]}\n4:{anime_4[4]}\n5:{anime_4[5]}\n6:{anime_4[6]}\n7:{anime_4[7]}\n8:{anime_4[8]}\n9:{anime_4[9]}\n10:{anime_4[10]}')
        kb_4 = [    
                [types.KeyboardButton("Код Гиас")],
                [types.KeyboardButton("Последний Серафим")],
                [types.KeyboardButton("Военная хроника маленькой девочки")],
                [types.KeyboardButton("Врата: там бьются наши воины")],
                [types.KeyboardButton("Восемьдесят шесть")],
                [types.KeyboardButton("Берсерк😏")],
                [types.KeyboardButton("Стальная тревога🔈")],
                [types.KeyboardButton("Призрак в доспехах: Синдром одиночки🛡️")],
                [types.KeyboardButton("Вальврейв Освободитель")],
                [types.KeyboardButton("Королевство🏰")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_4 = types.ReplyKeyboardMarkup(keyboard=kb_4 , resize_keyboard=True)
        await message.answer('Вот список, выбирай',reply_markup=keyboard_4)


#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)
#####################################################################################################################################################        
    if (message.text == "Пять невест👰"):
          name = 'Пять невест'
          site_url='https://rezka.ag/animation/comedy/30810-pyat-nevest-tv-1-2019.html'
          description = 'Старшеклассник Футаро Уэсуги отчаянно нуждается в деньгах, которые смогут улучшить тяжелое финансовое положение его семьи. Будучи отличником, он устраивается высокооплачиваемым репетитором для пяти новеньких одноклассниц, являющихся сестрами-близнецами. Несмотря на схожую внешность, девушки обладают совершенно непохожими друг на друга характерами, которые объединяет лишь одна черта – абсолютное нежелание учиться. Футаро придется приложить максимум усилий, чтобы завоевать доверие сестер и помочь им не вылететь из школы...'
          rating = '9.35/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/1/4/z4b162c2d2449lg34m99a.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Рандеву с жизнью"):
          name = 'Рандеву с жизнью'
          site_url='https://rezka.ag/animation/adventures/21859-randevu-s-zhiznyu-tv-1-2013.html'
          description = 'В сердце самого большого на планете материка Евразия произошло необъяснимое явление, которое впоследствии назвали Пространственным разломом. Стихийное бедствие повлекло множественные разрушения и гибель более 100 миллионов человек.Сидо Ицука – сирота. Вдвоем с сестренкой они живут в предместье Токио. Юноша случайно оказался в эпицентре одного из малых пространственных разломов, в последнее время они все чаще стали возникать на территории Японии, и узнал, что на Землю надвигаются Духи, в их планах захват планеты. В поисках сестры, Сидо встретил миловидную девушку, облаченную в доспехи.'
          rating = '9.33/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/4/9/cb5e71d1e7c34cw48t76i.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Хроники непобеждённого Бахамута"):
          name = 'Хроники непобеждённого Бахамута'
          site_url='https://rezka.ag/animation/mecha/12498-hroniki-nepobedimogo-bahamuta-2016.html'
          description = 'События разворачиваются вокруг приключений Люкса. Будучи экс-принцем Аркадии, чью династию безжалостно свергли с престола несколько лет назад, он оказывается посреди очередных неприятностей, когда случайно попадает в женскую купальню, где как раз принимает водные процедуры принцесса Лизешарт. Застигнутая врасплох обнаженной, принцесса разгневана, поэтому она вызывает нарушителя спокойствия на дуэль на специальном древнем оружии, именуемом Драг-Райдом. Некоторое время назад Люкс был одним из сильнейших рыцарей, способным победить любого противника на Драг-Райде, однако теперь его навыки значительно ухудшились…'
          rating = '9.07/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/3/21/b313dac6f7fafwj96a89b.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Мифический дух: Хроники"):
          name = 'Мифический дух: Хроники'
          site_url='https://rezka.ag/animation/adventures/40739-duhovnye-hroniki-2021.html'
          description = 'Юный Амакава Харуто умер несколько лет назад, не успев воссоединиться с без вести пропавшим другом детства. Мальчишка по имени Рио, живущий в трущобах, отчаянно желает отомстить убийце его матери. Однажды воспоминания и личностные качества Харуто реинкарнируются в Рио, который оказывается совершенно сбитым с толку присутствием Амакавы в его сознании. Оказавшись в параллельном мире, известном как Королевство Бертрам, мальчик пробуждает таинственную силу, а затем спасает принцессу от похитителей. Получив в качестве награды стипендию в Королевской академии, бедный сирота оказывается в крайне отвратительной школе для богатых и успешных детей загадочного мира.'
          rating = '8.82/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/7/14/gcdd08b8a5739hc61u25s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Фермерская жизнь в ином мире👨‍🌾"):
          name = 'Фермерская жизнь в ином мире'
          site_url='https://rezka.ag/animation/adventures/55305-fermerskaya-zhizn-v-inom-mire-2023.html'
          description = 'Умерев от болезни в возрасте 39 лет, Мачио Хираку получает возможность отправиться в другой мир. Когда Бог спрашивает у героя, что он хотел бы получить в новом мире, Мачио просит первое желание — иметь здоровое тело, второе желание — мирную жизнь, третье желание — знать местный язык и последнее желание — быть фермером.'
          rating = '8.75/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/2/19/n5ce775d6d234sv55n60y.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Связанные небом"):
          name = 'Связанные небом'
          site_url='https://rezka.ag/animation/romance/21880-svyazannye-nebom-odinochestvo-na-dvoih.html'
          description = 'Мелодраматичный аниме-сериал Такео Такахаси «Связанные Небом» поведает историю близнецов Касугано, потерявших своих мать с отцом в автомобильной катастрофе. Ближайших родственников поблизости не оказалось на момент трагедии и поэтому шестнадцатилетний парнишка по имени Харука, на правах настоящего мужчины, берёт на себя все обязательства за осиротевшую семью — себя и сестрёнку Сору. В тяжёлых недетских и жизненно важных заботах парнишка укрепился, повзрослел и сумел преодолеть постигшее их горе, только его не покидало чувство беспокойства за сестричку, с детства весьма слабенькую и болезненную, ставшую из-за этого нелюдимкой.'
          rating = '8.46/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/11/6/c216a5aa09c2avy77o87p.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Король магических стрел и Ванадис👑🏹"):
          name = 'Король магических стрел и Ванадис'
          site_url='https://rezka.ag/animation/adventures/2279-vladyka-volshebnyh-strel-i-vanadis-2014.html'
          description = 'Королевство Штед находится в мире, которое схоже с Европой средних веков. В самом королевстве идут нескончаемые войны. Иначе и быть не может, поскольку королю служат верой и правдой семь женщин, именуемых Ванадис. Эти воинственные девушки владеют магическим оружием. Им подчиняется целая гвардия солдат. Однако есть и такие, кто не верит в военные таланты молодых воинственных особ. К примеру, солдаты из армии Брюн – другого королевства.'
          rating = '9.06/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/11/8/y398675d42824sw87h98e.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Маг-целитель: Новый старт"):
          name = 'Маг-целитель: Новый старт'
          site_url='https://rezka.ag/animation/adventures/36983-mag-celitel-novyy-start-2021.html'
          description = 'В центре сюжета оказывается Кэяру — маг-целитель, живущий в мире, где уникальные способности специализирующихся на исцелении волшебников эксплуатируются для достижения чужих целей. Однажды главному герою удается узнать, что маги-целители — сильнейшие среди волшебников, а истинный потенциал исцеляющей магии невероятно велик. С помощью философского камня Кэяру получает уникальную возможность вернуться в прошлое, чтобы не только радикально изменить собственное будущее, но и, используя знания из будущего, отомстить своим обидчикам...'
          rating = '8.24/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/1/16/s2028d326ec6dwy10a23s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Тотальный гарем"):
          name = 'Тотальный гарем'
          site_url='https://rezka.ag/animation/fiction/45575-totalnyy-garem-2021.html'
          description = 'Несколько лет назад смертельный вирус практически полностью уничтожил мужское население планеты. Мужчины, которым чудом удалось выжить, были погружены на длительное время в криогенный сон, замедляющий убийственное действие вируса. После пяти лет, проведенных в глубоком сне, молодой Рэйто Мидзухара приходит в себя и обнаруживает мир, в котором он является ценнейшим ресурсом. На его плечи возложена ответственная миссия: он должен заниматься оплодотворением женщин, чтобы восстановить популяцию планеты. Вот только Рэйто не интересуют спонтанные связи с незнакомыми женщинами, ведь он мечтает о встрече со своей возлюбленной — Эрисой Татибаной…'
          rating = '7.69/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/3/18/q4adaebbf36a8hl24c57m.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")          

    if (message.text == "Старшая школа DxD"):
          name = 'Старшая школа DxD'
          site_url='https://rezka.ag/animation/adventures/22117-vysshaya-shkola-dxd-tv-1-2012.html'
          description = 'Приключенческий аниме-сериал Тецуя Янагисавы «Старшая Школа: Демоны против Падших» поведает историю семнадцатилетнего старшеклассника Иссэя Хёдо, прекрасно знающего ответ на вопрос, что хочет от жизни подросток. Именно для этого он и перевёлся в бывшую женской высшую школу Комао. Юноша по простоте душевной полагал, будто начав совместное обучение в заведении, где имеется недостаток мужского пола, он поистине сделается королём девичьих сердец. Только на деле идёт уже второй год обучения в данном заведении, а девицы по-прежнему преследуют только нескольких красавцев'
          rating = '9.34/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/16/dc2db1a9dab85jf91f56l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")



    if(message.text == "Гарем"):
        await message.answer("Окей сейчас найдем тебе что-то")            
        anime_5 = {
           1:'Пять невест👰',
           2:'Рандеву с жизнью',
           3:'Хроники непобеждённого Бахамута',
           4:'Мифический дух: Хроники',
           5:'Фермерская жизнь в ином мире👨‍🌾',
           6:'Связанные небом',
           7:'Король магических стрел и Ванадис👑🏹',
           8:'Маг-целитель: Новый старт',
           9:'Тотальный гарем',
           10:'Старшая школа DxD'
        }
        await message.answer(f'1:{anime_5[1]}\n2:{anime_5[2]}\n3:{anime_5[3]}\n4:{anime_5[4]}\n5:{anime_5[5]}\n6:{anime_5[6]}\n7:{anime_5[7]}\n8:{anime_5[8]}\n9:{anime_5[9]}\n10:{anime_5[10]}')
        kb_5 = [    
                [types.KeyboardButton("Пять невест👰")],
                [types.KeyboardButton("Рандеву с жизнью")],
                [types.KeyboardButton("Хроники непобеждённого Бахамута")],
                [types.KeyboardButton("Мифический дух: Хроники")],
                [types.KeyboardButton("Фермерская жизнь в ином мире👨‍🌾")],
                [types.KeyboardButton("Связанные небом")],
                [types.KeyboardButton("Король магических стрел и Ванадис👑🏹")],
                [types.KeyboardButton("Маг-целитель: Новый старт")],
                [types.KeyboardButton("Тотальный гарем")],
                [types.KeyboardButton("Старшая школа DxD")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_5 = types.ReplyKeyboardMarkup(keyboard=kb_5 , resize_keyboard=True)
        await message.answer('Вот список ,выбирай',reply_markup=keyboard_5)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)





#########################################################################################################################################################        
    if (message.text == "Синий экзорцист"):
          name = 'Синий экзорцист'
          site_url='https://rezka.ag/animation/adventures/20735-siniy-ekzorcist.html'
          description = 'Зрелищный, наполненный мистикой аниме-сериал о вечной войне между людьми и демонами. У Рина и Юкио нет родителей, мальчишки выросли в храме, их духовным наставником все эти годы был Фудзимото, считавший главной задачей своей жизни экзорцизм – изгнание дьявола.Как часто бывает в семьях, братья абсолютно разные. Рин – вспыльчивый непоседа и драчун, вечно ввязывающийся во всевозможные разборки. Юкио – умный и отвественный, мечтает стать доктором и лечит ссадины братишки, полученные в драках.'
          rating = '9.39/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/15/z636b4c1c51d4op49f18j.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Повелитель тьмы на подработке!"):
          name = 'Повелитель тьмы на подработке!'
          site_url='https://rezka.ag/animation/comedy/20775-povelitel-tmy-na-podrabotke-tv-1-2013.html'
          description = 'Довольно интересный юмористический анимационный сериал, действие которого развивается в двух мирах. В мире Энте Ислы Князь тьмы терроризирует человечество, заставляя страдать все население этого параллельного мира. Но любому терпению приходит конец, и люди восстают против диктатуры. После длительных сражений Князь Тьмы и его демоны потерпели поражение. Эмилия вместе со своей армией ворвалась в замок Сатаны, но он, спасаясь бегством, открыл портал и со своим генералом прыгнул в него. Однако открывая порталы, нужно думать, куда ты попадешь, чего не сделал измотанный Властелин Тьмы.'
          rating = '9.37/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/7/15/w76360553568cdl32w36g.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Дороро"):
          name = 'Дороро'
          site_url='https://rezka.ag/animation/drama/30053-dororo-2019.html'
          description = 'Дайго Кагемицу заключает сделку с сорока восемью демонами: они даруют ему неограниченную власть, а взамен возьмут по частичке тела его будущего сына. Когда ребенок рождается с ужасными физическими дефектами, Дайго приказывает избавиться от него, однако младенца спасает добрый лекарь и заменяет недостающие части его тела протезами.Спустя шестнадцать лет юноша, называющий себя Хяккимару, занимается охотой на демонов, желая вернуть то, что отобрали у него при рождении. Однажды он встречает маленького воришку Дороро, и тот присоединяется к нему в этом нелегком путешествии.'
          rating = '9.41/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/14/je3a5d9a0c1cbdj27i69j.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")



    if (message.text == "Магическая битва"):
          name = 'Магическая битва'
          site_url='https://rezka.ag/animation/adventures/35876-magicheskaya-bitva-2020.html'
          description = 'Несмотря на врожденный спортивный талант, старшеклассник Юдзи Итадори всячески отказывается принимать участие в соревнованиях, а однажды решает присоединиться к клубу оккультных исследований. Обнаружив, что члены клуба — настоящие колдуны, способные манипулировать энергией живых существ, школьник сталкивается с Мегуни Фусигуро, который открывает страшную тайну о том, что Юдзи недавно контактировал с проклятым артефактом в виде гниющего пальца Сукуны. Это открытие навлекает на Итадори серьезные неприятности, поскольку Идзи вынужден стать хозяином Сукуны, а руководство Токийского колледжа магии приговаривает его к смертной казни...'
          rating = '9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/9/21/kc59948339c7dch99i15s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "О моём перерождении в слизь"):
          name = 'О моём перерождении в слизь'
          site_url='https://rezka.ag/animation/adventures/29454-o-moem-pererozhdenii-v-sliz-tv-1-2018.html'
          description = 'Сатору Миками – тридцатисемилетний офисный сотрудник, недовольный своей работой и уставший от скучной и обыденной жизни. Но однажды все меняется, когда по дороге домой на мужчину нападает неизвестный злоумышленник и смертельно ранит его. После смерти Сатору просыпается в удивительном мире, наполненном магией и различными волшебными существами, а также обнаруживает, что переродился в маленького слизистого монстра. Поначалу он разочаровывается в своем новом обличье, но вскоре узнает, что даже слизь способна стать героем…'
          rating = '9.38/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/8/10/kd201fbbbe538by63a90a.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Тёмный дворецкий"):
          name = 'Тёмный дворецкий'
          site_url='https://rezka.ag/animation/comedy/13213-temnyy-dvoreckiy-tv-1-2008.html'
          description = 'События разворачиваются в викторианской Англии и рассказывают историю юного графа Сиэля Фантомхайва, родителей которого убили, а сам он чудом избежал гибели, заключив сделку с дьяволом. Теперь он возглавляет крупную фабрику, производящую игрушки и сладости, напрямую подчиняется королеве, а также делает все возможное, чтобы выследить и убить тех, кто виновен в смерти его отца и матери. Его слуга – никто иной как сам дьявол, который принял облик дворецкого по имени Себастьян Михаэлис, одетый всегда в черное и в любую минуту готовый прийти на помощь молодому хозяину.'
          rating = '9.29/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/4/22/d36aacfe85f1cum48q29g.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Очень приятно, Бог"):
          name = 'Очень приятно, Бог'
          site_url='https://rezka.ag/animation/comedy/20326-ochen-priyatno-bog-tv-1-2012.html'
          description = 'Добрая, красивая история о любви.Бесшабашный отец Нанами Момодзоно, окончательно проигравшийся, сбежал, оставив девочку без копейки денег, на следующий день явились незнакомые люди в черном и выбросили все пожитки на улицу. Девочка собрала самое необходимое, и отправилась в городской парк, возле дома оставаться было опасно, кто знает, что взбредет в голову головорезам, занявшим ее жилище?Сидя на скамейке на аллее парка, девочка услышала жалобный голос, умоляющий спасти кого-то от собаки. Собака оказалась не такой уж страшной, а помощи просил молодой человек, которому Нанами и выложила всю свою историю. Парень предложил ей временно пожить в его доме. Странноватое предложение для людей, пять минут назад впервые увидевших друг друга, неправда ли?'
          rating = '9.42/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/12/8/xf961280d7868zl92v24c.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Человек-бензопила👨"):
          name = 'Человек-бензопила'
          site_url='https://rezka.ag/animation/fantasy/51376-chelovek-benzopila-2022.html'
          description = 'Дэндзи мечтает однажды начать вести счастливую и беззаботную жизнь, однако сейчас он вынужден выплачивать огромные долги своего покойного отца. С этой целью главный герой становится нелегальным убийцей демонов, выполняя заказы для якудза, в чем ему помогает самоуверенный домашний питомец по прозвищу Почита, обладающий мощным оружием. Однажды якудза предает Дэндзи, оставляя его на растерзание дьявольского зомби, вот только в решающий момент Почита жертвует собой, чтобы спасти хозяина. Самоотверженность домашнего питомца вызывает серию необъяснимых событий, после чего Дэндзи и Почита оказываются заключены в одно тело…'
          rating = '9.15/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/9/6/hbbe4ef6f114crp83l92l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Кровавый парень🩸"):
          name = 'Кровавый парень'
          site_url='https://rezka.ag/animation/fantasy/22601-krovavyy-paren-2013.html'
          description = 'Действия разворачиваются в сатанинском мире, где существует город-призрак, именуемый Акрополем, расположившийся по центру Ада. Вся территория адского города поделена местными бандами и каждый район принадлежит той или иной криминальной группировке, где заправляет всем свой босс, а правит городом аристократия, населением же является различная нечисть: оборотни, духи, призраки и прочие. В центре повествования находится Влад Чарли Стаз — беспощадный молоденький парень, являющийся вампиром-вегетарианцем, относящимся к наивысшим вампирам, который успел заслужить титул босса Восточного участка.'
          rating = '9.41/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/11/18/p05f8bbc2b3d2nd75m81n.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Тетрадь дружбы Нацумэ"):
          name = 'Тетрадь дружбы Нацумэ'
          site_url='https://rezka.ag/animation/drama/20226-tetrad-druzhby-nacume-tv-1-2008.html'
          description = 'Сюжет сосредоточен вокруг осиротевшего старшеклассника Такаси Нацумэ, который унаследовал от своей бабушки Рэйко способность общаться с духами и прочими сверхъестественными существами. По этой причине юноша стал изгоем, так как не мог объяснить странности своего поведения. Однажды Такаси перебирается жить в дом своей покойной бабушки и находит «Тетрадь дружбы», где она записывала имена побежденных потусторонних существ, которых сделала своими слугами. Главный герой решает направить свои способности в мирное русло, начав помогать добрым духам обрести свободу, попутно сражаясь с силами тьмы.'
          rating = '9.1/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/3/5/t300239ab92e6km58o27l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


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
           8:'Человек-бензопила👨',
           9:'Кровавый парень🩸 ',
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
                [types.KeyboardButton("Человек-бензопила👨")],
                [types.KeyboardButton("Кровавый парень🩸")],
                [types.KeyboardButton("Тетрадь дружбы Нацумэ")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_6 = types.ReplyKeyboardMarkup(keyboard=kb_6 , resize_keyboard=True)
        await message.answer('Вот список, выбирай',reply_markup=keyboard_6)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)






###########################################################################################################################################        
    if (message.text == "Тетрадь смерти📓"):
          name = 'Тетрадь смерти'
          site_url='https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html'
          description = 'В основу сюжета фэнтезийного аниме сериала «Тетрадь смерти» легли культовые японские комиксы, так называемая манга, написанная известным японским писателем Цугуми Оба.Мультсериал повествует историю о некой странной тетради, обладающей магическими свойствами, и являющейся таким себе идеальным оружием. Согласно легенде, если написать на ней имя человека и указать его приметы, то в скором времени его непременно настигнет смерть.'
          rating = '9.26/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/7/1/m2452f445ecd6ds39e76g.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Великий из бродячих псов🐕"):
          name = 'Великий из бродячих псов'
          site_url='https://rezka.ag/animation/adventures/15552-velikiy-iz-brodyachih-psov-tv-1-2016.html'
          description = 'В основу сюжета фэнтезийного аниме сериала «Тетрадь смерти» легли культовые японские комиксы, так называемая манга, написанная известным японским писателем Цугуми Оба.Мультсериал повествует историю о некой странной тетради, обладающей магическими свойствами, и являющейся таким себе идеальным оружием. Согласно легенде, если написать на ней имя человека и указать его приметы, то в скором времени его непременно настигнет смерть.'
          rating = '9.26/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/14/hec4e7410b57dqm31k31l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Ложные выводы"):
          name = 'Ложные выводы'
          site_url='https://rezka.ag/animation/adventures/34941-lozhnye-vyvody-tv-1-2020.html'
          description = 'В одиннадцатилетнем возрасте Котоко Иванагу похитили ёкаи, чтобы сделать её богиней мудрости. Данное звание позволяло бы ей выступать посредником между мирами людей и потусторонних сущностей. Но такая участь требовала жертв, а именно утраты правого глаза и левой ноги. Котоко, недолго думая, дает согласие на такую сделку. Ёкаи с того дня в случае необходимости тотчас обращались к ней за помощью. С момента, как Котоко стала богиней, прошло шесть лет.'
          rating = '7.9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/12/19/mceeeeda4acb7ac98r58s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Обещаный Неверленд"):
          name = 'Обещаный Неверленд'
          site_url='https://rezka.ag/animation/drama/29587-obeschannyy-neverlend-tv-1-2019.html'
          description = 'В приюте «Грейс Филд» жизнь сирот похожа на рай. Хотя у них нет родителей, все дети являются одной большой и счастливой семьей, находясь под опекой доброй женщины, которую они называют «мамой». Здесь они учатся, носят чистую одежду, хорошо питаются и много играют, однако существует одно строгое правило, которому каждый ребенок должен неукоснительно подчиняться: никогда не покидать территорию приюта. Но однажды двое лучших друзей, Эмма и Норман, выходят за ворота и раскрывают ужасающую правду об этом месте. И теперь, если они хотят выжить, им придется найти способ сбежать отсюда...'
          rating = '9.47/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/29/m1a1e19c70126pj95k18p.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Игра друзей"):
          name = 'Игра друзей'
          site_url='https://rezka.ag/animation/drama/47972-igra-druzey-2022.html'
          description = 'Юичи Катагири всю свою жизнь боролся с финансовыми трудностями, но научился оставаться довольным и позитивным благодаря своему близкому кругу друзей. Чтобы сдержать данное им обещание, Юичи копит достаточно денег, чтобы присоединиться к ним в школьной поездке. Но когда собранные деньги таинственным образом пропадают, подозрение падает на двух друзей Юичи: Шихо Савараги и Макото Шибе, которые отвечали за сбор платежей. Хотя Шихо и Макото невиновны, они берут на себя ответственность за неспособность защитить деньги, когда больше никто не появляется.'
          rating = '8.91/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/4/6/u859c72f95432oc55d15o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Эхо терора"):
          name = 'Эхо терора'
          site_url='https://rezka.ag/animation/thriller/2173-eho-terrora-2014.html'
          description = 'Действие драматического аниме-сериала «Эхо террора» разворачивается в наши дни. Однажды в один из самых обычных дней в социальных сетях появляется видеообращение двух парней в масках, называющих себя террористической группой «Сфинкс». Они предупреждают жителей Токио, что в три часа дня столица погрузится во тьму, и в назначенное время город содрогается от ряда террористических актов. Преступники выдают себя за самых обычных школьников, и вне экрана называют друг друга прозвищами Найн и Твелв.'
          rating = '9.29/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/10/21/c1ce42e91500fml42u41b.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Данганронпа: Школа отчаяния"):
          name = 'Данганронпа: Школа отчаяния'
          site_url='https://rezka.ag/animation/thriller/18185-shkola-otchayaniya-2013.html'
          description = 'Действие разворачивается в таинственном учебном заведении, которым руководит неординарный директор — медведь Монокума. Однажды в школе появляются пятнадцать новых учеников, уверенных в том, что в дальнейшем их ждет яркое и блестящее будущее. Но мечты школьников разбиваются после первого диалога с Монокумой, который сообщает ученикам, что их успех полностью зависит от выполнения опасного задания: каждый из них должен убить одноклассника, однако остаться вне подозрений. Серьезно рискуя своими жизнями, новые ученики принимают предложение Монокумы…'
          rating = '8.95/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/8/12/o4002056a85ceuk15t40z.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Амнезия"):
          name = 'Амнезия'
          site_url='https://rezka.ag/animation/adventures/21692-amneziya.html'
          description = 'События аниме «Амнезия» происходят с обычной японской девушкой, которая в один день просыпается в каком-то подсобном помещении ресторана и с удивлением осознает, что не помни, как сюда попала. Из памяти красавицы стерлось даже ее собственное имя, и теперь наша героиня с удивлением смотрит на окружающих, силясь понять, кто все эти люди.'
          rating = '8.78/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/11/3/ed296adfa2ffajr89u76m.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Когда плачут Цикады"):
          name = 'Когда плачут Цикады'
          site_url='https://rezka.ag/animation/thriller/36129-kogda-plachut-cikady-karma-tv-1-2020.html'
          description = 'В 1983 году старшеклассник Кэйити Маэбара переезжает из города в отдаленную деревню Хинамидзава и поступает учиться в местную школу, где сразу же заводит несколько друзей, среди которых: староста Мион Сонодзаки, ее сестра-близнец Сион, сверстница Рэна Рюгу и двое девочек из младших классов, Сатоко Ходзе и Рика Фурудэ. Летом деревня готовится к празднованию традиционного фестиваля «Ватанагаси», который уже четвертый год подряд омрачается загадочными убийствами и исчезновениями людей, что вынуждает подростка и его новых друзей заняться поисками того, кто за всем этим стоит.'
          rating = '7.62/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/p031da44606dbcm69c31x.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if(message.text == "Детектив"):             
        await message.answer("Окей сейчас найдем тебе что-то")      
        anime_7 = {
           1:'Тетрадь смерти📓',
           2:'Великий из бродячих псов🐕',
           3:'Ложные выводы',
           4:'Тёмный дворецкий ',
           5:'Обещаный Неверленд ',
           6:'Игра друзей',
           7:'Эхо терора',
           8:'Данганронпа: Школа отчаяния',
           9:'Амнезия ',
           10:'Когда плачут Цикады'
        }
        await message.answer(f'1:{anime_7[1]}\n2:{anime_7[2]}\n3:{anime_7[3]}\n4:{anime_7[4]}\n5:{anime_7[5]}\n6:{anime_7[6]}\n7:{anime_7[7]}\n8:{anime_7[8]}\n9:{anime_7[9]}\n10:{anime_7[10]}')
        kb_7 = [    
                [types.KeyboardButton("Тетрадь смерти📓")],
                [types.KeyboardButton("Великий из бродячих псов🐕")],
                [types.KeyboardButton("Ложные выводы")],
                [types.KeyboardButton("Тёмный дворецкий")],
                [types.KeyboardButton("Обещаный Неверленд")],
                [types.KeyboardButton("Игра друзей")],
                [types.KeyboardButton("Эхо терора")],
                [types.KeyboardButton("Данганронпа: Школа отчаяния")],
                [types.KeyboardButton("Амнезия")],
                [types.KeyboardButton("Когда плачут Цикады")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_7 = types.ReplyKeyboardMarkup(keyboard=kb_7 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_7)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)





#####################################################################################################################################################
    if (message.text == "Врата Штейна"):
          name = 'Врата Штейна'
          site_url='https://rezka.ag/animation/drama/7718-vrata-shteyna-2011.html'
          description = 'Действие сериала «Врата Штейна» (Steins; Gate) разворачивается в необычном месте под названием Акихабара. Здесь полно странных, а порой даже сумасшедших людей. Главные герои как раз и относятся к таким не совсем адекватным людям. У каждого из них «свои тараканы в голове». Ринтаро Окабэ всего лишь восемнадцать лет, а он уже настоящий ученый и к тому же противостоит мировому заговору.'
          rating = '9.33/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2015/1/26/m0d4621b6dc8fwb95k14q.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Стальной Алхимик:братство⚗️"):
          name = 'Стальной Алхимик:братство'
          site_url='https://rezka.ag/animation/adventures/12092-stalnoy-alhimik.html'
          description = 'алантливые братья Элрики будучи еще совсем детьми, пытаясь воскресить маму, преступили дозволенную черту и нарушили главное табу Алхимии – преобразование человека. Во время ритуала всё пошло не так, как планировали малыши, в результате чего младший Альфонс лишился тела, и теперь его душа запечатана в огромных железных доспехах, а старший Эдвард, заплатив сполна за полученные знания и душу брата, остался без руки и ноги, и теперь вынужден использовать автоброню – специальные стальные доспехи.'
          rating = '9.35/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/3/13/gfa01e809ffc3wf45s69o.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")
 
    if (message.text == "Форма голоса"):
          name = 'Форма голоса'
          site_url='https://rezka.ag/animation/drama/24892-forma-golosa-2016.html'
          description = 'Мир подростков бывает невероятно жесток. Они порой не прощают отличия и с огромной радостью набрасываются на любого, кто ведет себя не так как все или выглядит иначе. В центре событий оказывается девушка по имени Сёко. Малышке совсем недавно пришлось сменить младшую школу. Вот только новые одноклассники вовсе не спешили принимать её в свой круг. Дело в том, что у бедняжки врожденные проблемы со слухом.'
          rating = '9.15/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2017/5/31/efbf5d1a63405nr46m49x.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Вайолет Эвергарден"):
          name = 'Вайолет Эвергарден'
          site_url='https://rezka.ag/animation/drama/26736-vayolet-evergarden-2018.html'
          description = 'После жестокой войны молодая девушка Вайолет Эвергарден хочет начать новую жизнь. Во время боевых действий её буквально использовали в качестве оружия, после чего она осталась без рук. После отставки Вайолет решает сотрудничать с почтовой службой в большом городе. Компания не только осуществляет перевозки, но и пишет письма и корректирует их для малограмотных местных жителей. Девушку привлекает профессия, поэтому она решает присоединиться к команде «автозапоминающих кукол». Вскоре она начинает понимать значение фразы «Я люблю тебя», которую ей когда-то сказал майор Гилберт Бугенвиллеи...'
          rating = '9.47/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/b2d89fc869959bu67b38l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if (message.text == "Сага о Винланде"):
          name = 'Сага о Винланде'
          site_url='https://rezka.ag/animation/adventures/31336-saga-o-vinlande-tv-1-2019.html'
          description = 'В центре событий находится Торфинн — юный сын Торса, одного из величайших викингов всех времен, который живет в небольшой заснеженной деревушке, расположенной на краю мира. Он любит слушать рассказы о Винланде — плодородных западных землях, свободных от войн и работорговли, и больше всего на свете хочет стать бесстрашным воином, чтобы сражаться рука об руку со своим отцом. Однако все мечты героя рушатся после того, как Торса убивает жестокий предводитель наемников Аскелад. И тогда Торфинн клянется во что бы то ни стало отомстить за его смерть, а затем разыскать легендарные земли...'
          rating = '9.15/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/2/13/pf63cf9a0b0b5no38z84r.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Ходячий замок🏯"):
          name = 'Ходячий замок'
          site_url='https://rezka.ag/animation/drama/818-hodyachiy-zamok-2004.html'
          description = 'В основу сюжета приключенческого аниме-мультфильма «Ходячий замок» лег одноименный роман известной английской писательницы Дианы Уинн Джонс. Действия картины разворачиваются в параллельном мире Европы конца XIX-го века. Главная героиня – шляпница Софи ведет скромный образ жизни. Но все меняется после того, как в окрестностях города, где живет девушка, появляется ходячий замок, хозяином которого является загадочный волшебник Хаула, за которым слывет слава похитителя женских сердец.'
          rating = '9.61/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2013/12/6/vf77d254dc1e2au48b43e.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Евангелион"):
          name = 'Евангелион'
          site_url='https://rezka.ag/animation/drama/16253-evangelion-1995.html'
          description = 'Прошло долгих пятнадцать лет с момента внезапного возникновения необъяснимой глобальной катастрофы, поставившей всё человечество под угрозу исчезновения. Но те, кому посчастливилось выжить, даже не догадывались, что это было только начало, ведь вскоре на них обрушилось новое испытание: неожиданно Землю атаковали возникшие неизвестно откуда огромные существа, именуемые Ангелами.'
          rating = '9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/6/30/ecdc72ad364f6mo73s86t.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Девять золушек в августе"):
          name = 'Девять золушек в августе'
          site_url='https://rezka.ag/animation/everyday/56249-devyat-zolushek-v-avguste-2019.html'
          description = 'Однажды Арихара Цубасу поступает в старшую школу и очень скоро обнаруживает, что в ней нет бейсбольного клуба. Решив создать спортивную команду для девочек, она сталкивается с первым серьезным препятствием в лице школьного совета, не поддерживающего ее амбициозную идею. Когда Арихаре удается решить возникшие разногласия, она приглашает в команду всех желающих — от новичков до опытных игроков. По мере того, как члены бейсбольного клуба приступают к тренировкам, в разношерстном коллективе подростков возникают первые конфликты и ссоры…'
          rating = '7.33/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/3/31/s6a8576eb63d1yl47i39v.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if(message.text == "Драма"):
        await message.answer("Окей сейчас найдем тебе что-то") 
        anime_8 = {
           1:'Врата Штейна',
           2:'Атака титанов🤺',
           3:'Стальной Алхимик:братство⚗️',
           4:'Форма голоса ',
           5:'Вайолет Эвергарден ',
           6:'Код Гиас',
           7:'Сага о Винланде',
           8:'Ходячий замок🏯',
           9:'Евангелион ',
           10:'Девять золушек в августе'
        }
        
        await message.answer(f'1:{anime_8[1]}\n2:{anime_8[2]}\n3:{anime_8[3]}\n4:{anime_8[4]}\n5:{anime_8[5]}\n6:{anime_8[6]}\n7:{anime_8[7]}\n8:{anime_8[8]}\n9:{anime_8[9]}\n10:{anime_8[10]}')
        kb_8 = [    
                [types.KeyboardButton("Врата Штейна")],
                [types.KeyboardButton("Атака титанов🤺")],
                [types.KeyboardButton("Стальной Алхимик:братство⚗️")],
                [types.KeyboardButton("Форма голоса")],
                [types.KeyboardButton("Евангелион")],
                [types.KeyboardButton("Вайолет Эвергарден")],
                [types.KeyboardButton("Код Гиас")],
                [types.KeyboardButton("Сага о Винланде")],
                [types.KeyboardButton("Ходячий замок🏯")],
                [types.KeyboardButton("Девять золушек в августе")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_8 = types.ReplyKeyboardMarkup(keyboard=kb_8 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_8)

#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)



########################################################################################################################################        
    if (message.text == "Покемон"):
          name = 'Покемон'
          site_url='https://rezka.ag/animation/adventures/18291-pokemon-1997.html#t:56-s:1-e:1'
          description = 'Пикачу – один из сильнейших покемонов, который по неизвестной причине выбрал себе в тренеры молодого парнишку по имени Эш. Товарищи стали путешествовать вместе, по пути посещая соревнования и помогая людям решать их проблемы. В скором времени на пути наших путешественников встретился еще один тренер, который специализировался на каменных покемонах, и предложил путешествовать вместе. Эш согласился, но вскоре к компании присоединилась еще одна участница по имени Мисти и ее очаровательные водные покемоны, которые чаще озорничали вместе, чем готовились к соревнованиям.'
          rating = '9.37/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/10/11/j58735ee94b4djx33m23d.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Невероятные приключения ДжоДжо"):
          name = 'Невероятные приключения ДжоДжо'
          site_url='https://rezka.ag/animation/adventures/11986-neveroyatnye-priklyucheniya-dzhodzho-tv-1-2012.html'
          description = 'Так уж сложилось, что в каждом поколении легендарной семьи Джостаров появляется прямой или побочный потомок, чьё имя начинается с того же слога, что и фамилия, вследствие чего он получает традиционное для семейства прозвище ДжоДжо.События разворачиваются в Великобритании на протяжении второй половины XIX века. Вор Дарио Брандо, столкнув в пропасть семейную повозку Джостаров, в которой был маленький Джонатан, выдаёт себя за спасителя, чем заслуживает снисхождение выжившего главы семейства.'
          rating = '9.37/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/c5c4a216e607dph36u98w.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Хантер х Хантер"):
          name = 'Хантер х Хантер'
          site_url='https://rezka.ag/animation/fantasy/2066-ohotnik-h-ohotnik-2011.html'
          description = 'Приключенческий аниме-сериал «Охотник х Охотник» снят по мотивам одноименной манги Ёсихиро Тогаси.Действие разворачивается в мире, где существует некая организация Охотников, имеющая множество всевозможных привилегий. Они могут путешествовать любым видом транспорта совершенно бесплатно, да еще и первым классом. Так же члены организации имеют доступ к большим сумам денег в каждом банке, а так же информации, которая попросту закрыта для других людей. Многие желают вступить в ряды Охотников, и по этой причине каждый год проводиться экзамен, по результатам которого отбирают самых достойных.Однажды на один из таких экзаменов отправляется и главный герой, Гон Фрикс, который хочет стать охотником для того чтобы найти своего отца. Впереди его ждет много трудностей и испытаний, преодолевая которые он найдет много новых друзей, каждый из которых имеет свои веские причины стать Охотником…'
          rating = '9.22/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2019/8/6/e40032f0b93fbkd22i89y.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Драгон Квест: Приключения Дая🐉"):
          name = 'Драгон Квест: Приключения Дая'
          site_url='https://jut.su/dragon-quest/episode-1.html'
          description = 'Несколько лет назад Владыка тьмы Хадлар сумел разрушить множество селений, а также убить тысячи мирных жителей. На помощь человечеству пришли отважные герои, которые сумели одолеть армию тьмы. Об этих героях начали слагать легенды, и все люди позабыли о кровожадном Хадларе. На острове Дермлин живёт множество монстров, которые нашли на этом месте пристанище. Среди жутких тварей живёт отважный мальчишка по имени Дай. Юноша всю жизнь мечтает стать великим героем, как его предки, но все попытки заканчиваются неудачей. Мальчишка частенько нападает на слабых монстров, чтобы отточить мастерство владения мечом.'
          rating = '9.32/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://yummyanime.tv/image200x300/uploads/posts/2020-11/1604764097_poster.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Богиня благословляет этот прекрасный мир💧"):
          name = 'Богиня благословляет этот прекрасный мир'
          site_url='https://rezka.ag/animation/fantasy/16209-boginya-blagoslovlyaet-etot-prekrasnyy-mir-tv-1-2016.html'
          description = 'Молодой паренёк Казума Сато – типичный хикикомори, который может сутками не выходить из собственной квартиры, играя с виртуальными друзьями в различные видеоигры. В один прекрасный день парень решает прервать своё повседневное затворничество и выбраться за пределы собственного жилья, чтобы добраться до ближайшего игрового магазина, где в этот раз он собирается купить ограниченное издание очень популярной онлайн игры. Уже через несколько часов уставший, но очень довольный, радостно сжимая коробку с игрой, Казума возвращался домой, как вдруг он заметил, что на девушку, в которой он узнал свою одноклассницу, несётся какой-то автомобиль, после чего парню удаётся в последний момент вытолкнуть её из-под колёс…'
          rating = '9.37/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/6/30/w56c4128f453adf90t90b.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Хроники Горизонта"):
          name = 'Хроники Горизонта'
          site_url='https://rezka.ag/animation/adventures/7622-hroniki-gorizonta-tv-1-2013.html'
          description = 'Онлайн-игра «Elder Tales» пользуется огромной популярностью, поскольку предлагает пользователям виртуальное погружение в уникальный постапокалиптический мир. С большим количеством квестов, гильдий и харизматичных персонажей игра стала отличным способом отвлечься от повседневных забот. Однако все меняется с выходом нового патча, из-за которого ряд пользователей оказался в ловушке внутри игры, когда пропала возможность выйти из «Elder Tales». Виртуальный мир становится новой реальностью для множества игроков...'
          rating = '9.33/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/1/10/i3254a115593acv34p54l.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Хроники Акаши"):
          name = 'Хроники Акаши'
          site_url='https://rezka.ag/animation/adventures/25522-akashiyskie-hroniki-hudshego-prepodavatelya-magii-2017.html'
          description = 'Магия – дело непростое и очень ответственное. Чтобы выучиться на настоящего мага, необходимо потратить множество времени и усилий. Но оно того стоит, ведь люди, познавшие эту дисциплину, обладают невероятными способностями, а также ведают тайны мироздания. И, конечно, существуют специальные места и академические городки, в которых детишек обучают магии. Одним из таких мест является Феджит, где учатся две главные героини – Люмия и Систи. Девчонки прилагают максимум усилий и мечтают стать лучшими в своем деле. Внезапно они узнают ужасную новость: их обожаемый преподаватель Хьюг уволился. Как же теперь быть, и кто его заменит?'
          rating = '9.52/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
           
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/2/17/a5b7c5bf3c4a4hz53s99s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")




    if(message.text == "Приключения"):
        await message.answer("Окей сейчас найдем тебе что-то")   
        anime_9 = {
           1:'Покемон',
           2:'Невероятные приключения ДжоДжо',
           3:'Хантер х Хантер',
           4:'Драгон Квест: Приключения Дая🐉',
           5:'Богиня благословляет этот прекрасный мир💧',
           6:'Хроники Горизонта',
           7:'Хроники Акаши',
        
        }
        await message.answer(f'1:{anime_9[1]}\n2:{anime_9[2]}\n3:{anime_9[3]}\n4:{anime_9[4]}\n5:{anime_9[5]}\n6:{anime_9[6]}\n7:{anime_9[7]}')
        kb_9 = [    
                [types.KeyboardButton("Покемон")],
                [types.KeyboardButton("Невероятные приключения ДжоДжо")],
                [types.KeyboardButton("Хантер х Хантер")],
                [types.KeyboardButton("Драгон Квест: Приключения Дая🐉")],
                [types.KeyboardButton("Богиня благословляет этот прекрасный мир💧")],
                [types.KeyboardButton("Хроники Горизонта")],
                [types.KeyboardButton("Хроники Акаши")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_9 = types.ReplyKeyboardMarkup(keyboard=kb_9 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_9)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)




##########################################################################################################################################        
    if (message.text == "Реинкорнация безработного"):
          name = 'Реинкорнация безработного'
          site_url='https://rezka.ag/animation/adventures/36797-reinkarnaciya-bezrabotnogo-tv-1-2021.html'
          description = 'В центре сюжета окажется безработный мужчина, который спасает группу подростков от верной гибели, но умирает сам. Неожиданно он просыпается в волшебном мире под новым именем — теперь его зовут Рудеус Грейрат. С удивлением герой обнаруживает в себе магические способности, а его новые родители уверены, что их сына ждёт большое будущее. Вскоре Рудеус отправляется проходить обучение у самых сильных воинов. Но, несмотря на стремление к великому, Рудеус всё ещё мечтает встретить девушку...'
          rating = '9.42/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/10/1/b1fbd9cb81659dr11y93z.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")
    
    if (message.text == "Нет игры-нет жизни🃏"):
          name = 'Нет игры-нет жизни'
          site_url='https://rezka.ag/animation/adventures/21251-net-igry-net-zhizni-2014.html'
          description = 'В центре сюжета находятся Сора и Широ — брат и сестра, которые известны среди геймеров в качестве легендарного дуэта «Бланк». Главные герои рассматривают реальный мир как очередную ужасную игру, однако их жизни кардинально меняются, когда они случайно оказываются в потустороннем мире, где встречаются с богом игр Тетом. В этом мире любые конфликты решаются посредством сложных игр, в которых игроки должны делать высокие ставки. В этой странной вселенной Сора и Широ неожиданно находят для себя настоящий вызов — объединить союзников, победить Тета и стать богами.'
          rating = '9.59/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/25/g1d4eafb3859fjk24p48a.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Мастера меча онлайн⚔️"):
          name = 'Мастера меча онлайн'
          site_url='https://rezka.ag/animation/drama/2038-mastera-mecha-onlayn-tv-1-2012.html'
          description = 'В основу сюжета захватывающего фантастического аниме-сериала «Мастера меча онлайн» лег цикл лайт-новелл известного японского писателя Рэки Кавахары.Действие разворачивается в недалеком будущем, когда технологии достигли такого прогресса, что позволили производителям компьютерных игр использовать так называемую технологию «Полного погружения». Одной из них становиться многопользовательская онлайн-игра под названием «Sword Art Online». Опытный геймер по имени Казуто «Кирито» Киригае становиться одним из немногих кому предоставляется шанс поучаствовать в бета-тестинге самой ожидаемой ММОРПГ.'
          rating = '9.4/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/9/14/qe33ce4aefc5dgd15k34g.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Возрождающие"):
          name = 'Возрождающие'
          site_url='https://rezka.ag/animation/fiction/29761-vozrozhdayuschie-2017.html'
          description = 'Сота Мизушино – шестнадцатилетний ученик средней школы, мечтающий выпустить собственное ранобэ. В поисках вдохновения он решает посмотреть аниме на своем планшете, но неожиданно переносится в вымышленный мир, где становится свидетелем жестокой битвы между персонажами. Вскоре после этого он возвращается в реальность и с удивлением обнаруживает, что Селесия, главная героиня, каким-то образом вернулась вместе с ним. Вслед за девушкой в реальный мир переместились и другие персонажи, не все из которых оказались положительными…'
          rating = '7.61/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/j2855d5681061qm12q35s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Да я паук и что🕷️"):
          name = 'Да я паук и что'
          site_url='https://rezka.ag/animation/adventures/36321-da-ya-pauk-i-chto-s-togo-2021.html'
          description = 'В результате ожесточенного противостояния Героя и Короля Демонов в фантастическом измерении идет в ход сильное заклинание, которое случайно уничтожает целый класс старшеклассников японской школы в мире людей. В качестве компенсации подросткам даруют новую жизнь, но одна из жертв, самая застенчивая и невзрачная Кумоко, каким-то образом оказывается в теле гигантского паука. И теперь ей приходится адаптироваться к новому телу в недружелюбном и опасном мире подземелья, благо имея в своем арсенале целый ряд мощных способностей.'
          rating = '8.51/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/ncf3f087acabbdu75r42a.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "В другом мире со смартфоном📱"):
          name = 'В другом мире со смартфоном'
          site_url='https://rezka.ag/animation/adventures/27379-v-drugom-mire-so-smartfonom-tv-1-2017.html'
          description = 'История данного аниме рассказывает нам о трагической смерти молодого парня по имени Мотидзуки Тоя, которого ударила молния. Этого не должно было случиться, так заявляют боги герою, когда он покидает свое бренное тело. В качестве извинения и компенсации Мотидзуки предлагают возможность прожить другую жизнь в сказочном и волшебном мире, населенном волшебными существами. Парень соглашается, но вместо каких-либо серьезных пожеланий он просит позволить взять с собой простой смартфон. Что он будет делать с ним в следующей жизни пока не понятно, но Тоя был тверд в своем решении.'
          rating = '9.1/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/y0bffac5a62ccri44o33a.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Восхождение героя щита🛡️"):
          name = 'Восхождение героя щита'
          site_url='https://rezka.ag/animation/fantasy/29842-voshozhdenie-geroya-schita-2018.html'
          description = 'Наофуми Иватани — добродушный студент из Японии, увлекающийся мангой и компьютерными играми. Однажды, наткнувшись на таинственную книгу, юноша переносится в параллельное измерение, где ему сообщают, что он — один из четырех легендарных героев, призванных спасти мир от уничтожения. Будучи героем щита, Наофуми считается самым слабым из четверки, из-за чего сталкивается с пренебрежительным отношением со стороны окружающих. Несмотря на это, он отправляется в путешествие, чтобы развить свои навыки, однако вскоре спутница героя предает его, ограбив и обвинив в преступлении. Попав в немилость короля, Наофуми становится изгоем, и теперь ему придется пройти весь путь самостоятельно…'
          rating = '9.41/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/7/bfb2aa5dea1cazp66i76z.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Лучший в мире убийца переродился в другом мире в аристократа"):
          name = 'Лучший в мире убийца переродился в другом мире в аристократа'
          site_url='https://rezka.ag/animation/action/42776-luchshiy-v-mire-assasin-pererodivshiysya-v-drugom-mire-kak-aristokrat-2021.html'
          description = 'Луг — пожилой мужчина, которого считают величайшим в мире убийцей. В связи с его преклонным возрастом было принято окончательное решение, что Луг может выйти на пенсию. Но самолет, в котором он находился, был захвачен и даже навыки ассасина не смогли спасти его от смерти. Когда он погиб, его воскресила богиня, которая желает перевоплотить Луга, чтобы предотвратить разрушение мира мечей и магии. Принимая предложение богини, величайший убийца приходит в себя в новом для него мире и дает торжественную клятву, что он проживет эту жизнь в полной мере как человек, а не инструмент для убийства.'
          rating = '8.56/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/10/8/c0b7d7d306991ux96k99c.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня"):
          name = 'Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня'
          site_url='https://rezka.ag/animation/fantasy/38776-ubivaya-slizney-300-let-sama-togo-ne-zametiv-ya-dostigla-maksimalnogo-urovnya-2021.html'
          description = 'После долгих лет корпоративного «рабства» в крупной компании, Азуса неожиданно скончалась из-за сильного переутомления. Внезапно героиня встречает богиню, которая дарует ей бессмертие и мирную жизнь в другом мире. С этого момента Азуса живет на ферме, а также занимается защитой близлежащей деревни от слизней, убивая их. Монотонный образ жизни девушки начинает меняться, когда она случайно достигает максимально возможного опыта, чем привлекает к себе нежелательное внимание. В скором времени различные персонажи, включая дракона Лайка и эльфийку Халкара, начинают появляться у ее поместья — одни ищут битвы, другие просят ее помощи…'
          rating = '8.41/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/4/11/j16a662ab6694ds68u35k.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if(message.text == "Исекай"):
        await message.answer("Окей сейчас найдем тебе что-то")   
        anime_10 = {
           1:'Реинкорнация безработного',
           2:'Нет игры-нет жизни🃏',
           3:'О моём перерождении в слизь',
           4:'Мастера меча онлайн⚔️ ',
           5:'Возрождающие ',
           6:' Да я паук и что🕷️',
           7:'В другом мире со смартфоном📱',
           8:'Восхождение героя щита🛡️',
           9:'Лучший в мире убийца переродился в другом мире в аристократа ',
           10:'Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня'
        }
        await message.answer(f'1:{anime_10[1]}\n2:{anime_10[2]}\n3:{anime_10[3]}\n4:{anime_10[4]}\n5:{anime_10[5]}\n6:{anime_10[6]}\n7:{anime_10[7]}\n8:{anime_10[8]}\n9:{anime_10[9]}\n10:{anime_10[10]}')
        kb_10 = [    
                [types.KeyboardButton("Реинкорнация безработного")],
                [types.KeyboardButton("Нет игры-нет жизни🃏")],
                [types.KeyboardButton("О моём перерождении в слизь")],
                [types.KeyboardButton("Мастера меча онлайн⚔️")],
                [types.KeyboardButton("Возрождающие")],
                [types.KeyboardButton("Да я паук и что🕷️")],
                [types.KeyboardButton("В другом мире со смартфоном📱")],
                [types.KeyboardButton("Восхождение героя щита🛡️")],
                [types.KeyboardButton("Лучший в мире убийца переродился в другом мире в аристократа ")],
                [types.KeyboardButton("Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_10 = types.ReplyKeyboardMarkup(keyboard=kb_10 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_10)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)



########################################################################################################################################        
    if (message.text == "Бегущий по краю"):
          name = 'Бегущий по краю'
          site_url='https://rezka.ag/animation/fiction/51066-kiberpank-beguschie-po-krayu-2022.html'
          description = 'Действие происходит в Найт-Сити — стильном городе будущего, где люди помешаны на технологиях и модификациях тела, а социальное неравенство привело к крайне высокому уровню преступности. В центре сюжета находится Дэвид Мартинес — талантливый подросток, посещающий престижную академию, на оплату которой уходит вся зарплата его матери-одиночки Глории, работающей фельдшером. После того как в жизни главного героя приключается болезненная трагедия, он становится «бегуном по краю» — наемником-преступником, также известным как Киберпанк.'
          rating = '9.03/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/4/11/j16a662ab6694ds68u35k.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Акира"):
          name = 'Акира'
          site_url='https://rezka.ag/animation/fiction/9251-akira-1988.html'
          description = 'Спустя 31 год после тотального разрушения во время Третьей мировой войны, Токио был восстановлен и постепенно превратился в процветающий город. В центре сюжета находится Шотаро Канеда — лидер банды байкеров. Однажды его близкий друг Тецуо получил ранение в результате несчастного случая, после чего он был доставлен в сверхсекретное правительственное учреждение. Очень скоро у Тецуо развиваются невероятные телекинетические способности, которые он решает использовать для достижения коварных целей. Когда выясняется, что Тецуо обладает силой, которая привела к разрушению Токио, Канеда становится единственным человеком, способным спасти город и жизнь своего друга.'
          rating = '9.03/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2015/5/11/jc0ed3518ad6atl40h13c.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Эксперементы Лейн"):
          name = 'Эксперементы Лейн'
          site_url='https://rezka.ag/animation/drama/20157-eksperimenty-leyn-1998.html'
          description = 'Данный аниме-сериал за время своего существования вызывал множество противоречивых эмоций и отзывов. Кто-то считает его не самым удачным, а для кого-то он стал своего рода открытием. «Эксперименты Лэйн» заставляет заглянуть внутрь человеческой сущности, разума, задуматься о многих вещах, на которые люди просто не обращают внимания в повседневной жизни. При просмотре этого аниме, каждый придет к своим выводам и получит свое понимание, недоступное остальным.Мир, показанный в аниме, сильно напоминает наше время.'
          rating = '9.01/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/5/h0140d7a965b5zz55j24r.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Психопаспорт"):
          name = 'Психопаспорт'
          site_url='https://rezka.ag/animation/thriller/2339-psihopasport-tv-1-2012.html'
          description = 'Действие разворачивается в футуристическом мире, где одной мысли о преступлении достаточно, чтобы получить обвинение и признание вины. Плохие намерения больше невозможно скрыть, и полицейские точно знают, кто из потенциальных преступников собирается перейти черту. Используя инновационное приспособление «Доминатор», способное читать мысли и оценивать риски того, что гражданин станет преступником, полицейские эффективно ведут борьбу с головорезами, однако не все поддерживают современную методику. Одаренная Аканэ Цунэмори всегда ставит собственное чувство справедливости выше суждений системы Сибил, анализирующей преступные намерения, и неожиданно находит союзника, поддерживающего ее методы…'
          rating = '9.26/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/8/17/aa8feb5a72036ud18p26i.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Акудама Драйв"):
          name = 'Акудама Драйв'
          site_url='https://rezka.ag/animation/adventures/35930-akudama-drayv-2020.html'
          description = 'В далеком прошлом в Японии вспыхнула война между двумя крупнейшими регионами страны: Кансай и Канто. Тогда Кансай, центр которого находится в Киото, потерпел сокрушительное поражение и был вынужден подчиниться воле правителей из Токио, стоящих во главе Канто. С течением времени, когда на захваченных территориях начала орудовать группировка безжалостных преступников, известная как Акудама, Канто стал терять контроль над Кансай, а оба региона оказались на пороге нового кровопролития...'
          rating = '9.26/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/v8032f3b572c2ye70j21q.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Измерение W"):
          name = 'Измерение W'
          site_url='https://rezka.ag/animation/fiction/12334-izmereniew.html'
          description = 'Никола Тесла – величайший физик ХIХ века, прославившийся множеством выдающихся изобретений, но, несмотря на все заслуги, его идею о беспроводной передаче электричества на большие расстояния многие ученые того времени рассматривали как помешательство.И вот в далёком будущем, спустя чуть менее века после даты смерти гениального ученого, в 2036 году было наконец-то доказано существование четвертого измерения W, представляющего собой бесконечный источник электрической энергии, для получения которого величайшие умы человечества изобрели межпространственный электромагнитный индукционный прибор, получивший простое название «катушка». Чтобы стабилизировать энергию из четвертого измерения, по всему миру было построено шестьдесят огромных башен, позволивших снабжать электричеством всю планету.'
          rating = '9.45/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/3/27/a9626c62f2bc2ar12t42s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Метрополис"):
          name = 'Метрополис'
          site_url='https://rezka.ag/animation/drama/10150-metropolis.html'
          description = '«Метрополис» (Metoroporisu) – японский мультфильм о будущем. В огромном городе множество роботов, которые работают вместо людей на производстве. Правитель Метрополиса потерял свою дочь Тиму. Он обращается к гениальному, но сумасшедшему ученому Лоутону с поручением – сделать точную копию Тимы. Но лаборатория взрывается, ученый погибает, а девочка-робот сбегает. Охотник на роботов, которые вышли из под контроля, идет искать ее, прихватив с собой сына. Тем временем Тима встречает обычного мальчика Кеничи, который думает, что девочка каким-то образом потеряла память. Он и подумать не мог, что попадет в самый центр масштабного заговора, который может погубить не одну тысячу жизней.'
          rating = '8.9/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2015/6/21/jf329a695f989ue46l85s.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Армитаж"):
          name = 'Армитаж'
          site_url='https://rezka.ag/animation/adventures/24686-armitazh-dvoynaya-matrica-2002.html'
          description = 'В центре сюжета оказывается главная героиня по имени Наоми Армитаж. Смелая, красивая и умная девушка-боец вынуждена была бежать от врагов вместе с Россом Силибусом, взяв себе вымышленные имена и фамилии. Нашим героям ничего не осталось, кроме как залечь на дно, укрывшись на далеком Марсе, где вряд ли их кто-то сможет найти. Здесь парочка успокоилась и стала жить размеренно, растя любимую дочурку по имени Йоко. Но все переворачивается с ног на голову, когда происходит непредвиденное. На земном предприятии, которое производило антиматерию, неожиданно происходит бунт роботов.'
          rating = '8.15/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2017/5/14/wad0b0a5af8fedp49q17a.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Технолайз"):
          name = 'Технолайз'
          site_url='https://rezka.ag/animation/drama/20554-tehnolayz.html'
          description = 'Японский фантастический аниме-сериал режиссера Хироси Хамасаки, созданный в лучших традициях жанра киберпанк и повествующий о мрачном подземном городе-гетто под названием Люкс, основанном в недалеком будущем с единственной целью – поселения там многочисленных асоциальных элементов, угрожающих цивилизованному обществу. Сосланные туда преступники, бунтари и прочие несогласные довольно быстро организовались в несколько мощных группировок, ведущих непрерывную кровопролитную борьбу за власть. Неподалеку от изолированного города, раздираемого постоянными междоусобицами, расположен своеобразный оплот технологической элиты Класс, а также деревня Габэ, жители которой предпочли жить обособленно, организовав секту из единомышленников.'
          rating = '8.81/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/13/e0964dcf32e7ejv31y36k.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if(message.text == "Киберпанк"):
        await message.answer("Окей сейчас найдем тебе что-то")
        anime_11 = {
           1:'Бегущий по краю',
           2:'Акира',
           3:'Эксперементы Лейн',
           5:'Психопаспорт',
           6:'Акудама Драйв',
           7:'Измерение W',
           8:'Метрополис',
           9:'Армитаж',
           10:'Технолайз'
        }
        await message.answer(f'1:{anime_11[1]}\n2:{anime_11[2]}\n3:{anime_11[3]}\n5:{anime_11[5]}\n6:{anime_11[6]}\n7:{anime_11[7]}\n8:{anime_11[8]}\n9:{anime_11[9]}\n10:{anime_11[10]}')
        kb_11 = [    
                [types.KeyboardButton("Бегущий по краю")],
                [types.KeyboardButton("Акира")],
                [types.KeyboardButton("Эксперементы Лейн")],
                [types.KeyboardButton("Психопаспорт")],
                [types.KeyboardButton("Акудама Драйв")],
                [types.KeyboardButton("Измерение W")],
                [types.KeyboardButton("Метрополис")],
                [types.KeyboardButton("Армитаж")],
                [types.KeyboardButton("Технолайз")],
                [types.KeyboardButton("⬅️Назад")],
          
      ] 
        keyboard_11 = types.ReplyKeyboardMarkup(keyboard=kb_11 , resize_keyboard=True)
        await message.answer('Вот список , выбирай',reply_markup=keyboard_11)

#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)
    if (message.text == "Пинг-понг🏓"):
          name = 'Пинг-понг'
          site_url='https://rezka.ag/animation/sport/21043-ping-pong-2014.html'
          description = 'История о двух друзьях Макото по прозвищу Смехач и Ютаки, которого приятели зовут Пеко. В целом мире сложно найти двоих более непохожих ребят, но мальчишки с детства не разлей вода.То, что Макото называют смехачом, чистейшей воды сарказм, он всегда угрюм, и никогда не улыбается. Ютаки – полнейшая противоположность, он вечно дурачится и хохочет, а Пеко его назвали за болезненное пристрастие к конфетам с таким названием.'
          rating = '9.02/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/23/j41e30e05874ddy12q37c.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Волейбол🏐"):
          name = 'Волейбол'
          site_url='https://rezka.ag/animation/comedy/11031-voleybol-tv-1-2014.html'
          description = 'Однажды, включив телевизор, двенадцатилетний Хината Сёё попадает на трансляцию волейбольного чемпионата, и с первого взгляда влюбляется в эту увлекательную игру. Волейбол настолько покоряет мальчика, что он даже собирает собственную школьную команду, и вместе с ней оправляется на турнир. Однако в первой же игре они сталкиваются с очень сильным противником в лице команды плеймейкера Тобио Кагеяма, который на тот момент уже был настоящим профессионалом. Он чуть ли не в одиночку устраивает команде Хинате разгромное поражение, что очень сильно бьет по самолюбию героя.'
          rating = '9.37/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/fe61c02053f7eig83k40d.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Баскетбол Куроко🏀"):
          name = 'Баскетбол Куроко'
          site_url='https://rezka.ag/animation/comedy/12002-basketbol-kuroko-tv-1-2012.html'
          description = 'Баскетбольный клуб средней школы Тэйко прославился в японском молодёжном баскетболе отнюдь не своими прекрасными традициями. О нем стали всё чаще говорить, когда туда пришли пятеро феноменальных игроков, ставших так называемой «дрим тим», которая за последние годы сумела победить во всех соревнованиях, где парни принимали участие. Получив прозвище «Поколение Чудес» и принеся Тэйко невероятную славу, юные таланты, повзрослев, разошлись по разным дорогам и поступили в различные старшие школы, где они стали могучей опорой существующих команд, постоянно соперничающих между собой. В тот момент мало кто мог подумать, что в тени прославленной пятёрки находился шестой игрок, совершенно не уступавший им в способностях, но слава по непонятной причине обошла его стороной, оставив имя парня и его заслуги незамеченными.'
          rating = '9.45/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/3/1/rca98930dcbbfqr28z66f.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Blue Lock⚽"):
          name = 'Blue Lock'
          site_url='https://rezka.ag/animation/sport/52222-sinyaya-tyurma-blyu-lok-2022.html'
          description = 'Продолжая терпеть обидные поражения на чемпионатах мира по футболу, японская спортивная ассоциация решает доверить тренерский пост Дзимпати Эго, которому поставлена сложная цель: привести Японию к триумфу на международном турнире. Будучи уверенным в том, что залог успеха — наличие в команде самодостаточного и амбициозного нападающего, Дзимпати решает провести эксперимент, организовав тренировки в специальном лагере «Синяя тюрьма», куда приезжают талантливые, но начинающие футболисты. В лагере, оказавшись в условиях безжалостной конкуренции и тренировок на износ, спортсмены ведут отчаянную борьбу за место в национальной футбольной сборной.'
          rating = '9.12/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/10/9/i2f64cf4caa06sm21v50q.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "SK8 the Infinity🛹"):
          name = 'SK8 the Infinity'
          site_url='https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html'
          description = 'Старшеклассник Рэки, едва увидев один раз, начинает фанатеть по S — опасной подпольной гонке без правил на скейтбордах в заброшенной шахте, где разгораются ожесточенные баталии между участниками, не брезгующими грязными приёмами. Вместе с Рэки в мир опасных гонок оказывается вовлечён недавно вернувшийся из Канады Ланга, который раньше даже ни разу не стоял на скейте.'
          rating = '9.28/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/10/9/i2f64cf4caa06sm21v50q.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Yuri on Ice⛸️"):
          name = 'Yuri on Ice'
          site_url='https://rezka.ag/animation/drama/29722-yuri-na-ldu-2016.html'
          description = 'После позорного выступления в финале Гран-при по фигурному катанию, японский спортсмен Юри Кацуки, разочаровавшись в собственных силах, собирается закончить карьеру. Однажды судьба сводит главного героя с Виктором Никифоровым, чемпионом мира по фигурному катанию, который, посмотрев видеозапись успешного выступления Юри, приезжает в Японию, желая тренировать парня. Приняв предложение тренера, фигурист обретает уверенность в себе, что помогает ему забыть о прошлом позоре и с новыми силами начать путь к достижению спортивных высот.'
          rating = '9.08/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2019/2/1/x1f492256c96cji47r54q.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Вольный стиль!🏊‍♂️"):
          name = 'Вольный стиль!'
          site_url='https://rezka.ag/animation/sport/2317-volnyy-tv-1-2013.htm'
          description = 'После позорного выступления в финале Гран-при по фигурному катанию, японский спортсмен Юри Кацуки, разочаровавшись в собственных силах, собирается закончить карьеру. Однажды судьба сводит главного героя с Виктором Никифоровым, чемпионом мира по фигурному катанию, который, посмотрев видеозапись успешного выступления Юри, приезжает в Японию, желая тренировать парня. Приняв предложение тренера, фигурист обретает уверенность в себе, что помогает ему забыть о прошлом позоре и с новыми силами начать путь к достижению спортивных высот.'
          rating = '9.34/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2014/11/9/sbb4d81c34b42ky67s96y.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Клуб белых воротничков🏸"):
          name = 'Клуб белых воротничков'
          site_url='https://animego.org/anime/klub-raymana-1968'
          description = 'Хотя считается, что бадминтон не командный вид спорта и чаще всего игроки «сражаются» один на один, тем не менее каждый японский бадминтонист состоит в клубе. Этот клуб, как правило, «прикреплен» к организации или финансовой компании, которая является и главным спонсором. Бадминтонист числится как сотрудник компании, которая содержит клуб, но его должностные обязанности определяет политика компании.Как раз с этим нюансом придётся столкнуться Микото Сиратори, недавно уволенному из бадминтонного клуба при крупном банке, где бадминтонисты занимались только тренировками.Микото довольно быстро получил предложение о работе в другом клубе, только вот оказалось, что здесь бадминтонисты не только игроки, но и деятельные члены компании, так что отныне ему придётся не только махать ракеткой, но и сражаться за повышение продаж!Однако не только это стало для Микото неприятным сюрпризом. Мало того, что он понятия не имеет о продажах, что из-за работы теряется драгоценное время тренировок, так ещё и по требованию компании он теперь должен играть в паре, чего он хотел бы избежать по личным причинам.'
          rating = '8.6/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://animego.org/media/cache/thumbs_250x350/upload/anime/images/61d74a4d796e4649085496.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Iwa-Kakeru! -Sport Climbing Girls🧗‍♀️"):
          name = 'Iwa-Kakeru! -Sport Climbing Girls'
          site_url='https://rezka.ag/animation/comedy/36420-derzhis-krepche-skalolazki-2020.html'
          description = 'Кономи Касахара — ученица средней школы для девочек, которая стала популярной, выиграв большое количество соревнований по решению головоломок. Однажды, случайно наткнувшись на школьный скалодром, Касахара решила стать участницей клуба спортивного скалолазания, еще не зная, что новое занятие кардинально изменит ее жизнь. Используя в скалолазании развитые аналитические способности, благодаря которым девушка решала запутанные головоломки, Кономи увлекается новым для нее видом спорта, постепенно добиваясь удивительного прогресса...'
          rating = '6.89/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://rezka.ag/animation/comedy/36420-derzhis-krepche-skalolazki-2020.html')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Ре-Мейн🏖️"):
          name = 'Ре-Мейн'
          site_url='https://rezka.ag/animation/drama/40547-re-meyn-2021.html'
          description = 'Минато Киюмизу — перспективный игрок в водное поло, который в составе школьной команды добивается первенства на национальном молодежном чемпионате, но во время возвращения домой вместе с семьей попадает в серьезную автомобильную аварию, а результате чего полгода проводит в коме. Наконец очнувшись в больнице, подросток не может вспомнить последние 3 года своей жизни, в том числе любимое спортивное увлечение. 4 месяца спустя главный герой переводится учиться в старшую школу, заводит новых друзей и решает возобновить тренировки по водному поло.'
          rating = '8.33/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/7/4/y5f80af066b71hb65b56y.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if(message.text == "Спокон"):
         await message.answer("Окей сейчас найдем тебе что-то")   
         anime_12 = {
               1: 'Пинг-понг🏓', 
               2: 'Волейбол🏐', 
               3: 'Баскетбол Куроко🏀', 
               4: 'Blue Lock⚽', 
               5: 'SK8 the Infinity🛹',
               6: 'Yuri on Ice⛸️',
               7: 'Вольный стиль!🏊‍♂️',
               8: 'Клуб белых воротничков🏸',
               9: 'Iwa-Kakeru! -Sport Climbing Girls🧗‍♀️',
               10: 'Ре-Мейн🏖️'
         }
         await message.answer(f'1:{anime_12[1]}\n2:{anime_12[2]}\n3:{anime_12[3]}\n5:{anime_12[5]}\n6:{anime_12[6]}\n7:{anime_12[7]}\n8:{anime_12[8]}\n9:{anime_12[9]}\n10:{anime_12[10]}')   
         kb_12 = [    
                [types.KeyboardButton("Пинг-понг🏓")],
                [types.KeyboardButton("Волейбол🏐")],
                [types.KeyboardButton("Баскетбол Куроко🏀")],
                [types.KeyboardButton("Blue Lock⚽")],
                [types.KeyboardButton("SK8 the Infinity🛹")],
                [types.KeyboardButton("Yuri on Ice⛸️")],
                [types.KeyboardButton("Вольный стиль!🏊‍♂️")],
                [types.KeyboardButton("Клуб белых воротничков🏸")],
                [types.KeyboardButton("Iwa-Kakeru! -Sport Climbing Girls🧗‍♀️")],
                [types.KeyboardButton("Ре-Мейн🏖️")],
                [types.KeyboardButton("⬅️Назад")],
      ]   
         keyboard_12 = types.ReplyKeyboardMarkup(keyboard=kb_12 , resize_keyboard=True)
         await message.answer('Вот список , выбирай',reply_markup=keyboard_12)



#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)

########################################################################################################################################################         
    if (message.text == "Необъятный океан🌊"):
          name = 'Необъятный океан'
          site_url='https://rezka.ag/animation/adventures/28185-neobyatnyy-okean-2018.html'
          description = 'Иори Катихара ужасно боится воды, у него развилась настоящая фобия, от которой парень никак не может избавиться. И так случилось, что герой аниме поступил в университет, который и расположился на побережье. Там он снимает комнату у семейства Котегава, члены которого владеют магазином снаряжения для дайвинга. Со временем Иори познакомится с веселыми парнями-дайверы, которые постараются изменить его приоритеты. Новые приятели считают, что Катихара обязательно должен испытать чувство при погружении на самую глубину и наслаждения подводными пейзажами!'
          rating = '9.37/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/bcfaad3238200yj75s27i.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Госпожа кагуя:В любви как на войне"):
          name = 'Госпожа кагуя:В любви как на войне'
          site_url='https://rezka.ag/animation/comedy/29627-gospozha-kaguya-v-lyubvi-kak-na-voyne-tv-1-2019.html'
          description = 'Кагуя Шиномия — красивая и умная девушка из богатой семьи, которая учится в одной из самых престижных школ страны. Будучи вице-президентом школьного совета, Кагуя работает вместе с президентом Миюки Широгане — лучшим учеником в школе. Из-за этого многие считают их идеальной парой, хотя между ними нет романтических отношений. На самом деле Кагуя и Миюки уже давно питают друг к другу чувства, просто они слишком горды, чтобы признать свою любовь первыми. Поэтому герои решают сделать все возможное, чтобы добиться признания от другого, запустив настоящую любовную битву.'
          rating = '9.16/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/m1de637de7ef0kn63z42c.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Гинтама"):
          name = 'Гинтама'
          site_url='https://rezka.ag/animation/comedy/11038-gintama-tv-1-2006.html'
          description = 'В середине XIX столетия Япония, уже несколько веков живущая в изоляции от всего мира, сталкивается с вторжением космических пришельцев, которые подчиняют себе сегунат, а всех самураев разоружают и превращают в обыкновенных рабочих. Во главе истории находится молодой и эксцентричный самурай Гинтоки Саката, прозванный за свои серебристые волосы и храбрость в бою Белым Демоном. Чтобы выживать в новом мире, он берется за любую работу, из-за чего нередко оказывается втянут в опасные приключения вместе со своими спутниками, учеником Симпати Симурой и инопланетной девушкой Кагурой.'
          rating = '8.69/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/2/9/waec8af1ce7d8ci37e68b.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Крутой учитель Онидзука"):
          name = 'Крутой учитель Онидзука'
          site_url='https://rezka.ag/animation/comedy/20767-krutoy-uchitel-onidzuka-1999.html'
          description = 'Онидзука — экс-лидер банды байкеров, мечтающий стать великим учителем. Проходя стажировку в рамках обучения, мужчина попадает не в класс для девочек, как он хотел, а в класс для правонарушителей. Здесь Онидзука узнает о важности умения находить общий язык даже с отъявленными хулиганами и уважать их принципы. После стажировки, благодаря блестящей харизме и амбициям, герой получает возможность работать в одной из самых престижных школ в Японии, в которой ему предстоит заниматься «проблемным» классом. Очень скоро Онидзука начинает осознавать, что он способен решить любую проблему в школе с помощью непреклонного характера и авторитета, но он хочет найти правильный подход к каждому ученику…'
          rating = '9.62/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/17/ye84e6bbafa43ua36c59r.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Этот герой неуязвим но очень осторожен"):
          name = 'Этот герой неуязвим но очень осторожен'
          site_url='https://rezka.ag/animation/adventures/34976-etot-geroy-neuyazvim-no-ochen-ostorozhen-2019.html'
          description = 'В жестоком мире Геабуранде обитает богиня Листарте. Она является отважной воительницей и спасительницей. Но даже такая сильная особа не откажется от помощника и Листарте приходится вызвать себе на подмогу героя. Им оказывается заядлый геймер Сэйя Рюгуин. Парень был продвинутым игроком, но обладал парадоксальной осторожностью при начинании любого дела. Чрезмерная бдительность заставила его купить аж три комплекта боевых доспехов. Один из них он принялся носить, второй оставил на запас, собственно и третий предназначался для перестраховки. Большую часть времени Сэйя тратил на физические упражнения, дабы развить силу и выносливость. Причем он редко и из дома-то выходит, так что времени у парня валом, чтобы отточить свои навыки.'
          rating = '8.79/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/u73c58c05468ess13j92h.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Ванпачмен🥊"):
          name = 'Ванпачмен'
          site_url='https://rezka.ag/animation/comedy/11494-vanpanchmen-tv-1-2015.html'
          description = 'Действие фантастического мультсериала «Ванпанчмен» происходит в альтернативном мире, который иронично похож на наш. Здесь существует огромное множество всевозможных враждебно настроенных существ, многие из которых поражают своими размерами, и способны за раз уничтожить целый жилой квартал. Но кроме них в этом невероятном мире также живут и супергерои, яро сражающиеся за добро и справедливость. К ним относится и двадцатипятилетний юноша по имени Сайтама. Увидев впервые этого лысого неприметного паренька вряд ли можно поверить в то, что он обладает невероятной силой..'
          rating = '9.47/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2021/11/14/x3093b347f21akm15h83p.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Школа строгого режима"):
          name = 'Школа строгого режима'
          site_url='https://rezka.ag/animation/comedy/22519-shkola-strogogo-rezhima-2015.html'
          description = 'Хатимицу – частная женская школа, где со времени основания не ступала мужская нога. Правда, девушки, учащиеся здесь, отнюдь не праведницы и не ангелы, а скорее наоборот – демоны в людском обличии. Между ученицами уже довольно длительное время идет война, в которой общество разделилось на два лагеря: один возглавляет председатель студенческого совета, а второй – дочка директора учреждения. Вот только девчонкам придется на время забыть о конфронтации, так как со школой произошло удивительное событие.'
          rating = '9.21/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/11/16/vb7c436d1ef5aww31q18h.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Моб психо 100"):
          name = 'Моб психо 100'
          site_url='https://rezka.ag/animation/comedy/17734-mob-psiho-100-tv-1-2016.html'
          description = 'Молодой паренёк Кагэяма Сигео по прозвищу «Моб» — неуверенный в себе школьник, обладающий невероятно сильными экстрасенсорными способностями. Еще в детстве наш герой мог без труда сгибать ложки, а также поднимать довольно тяжелые предметы в воздух при помощи силы мысли, за что его и невзлюбили окружающие. Такая реакция обычных людей заставила Кагэяму научиться сдерживаться и без надобности не применять экстрасенсорные способности на публике. И теперь превратившись в робкого закомплексованного парня, наш герой в свободное от учебы время за весьма скромную плату подрабатывает у местного «экстрасенса» Аратаки Рэйгэна, являющегося не более чем обычным шарлатаном.'
          rating = '9.48/10'
          mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
          await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/2/12/nb5dc2f85a136gt15r43b.jpg')
          await bot.send_message(message.from_user.id, mes, parse_mode="html")


    if(message.text == "Комедия"):
         await message.answer("Окей сейчас найдем тебе что-то")
         anime_13 = {
               1: 'Необъятный океан🌊', 
               2: 'Госпожа кагуя:В любви как на войне', 
               3: 'Гинтама', 
               4: 'Крутой учитель Онидзука', 
               5: 'Этот герой неуязвим но очень осторожен',
               6: 'Ванпачмен🥊',
               7: 'Школа строгого режима',
               8: 'Невероятные приключения ДжоДжо',
               9: 'Очень приятно, Бог',
               10: 'Моб психо 100'
               
         }
         await message.answer(f'1:{anime_13[1]}\n2:{anime_13[2]}\n3:{anime_13[3]}\n5:{anime_13[5]}\n6:{anime_13[6]}\n7:{anime_13[7]}\n8:{anime_13[8]}\n9:{anime_13[9]}\n10:{anime_13[10]}')   
         kb_13 = [    
                [types.KeyboardButton("Необъятный океан🌊")],
                [types.KeyboardButton("Госпожа кагуя:В любви как на войне")],
                [types.KeyboardButton("Гинтама")],
                [types.KeyboardButton("Крутой учитель Онидзука")],
                [types.KeyboardButton("Этот герой неуязвим но очень осторожен")],
                [types.KeyboardButton("Ванпачмен🥊")],
                [types.KeyboardButton("Школа строгого режима")],
                [types.KeyboardButton("Невероятные приключения ДжоДжо")],
                [types.KeyboardButton("Очень приятно, Бог")],
                [types.KeyboardButton("Моб психо 100")],
                [types.KeyboardButton("⬅️Назад")],
      ]   
         keyboard_13 = types.ReplyKeyboardMarkup(keyboard=kb_13 , resize_keyboard=True)
         await message.answer('Вот список , выбирай',reply_markup=keyboard_13)
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)



#######################################################################################################################################


    if (message.text == "Лагерь на свежем воздухе"):
            name = 'Лагерь на свежем воздухе'
            site_url='https://rezka.ag/animation/comedy/30485-lager-na-svezhem-vozduhe-tv-1-2018.html'
            description = 'Старшеклассница Рин обожает туризм и предпочитает отдыхать в одиночестве. Во время очередного похода она встречает странную девушку, которая отправилась в горы без должной подготовки и экипировки. Вскоре выясняется, что ее зовут Надешико, и она решила взглянуть на Фудзи, однако быстро выбилась из сил и заблудилась. Рин накормила бедняжку горячим раменом и позволила погреться у костра, а затем помогла вернуться домой. Девушки и представить не могли, что их встреча окажется судьбоносной, ведь впереди их ждет множество совместных походов, которые принесут им море незабываемых эмоций и ярких приключений...'
            rating = '8.9/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2020/12/26/a03bc73c4f0cafx51p40s.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Мой братик теперь не братик!"):
            name = 'Мой братик теперь не братик!'
            site_url='https://rezka.ag/animation/comedy/54183-moy-bratik-teper-ne-bratik-2023.html'
            description = 'Махиро Ояма — обычный паренек, которому нравится проводить свободное время, играя в виртуальные игры. Его младшая сестра Михари — целеустремленная девушка-подросток с отличными техническими навыками, занимающаяся работой над собственными изобретениями. Однажды Михари решает провести эксперимент, где подопытным выступает ее родной брат. Когда ситуация выходит из-под контроля, неудачный опыт превращает Махиро в привлекательную девушку. Теперь, оказавшись в необычной ситуации, Махиро должен вести совершенно нетипичный для него образ жизни, завести новых друзей и найти способ того, как вернуться в свое тело.'
            rating = '7.49/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/1/5/c68f4fe8110beax76v22w.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")
    if (message.text == "Магазинчик сладостей🍬"):
            name = 'Магазинчик сладостей'
            site_url='https://rezka.ag/animation/comedy/12501-magazinchik-sladostey-tv-1-2016.html'
            description = 'Прошло немало лет, как семья Сикада впервые открыла свой магазинчик сладостей, с тех пор, на протяжении восьми поколений, её потомки продолжают развивать семейное дело. Овдовевший Йо Сикада, нынешний владелец лавки, – человек очень известный и уважаемый в родном поселении, вот только годы идут, а его единственный сын Коконоцу, на которого отец возлагает большие надежды, совсем не хочет вникать в семейный бизнес, предпочитая увлекаться рисованием модной манги. Поэтому всё свободное время паренёк самозабвенно портит бумагу, периодически отправляясь гулять со своими друзьями.'
            rating = '8.65/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/12/28/dee3294b52110iz88i52i.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")  
    if (message.text == "Не издевайся, Нагаторо"):
            name = 'Не издевайся, Нагаторо'
            site_url='https://rezka.ag/animation/comedy/38785-ne-izdevaysya-nagatoro-tv-1-2021.html'
            description = 'Замкнутый, ранимый и застенчивый старшеклассник Наото Хатиодзи знакомится со вспыльчивой и самоуверенной Хаясе Нагаторо, которая только перевелась в старшую школу. С этого момента мирная и спокойная жизнь Наото переворачивается с ног на голову, поскольку Нагаторо использует любую представившуюся возможность, чтобы запугивать, дразнить и даже доводить до слез робкого старшеклассника. Однако с течением времени становится очевидным, что поведение Нагаторо на самом деле является защитной реакцией, ведь она испытывает романтический интерес к Наото…'
            rating = '8.42/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/1/8/f4782d631a89cfq54j91v.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Одинокий рокер!🎸"):
            name = 'Одинокий рокер!'
            site_url='https://rezka.ag/animation/comedy/52261-odinokiy-roker-2022.html'
            description = 'Мечтающая в будущем играть в музыкальной группе, старшеклассница Хитори Гото взялась за уроки игры на гитаре. Ничего не мешает исполнению её мечты, кроме самой Хитори, которая настолько застенчива и зажата, что не смогла завести ни одного друга, чего уж говорить о создании собственного музыкального коллектива. Сама судьба решает помочь Хитори, и та, на своё счастье, встречает Нидзику Идзити, которая играет на ударных в собственной группе и как раз подыскивает гитаристку!'
            rating = '9.03/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/10/10/qd94b04faab7fqt87q53e.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Городская дьяволица"):
            name = 'Городская дьяволица'
            site_url='https://rezka.ag/animation/fantasy/47921-gorodskaya-dyavolica-tv-1-2019.html'
            description = 'Ёсида Юко была обычной школьницей, пока Лилит не пробудила ее скрытые демонические силы! Теперь она настоящая батарейка энерджайзер с рогами и хвостом, а зовут ее Хозяйка Теней Юко. И ей предстоит победить другое волшебное создание — жрицу храма Клана Света по имени Тиёда Момо, которая ходит с ней в одну школу. Но быть демонической девочкой-волшебницей не так-то просто, и Юко предстоит многому научиться, прежде чем она сможет исполнить свое предназначение и одолеть Клан Света.'
            rating = '7.92/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/6/19/sb6a2ba1ac0d9kz44z10p.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if (message.text == "Дэаимон"):
            name = 'Дэаимон'
            site_url='https://rezka.ag/animation/everyday/47999-deaimon-2022.html'
            description = 'Впервые за десять лет Нагому Ирино возвращается домой в Киото, когда его отец попадает в больницу. Нагому очень хочет возглавить семейную кондитерскую «Рёкусё», но вместо этого его просят опекать Ицуки Юкихиру — девочку, которую все называют преемницей.'
            rating = '8.59/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2022/4/7/occ080ec67a0acw69h89w.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")

    if(message.text == "Повседневность"):
         await message.answer("Окей сейчас найдем тебе что-то")        
         anime_14 = {
               1: 'Тетрадь дружбы Нацумэ', 
               2: 'Лагерь на свежем воздухе', 
               3: 'Не издевайся, Нагаторо', 
               4: 'Мой братик теперь не братик!', 
               5: 'Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня',
               6: 'Одинокий рокер!🎸',
               7: 'Повелитель тьмы на подработке!',
               8: 'Городская дьяволица',
               9: 'Дэаимон',
               10:'Магазинчик сладостей🍬'
         }
         await message.answer(f'1:{anime_14[1]}\n2:{anime_14[2]}\n3:{anime_14[3]}\n5:{anime_14[5]}\n6:{anime_14[6]}\n7:{anime_14[7]}\n8:{anime_14[8]}\n9:{anime_14[9]}\n10:{anime_14[10]}')   
         kb_14 = [    
                [types.KeyboardButton("Тетрадь дружбы Нацумэ")],
                [types.KeyboardButton("Лагерь на свежем воздухе")],
                [types.KeyboardButton("Не издевайся, Нагаторо")],
                [types.KeyboardButton("Мой братик теперь не братик!")],
                [types.KeyboardButton("Убивая слизней 300 лет, сама того не заметив, я достигла максимального уровня")],
                [types.KeyboardButton("Одинокий рокер!🎸")],
                [types.KeyboardButton("Повелитель тьмы на подработке!")],
                [types.KeyboardButton("Городская дьяволица")],
                [types.KeyboardButton("Дэаимон")],
                [types.KeyboardButton("Магазинчик сладостей🍬")],
                [types.KeyboardButton("⬅️Назад")],
      ]   
         keyboard_14 = types.ReplyKeyboardMarkup(keyboard=kb_14 , resize_keyboard=True)
         await message.answer('Вот список , выбирай',reply_markup=keyboard_14)   
#     if (message.text == "⬅️Назад"):
#             kb = [
          
#                [types.KeyboardButton("Боевик")],
#                [types.KeyboardButton("Сёнэн")],
#                [types.KeyboardButton("Боевые искуства")],
#                [types.KeyboardButton("Военные")],
#                [types.KeyboardButton("Гарем")],
#                [types.KeyboardButton("Демоны")],
#                [types.KeyboardButton("Детектив")],
#                [types.KeyboardButton("Драма")],
#                [types.KeyboardButton("Приключения")], 
#                [types.KeyboardButton("Исекай")],
#                [types.KeyboardButton("Киберпанк")],
#                [types.KeyboardButton("Спокон")],
#                [types.KeyboardButton("Комедия")],
#                [types.KeyboardButton("Повседневность")], 
#                [types.KeyboardButton("Фантастика")],
          
#      ]
#             keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
#             await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)



    if (message.text == "Триган: Ураган🌪️"):
            name = 'Триган: Ураган'
            site_url='https://rezka.ag/animation/fiction/54232-trigan-uragan-2023.html'
            description = 'Сюжет следит за приключениями таинственного молодого стрелка Вэша по прозвищу Ураган, который бежит от своего темного прошлого. Считая себя пацифистом и просто хорошим парнем, Вэш старается всегда сохранять жизнь своим противникам, тем не менее он является одним из самых разыскиваемых преступников планеты, за голову которого назначена астрономическая награда. Скрываясь на пустынной планете от бесчисленных охотников за головами, главный герой встречает неожиданных союзников, начинающую журналистку Мерил Страйф и ее коллегу Роберто Де Ниро.'
            rating = '7.67/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2023/1/7/r995970285155sq21c18s.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")  

    if (message.text == "Черная пуля⚫🔫"):
            name = 'Черная пуля'
            site_url='https://rezka.ag/animation/drama/20147-chernaya-pulya.html'
            description = 'Недалекое будущее, человеческая цивилизация встретилась с непреодолимой опасностью, коварным вирусом Гастрея, который, попадая в организм, превращал человека в ужасное чудовище, стремящееся заразить как можно больше людей. Эпидемия мгновенно распространилась по планете, не зараженных осталось совсем немного, они сумели укрыться на небольшой территории, огражденной стеной, сквозь специально разработанный материал вирус проникнуть не мог.'
            rating = '9.21/10'
            mes = f"Название : {name}\nСайт с аниме: {site_url}\nПро аниме: {description}\nРейтинг:{rating}" 
            await bot.send_photo(message.from_user.id ,'https://static.hdrezka.ac/i/2016/10/5/db2dcf658be60ey49b22k.jpg')
            await bot.send_message(message.from_user.id, mes, parse_mode="html")                 
          
    if(message.text == "Фантастика"):
         await message.answer("Окей сейчас найдем тебе что-то")         
         anime_15 = {
                  1:"Стальной Алхимик:братство⚗️",
                  2:"Триган: Ураган🌪️",
                  3:"Ковбой Бибоп🤠",
                  4:"Наруто🍜",
                  5:"Атака титанов🤺",
                  6:"Гуррен-Лаганн",
                  7:"Евангелион",
                  8:"Черная пуля⚫🔫",
                  9:"Врата: там бьются наши воины",
                  10:"Покемон" 

         }
         await message.answer(f'1:{anime_15[1]}\n2:{anime_15[2]}\n3:{anime_15[3]}\n5:{anime_15[5]}\n6:{anime_15[6]}\n7:{anime_15[7]}\n8:{anime_15[8]}\n9:{anime_15[9]}\n10:{anime_15[10]}')   
         kb_15 = [    
                [types.KeyboardButton("Стальной Алхимик:братство⚗️")],
                [types.KeyboardButton("Триган: Ураган🌪️")],
                [types.KeyboardButton("Ковбой Бибоп🤠")],
                [types.KeyboardButton("Наруто🍜")],
                [types.KeyboardButton("Атака титанов🤺")],
                [types.KeyboardButton("Гуррен-Лаганн")],
                [types.KeyboardButton("Евангелион")],
                [types.KeyboardButton("Черная пуля⚫🔫")],
                [types.KeyboardButton("Врата: там бьются наши воины")],
                [types.KeyboardButton("Покемон")],
                [types.KeyboardButton("⬅️Назад")],

      ]   
         keyboard_15 = types.ReplyKeyboardMarkup(keyboard=kb_15 , resize_keyboard=True)
         await message.answer('Вот список , выбирай',reply_markup=keyboard_15)
    if (message.text == "⬅️Назад"):
            kb = [
          
               [types.KeyboardButton("Боевик")],
               [types.KeyboardButton("Сёнэн")],
               [types.KeyboardButton("Боевые искуства")],
               [types.KeyboardButton("Военные")],
               [types.KeyboardButton("Гарем")],
               [types.KeyboardButton("Демоны")],
               [types.KeyboardButton("Детектив")],
               [types.KeyboardButton("Драма")],
               [types.KeyboardButton("Приключения")], 
               [types.KeyboardButton("Исекай")],
               [types.KeyboardButton("Киберпанк")],
               [types.KeyboardButton("Спокон")],
               [types.KeyboardButton("Комедия")],
               [types.KeyboardButton("Повседневность")], 
               [types.KeyboardButton("Фантастика")],
          
     ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb , resize_keyboard=True, selective=True)
            await message.answer('Какой жанр аниме тебе нравится?', reply_markup=keyboard)    
          
          
if __name__ == '__main__':
    executor.start_polling(dp)     
