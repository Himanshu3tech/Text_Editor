from win32com.client import Dispatch
import requests
import json
import time

from tkinter import *
from PIL import Image,ImageTk



speaker=Dispatch("SAPI.SpVoice")


 

def buisness():
    url_ = "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
    response = requests.get(url_).text
    news_json = json.loads(response)
    news = news_json['articles']
    speaker.speak("BUISNESS RELATED NEWS ARE AS FOLLOWS : ")
    for x in news:
        print(x['title'])
        print(x['description'])
        speaker.speak(x['title'])
        speaker.speak(x['description'])
        print()
        print(x['url'])
        speaker.speak("FOR DETAILS MOVE TO THE PROVIDED LINK  ")
        time.sleep(1)
        speaker.speak("lets move to next news")
        time.sleep(1)
        print()


def technology():
    url_ = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
    response = requests.get(url_).text
    news_json = json.loads(response)
    news = news_json['articles']
    speaker.speak("TECHNOLOGY RELATED NEWS ARE AS FOLLOWS : ")
    for x in news:
        print(x['title'])
        print(x['description'])
        speaker.speak(x['title'])
        speaker.speak(x['description'])
        print()
        print(x['url'])
        speaker.speak("FOR DETAILS MOVE TO THE PROVIDED LINK  ")
        time.sleep(1)
        speaker.speak("lets move to next news")
        time.sleep(1)
        print()


def sports():
    url_ = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
    response = requests.get(url_).text
    news_json = json.loads(response)
    news = news_json['articles']
    speaker.speak("SPORTS RELATED NEWS ARE AS FOLLOWS : ")
    for x in news:
        print(x['title'])
        print(x['description'])
        speaker.speak(x['title'])
        speaker.speak(x['description'])
        print()
        print(x['url'])
        speaker.speak("FOR DETAILS MOVE TO THE PROVIDED LINK  ")
        time.sleep(1)
        speaker.speak("lets move to next news")
        time.sleep(1)
        print()



def health():
    url_ = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
    response = requests.get(url_).text
    news_json = json.loads(response)
    news = news_json['articles']
    speaker.speak("HEALTH RELATED NEWS ARE AS FOLLOWS : ")
    for x in news:
        print(x['title'])
        print(x['description'])
        speaker.speak(x['title'])
        speaker.speak(x['description'])
        print()
        print(x['url'])
        speaker.speak("FOR DETAILS MOVE TO THE PROVIDED LINK  ")
        time.sleep(1)
        speaker.speak("lets move to next news")
        time.sleep(1)
        print()




def entertainment():
    url_ = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
    response = requests.get(url_).text
    news_json = json.loads(response)
    news = news_json['articles']
    speaker.speak("ENTERTAINMENT RELATED NEWS ARE AS FOLLOWS : ")
    for x in news:
        print(x['title'])
        print(x['description'])
        speaker.speak(x['title'])
        speaker.speak(x['description'])
        print()
        print(x['url'])
        speaker.speak("FOR DETAILS MOVE TO THE PROVIDED LINK  ")
        time.sleep(1)
        speaker.speak("lets move to next news")
        time.sleep(1)
        print()




def science():
    url_ = "http://newsapi.org/v2/top-headlines?country=in&category=science&category=bus&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
    response = requests.get(url_).text
    news_json = json.loads(response)
    news = news_json['articles']
    speaker.speak("SCIENCE RELATED NEWS ARE AS FOLLOWS : ")
    for x in news:
        print(x['title'])
        print(x['description'])
        speaker.speak(x['title'])
        speaker.speak(x['description'])
        print()
        print(x['url'])
        speaker.speak("FOR DETAILS MOVE TO THE PROVIDED LINK  ")
        time.sleep(1)
        speaker.speak("lets move to next news")
        time.sleep(1)
        print()



def choice(n):
    if(n==1):
        buisness()
    elif(n==2):
        technology()
    elif(n==3):
        sports()
    elif(n==4):
        health()
    elif(n==5):
        science()
    elif(n==6):
        entertainment()
    else:exit()

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x600")
    root.wm_maxsize(600, 600)
    image = Image.open("3.jpg")
    photo = ImageTk.PhotoImage(image)
    image_label = Label(image=photo)
    image_label.pack()
    root.mainloop()
    print()
    print("""                                  WHICH NEWS YOU WANT TO READ ?              
                               CHOOSE ACCORDING TO YOUR INTEREST         """)
    time.sleep(1)
    speaker.speak("welcome himanshu your news portal is ready ")
    speaker.speak("WHICH NEWS YOU WANT TO READ CHOOSE ACCORDING TO YOUR INTEREST")
    ch='y'
    while(ch=='y'):
        print("""    
                      1.BUISNESS
                      2.TECHNOLOGY
                      3.SPORTS
                      4.HEALTH
                      5.SCIENCE
                      6.ENTERTAINMENT  """)
        a=int(input())
        choice(a)
        print("DO YOU WANT TO CONTINUE ")
        ch=input()

    exit()


