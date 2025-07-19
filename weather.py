import requests
def get_weather(city_name):
    API_KEY = "02115afc2754cfcf66aa986510fe0016"
    ##get api key from https://home.openweathermap.org/api_keys
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_name.lower()

    params = {
        'APPID': API_KEY,
        'q': city_name,
        'units': 'metric',
        'lang': 'bn'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"\n{city_name} এর বর্তমান তাপমাত্রাঃ {temperature} ডিগ্রি সেলসিয়াস")
        print(f"আবহাওয়ার ধরনঃ {description}")
    else:
        print("শহরের নাম সঠিক নয় অথবা ডাটা পাওয়া যায় নাই")

city = input("আপনার শহরের নাম লিখুনঃ ")
get_weather(city)