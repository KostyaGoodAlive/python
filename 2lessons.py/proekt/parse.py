import requests 
from bs4 import BeautifulSoup 
 
 
def anime_getting(anime_title: str): 
    response = requests.get('https://animego.org/anime') 
    soup = BeautifulSoup(response.content, 'html.parser') 
    animes_soup = soup.select('.animes-list-item') 
    result=[] 
 
    for anime in animes_soup: 
        name = anime.select_one('.media-body > .h5').text 
         
        url = anime.select_one('.media-body > .h5 > a').get('href') 
    
        genre = anime.select_one('.mb-2 > .anime-genre ').text.strip().replace('\n', '').replace('                                                     ', ' ').replace('                                                     ', ' ').replace('\u2060', '') 
        description = anime.select_one('.description').text.strip().replace('\n', '').replace('                                                     ', ' ').replace('                                                     ', ' ').replace('\u2060', '') 
 
        anime_obj = { 
            "name": name, 
            "genre": genre, 
            "description": description, 
            "url": url 
        }  

        anime_name = anime_obj['name']
        
        if anime_name.lower() == anime_title:
            result.append(anime_obj) 

    return result     
 


# def anime_news(): 
#     response = requests.get('https://suspilne.media/tag/anime/') 
#     soup = BeautifulSoup(response.content, 'html.parser') 
#     news_soup = soup.select_one('.c-article-card')
#     result=[]

#     description = news_soup.text.strip().replace('\n', '  ').replace('                                                     ', ' ').replace('\u2060', '') 
    
#     anime_news = {
#         'description': description
#     }
#     result.append(anime_news)

#     return result
# print(anime_news())



def anime_news(): 
    response = requests.get('https://animag.ru/news') 
    soup = BeautifulSoup(response.content, 'html.parser') 
    news_soup = soup.select('.col-sm-9')
    result=[]
# > h3 > a')
# .field-content > span')
# > col-md-5')
    for news in news_soup:
        title = news.select_one('.views-field > h3 ').text
        description = news.select_one('.views-field > span > p').text
        time = news.select_one('.col-md-5').text
        anime_news = {
                'title': title,
                'description': description,
                'time':time
            }
        result.append(anime_news)
    return result
