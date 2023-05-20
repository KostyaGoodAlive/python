import requests
def parse_weather(city: str):
 
    api_key = '8e1be73c67e1efe0775888eea53cd0fa'
    url = f"https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&q={city}"
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':

    city = input("Enter your city: ")
    weather = parse_weather(city)['main']
    temp = weather['temp'] - 273.15
    print(f"City - {city}\nTemperature - {temp}")
    print(parse_weather('Kyiv')['main'])

