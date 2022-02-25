import socket
import email
from ipaddress import ip_address
from unittest import result
import requests
import wikipedia
import pywhatkit as kit
import smtplib
from decouple import config
from bs4 import BeautifulSoup
import re
import pyjokes


#-----------Define the API Keys-------------
NEWS_API_KEY="e4173478eeaa4cb79a141ce050f6d658"  #To fetch the latest news headlines, we'll be using NewsAPI. Signup for a free account on NewsAPI and get the API Key.
OPENWEATHER_APP_ID="a294cdef05c2e9cf2c5a7164ca4a4851"  #To get the weather report, we're using the OpenWeatherMap API. Signup for a free account and get the APP ID.
'''TMDB_API_KEY=config("TMDB_API_KEY")
EMAIL=config('EMAIL')
PASSWORD=config('PASSWORD')'''

#------------Functions----------------------
def find_my_ip():
    hostname=socket.gethostname()
    ip_addr=socket.gethostbyname(hostname)
    return ip_addr

def search_on_wikipedia(query):
    results=wikipedia.summary(query,sentences=2)
    return results

def play_on_yt(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_wts_msg(number,msg):
    kit.sendwhatmsg_instantly(f"+91{number}",msg)

'''def send_email(recv_addr,sub,msg):
    try:
        email = EmailMessage()
        email['To'] = recv_addr
        email['Subject'] = sub
        email['From'] = EMAIL
        email.set_content(msg)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False'''

def get_latest_news():
    news_headlines=[]
    res=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles=res['articles']
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def get_weather_news(city):
    res=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather=res["weather"][0]["main"]
    temp=res["main"]["temp"]
    feels_like=res["main"]["feels_like"]
    return weather,f"{temp}℃", f"{feels_like}℃"

def get_top_IMDB_movies():
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movies = soup.select('td.titleColumn')
    #links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    #crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    #ratings = [b.attrs.get('data-value')
            #for b in soup.select('td.posterColumn span[name=ir]')]
    #votes = [b.attrs.get('data-value')
         #for b in soup.select('td.ratingColumn strong')]
    list = []
    list = []
    for index in range(0, len(movies)):
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        #year = re.search('\((.*?)\)', movie_string).group(1)
        #place = movie[:len(str(index))-(len(movie))]
        list.append(movie_title)
    '''for movie in list:
        print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
              ') -', 'Starring:', movie['star_cast'], movie['rating'])'''
    return list

def get_random_joke():
    lol=pyjokes.get_jokes(language='en',category='neutral')
    return lol

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']