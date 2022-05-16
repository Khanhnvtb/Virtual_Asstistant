import webbrowser as wb
from youtube_search import YoutubeSearch
import requests
import smtplib
from datetime import datetime
import wikipedia
from geopy.geocoders import Nominatim
from geopy.distance import great_circle


def solveGoogle(lg, search):
    if lg == 'en':
        url = f'https://www.google.com/search?q={search}'
        wb.get().open(url)
        return f'Here is your {search} on google'
    else:
        url = f'https://www.google.com/search?q={search}'
        wb.get().open(url)
        return f'Đây là kết quả {search} trên google'


def solveYoutube(lg, search):
    if lg == 'en':
        url = f'https://www.youtube.com/search?q={search}'
        wb.get().open(url)
        return f'Here is your {search} on youtube'
    else:
        url = f'https://www.youtube.com/search?q={search}'
        wb.get().open(url)
        return f'Đây là kết quả {search} trên youtube'


def play_song(lg, song):
    if lg == 'vi':
        while True:
            result = YoutubeSearch(song, max_results=10).to_dict()
            if result:
                break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        wb.get().open(url)
        return "Bài hát bạn yêu cầu đã được mở."
    else:
        while True:
            result = YoutubeSearch(song, max_results=10).to_dict()
            if result:
                break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        wb.get().open(url)
        return "The requested song has been opened"


def current_weather(lg, city):
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] == "404":
        if lg == 'vi':
            return "Không tìm thấy địa chỉ của bạn vui lòng thử lại!"
        else:
            return "Can not find your address, pleasee try again"

    city_res = data["main"]
    current_temperature = city_res["temp"]
    current_pressure = city_res["pressure"]
    current_humidity = city_res["humidity"]
    suntime = data["sys"]
    sunrise = datetime.fromtimestamp(suntime["sunrise"])
    sunset = datetime.fromtimestamp(suntime["sunset"])
    wthr = data["weather"]
    weather_description = wthr[0]["description"]
    now = datetime.now()
    content = """
    Hôm nay là ngày {day} tháng {month} năm {year}.
    Mặt trời mọc vào {hourrise} giờ {minrise} phút.
    Mặt trời lặn vào {hourset} giờ {minset} phút.
    Nhiệt độ trung bình là {temp} độ C.
    Áp suất không khí là {pressure} héc tơ Pascal.
    Độ ẩm là {humidity}%.
    Trời  quang mây, tầm nhìn xa từ nhà xuống bếp.""".format(day=now.day, month=now.month, year=now.year,
                                                             hourrise=sunrise.hour, minrise=sunrise.minute,
                                                             hourset=sunset.hour, minset=sunset.minute,
                                                             temp=current_temperature, pressure=current_pressure,
                                                             humidity=current_humidity)
    content2 = """
        Today is {day} {month} {year}.
        Sunrise in {hourrise} a.m {minrise} minute.
        Sunset in {hourset} p.m {minset} minute.
        The avarge temperature is {temp} poison.
        The air pressure is {pressure} hectare pascal.
        Humidity is {humidity}%.
        Have a great day boss!!!""".format(day=now.day, month=now.month, year=now.year, hourrise=sunrise.hour,
                                           minrise=sunrise.minute,
                                           hourset=sunset.hour, minset=sunset.minute,
                                           temp=current_temperature, pressure=current_pressure,
                                           humidity=current_humidity)
    if lg == 'en':
        return content2
    else:
        return content


def read_news(lg):
    wb.open("https://vnexpress.net/tin-tuc-24h")
    if lg == 'vi':
        return "Đây là trang tin tức mới nhất"
    else:
        return "This is the news"


def send_email(lg, user, content):
    dic = {'khánh': 'khanhtb.1012@gmail.com',
           'huy': 'pqhuy27122000@gmail.com'}

    if user in dic.keys():

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        # tài khoản, mật khẩu
        mail.login('khanhtb.1012@gmail.com', 'password')
        mail.sendmail('khanhtb.1012@gmail.com',  # tài khoản gửi
                      dic.get(user), content.encode('utf-8'))
        mail.close()
        if lg == 'en':
            return 'Your email has just been sent. Please check your email again'
        else:
            return "Email của bạn vừa được gửi. Bạn check lại email nhé hihi."
    else:
        if lg == 'en':
            return "The bot doesn't understand who you want to email. Can you repeat"
        else:
            return 'Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?'


def tell_me_about(lg, text):
    try:
        wikipedia.set_lang(lg)

        contents = wikipedia.summary(text).split('.')
        return contents
    except:
        if lg == 'en':
            return "The bot doesn't define your term. Please say it again"
        else:
            return "Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại"


def maps(text):
    text = text.replace('maps', '')
    text = text.replace('map', '')
    text = text.replace('google', '')
    return text
    wb.open('https://www.google.com/maps/place/' + text)


def giveDirections(lg, startingPoint, destinationPoint):
    try:
        geolocator = Nominatim(user_agent='assistant')
        if 'current' in startingPoint:
            res = requests.get("https://ipinfo.io/")
            data = res.json()
            startinglocation = geolocator.reverse(data['loc'])
        else:
            startinglocation = geolocator.geocode(startingPoint)

        destinationlocation = geolocator.geocode(destinationPoint)
        startingPoint = startinglocation.address.replace(' ', '+')
        destinationPoint = destinationlocation.address.replace(' ', '+')

        wb.open('https://www.google.co.in/maps/dir/' +
                startingPoint + '/' + destinationPoint + '/')

        startinglocationCoordinate = (
            startinglocation.latitude, startinglocation.longitude)
        destinationlocationCoordinate = (
            destinationlocation.latitude, destinationlocation.longitude)
        total_distance = great_circle(
            startinglocationCoordinate, destinationlocationCoordinate).km  # .mile
        res = str(round(total_distance, 2))
        if lg == 'vi':
            return res + 'ki lô mét'
        else:
            return res + 'kilomet'
    except:
        if lg == 'vi':
            return "Tôi nghĩ địa điểm không phù hợp"
        else:
            return "I think location is not proper, Try Again!"
