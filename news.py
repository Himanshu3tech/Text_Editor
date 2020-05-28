import multiprocessing
from tkinter import *
from win32com.client import Dispatch
from PIL import Image,ImageTk
import datetime
import requests
import json
speaker=Dispatch("SAPI.SpVoice")



def mainspeak(var,null):
    for x in var:
            speaker.speak(x['title'])
            speaker.speak("..description.")
            speaker.speak(x['description'])
            speaker.speak("for more please move to the provided link")




def speak3():

    speaker.speak("todays news are as follows...")

def entertainment(widget):
    widget.delete(1.0,END)
    root.update()
    P2=multiprocessing.Process(target=speak3)
    try:
        url_ = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
        response = requests.get(url_).text
        news_json = json.loads(response)
        news = news_json['articles']
        P2.start()
        P2.join()
    except:
        speaker.speak("THERE IS some problem  IN YOUR INTERNET CONNECTION.. PLEASE CHECK It AND TRY AGAIN")
        root.destroy()
    for x in news:
        widget.insert(END, x['title'])
        widget.insert(END, '\n')
        widget.insert(END, "DESCRIPTION: ")
        widget.insert(END, x['description'])
        widget.insert(END, '\nURL: ')
        widget.insert(END, x['url'])
        widget.insert(END, '\n\n')
        root.update()
    root.update()
    p3 = multiprocessing.Process(target=mainspeak, args=(news, 0))
    p3.start()
    root.update()

def science(widget):
    widget.delete(1.0, END)
    root.update()
    P2 = multiprocessing.Process(target=speak3)
    try:
        url_ = "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
        response = requests.get(url_).text
        news_json = json.loads(response)
        news = news_json['articles']
        P2.start()
        P2.join()
    except:
        speaker.speak("THERE IS some problem  IN YOUR INTERNET CONNECTION.. PLEASE CHECK It AND TRY AGAIN")
        root.destroy()
    for x in news:
        widget.insert(END, x['title'])
        widget.insert(END, '\n')
        widget.insert(END, "DESCRIPTION: ")
        widget.insert(END, x['description'])
        widget.insert(END, '\nURL: ')
        widget.insert(END, x['url'])
        widget.insert(END, '\n\n')
        root.update()
    root.update()
    p3 = multiprocessing.Process(target=mainspeak, args=(news, 0))
    p3.start()
    root.update()


def health(widget):
    widget.delete(1.0, END)
    root.update()
    P2 = multiprocessing.Process(target=speak3)
    try:
        url_ = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
        response = requests.get(url_).text
        news_json = json.loads(response)
        news = news_json['articles']
        P2.start()
        P2.join()
    except:
        speaker.speak("THERE IS some problem  IN YOUR INTERNET CONNECTION.. PLEASE CHECK It AND TRY AGAIN")
        root.destroy()
    for x in news:
        widget.insert(END, x['title'])
        widget.insert(END, '\n')
        widget.insert(END, "DESCRIPTION: ")
        widget.insert(END, x['description'])
        widget.insert(END, '\nURL: ')
        widget.insert(END, x['url'])
        widget.insert(END, '\n\n')
        root.update()
    root.update()
    p3 = multiprocessing.Process(target=mainspeak, args=(news, 0))
    p3.start()
    root.update()

def technology(widget):
    widget.delete(1.0, END)
    root.update()
    P2 = multiprocessing.Process(target=speak3)
    try:
        url_ = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
        response = requests.get(url_).text
        news_json = json.loads(response)
        news = news_json['articles']
        P2.start()
        P2.join()
    except:
        speaker.speak("THERE IS some problem  IN YOUR INTERNET CONNECTION.. PLEASE CHECK It AND TRY AGAIN")
        root.destroy()
    for x in news:
        widget.insert(END, x['title'])
        widget.insert(END, '\n')
        widget.insert(END, "DESCRIPTION: ")
        widget.insert(END, x['description'])
        widget.insert(END, '\nURL: ')
        widget.insert(END, x['url'])
        widget.insert(END, '\n\n')
        root.update()
    root.update()
    p3 = multiprocessing.Process(target=mainspeak, args=(news, 0))
    p3.start()
    root.update()

def sports(widget):
    widget.delete(1.0, END)
    root.update()
    P2 = multiprocessing.Process(target=speak3)
    try:
        url_ = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
        response = requests.get(url_).text
        news_json = json.loads(response)
        news = news_json['articles']
        P2.start()
        P2.join()
    except:
        speaker.speak("THERE IS some problem  IN YOUR INTERNET CONNECTION.. PLEASE CHECK It AND TRY AGAIN")
        root.destroy()
    for x in news:
        widget.insert(END, x['title'])
        widget.insert(END, '\n')
        widget.insert(END, "DESCRIPTION: ")
        widget.insert(END, x['description'])
        widget.insert(END, '\nURL: ')
        widget.insert(END, x['url'])
        widget.insert(END, '\n\n')
        root.update()
    root.update()
    p3 = multiprocessing.Process(target=mainspeak, args=(news, 0))
    p3.start()
    root.update()

def buisness(widget):
    widget.delete(1.0, END)
    root.update()
    P2 = multiprocessing.Process(target=speak3)
    try:
        url_ = "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ba4cbdb2fc97412e8df66fb4d1f346ce"
        response = requests.get(url_).text
        news_json = json.loads(response)
        news = news_json['articles']
        P2.start()
        P2.join()
    except:
        speaker.speak("THERE IS some problem  IN YOUR INTERNET CONNECTION.. PLEASE CHECK It AND TRY AGAIN")
        root.destroy()
    for x in news:
        widget.insert(END, x['title'])
        widget.insert(END, '\n')
        widget.insert(END, "DESCRIPTION: ")
        widget.insert(END, x['description'])
        widget.insert(END, '\nURL: ')
        widget.insert(END, x['url'])
        widget.insert(END, '\n\n')
        root.update()
    root.update()
    p3 = multiprocessing.Process(target=mainspeak, args=(news, 0))
    p3.start()
    root.update()
def speak():
    cur_time=datetime.datetime.now()
    hour=cur_time.hour
    if(hour>=00 and hour<=11):
        speaker.speak("HELLO master! good morning.....YOUR NEWS PORTAL IS READY")
    else:
        speaker.speak("Hello master! good afternoon......... YOUR NEWS PORTAL IS READY")

def choice(widget):
    widget.place_forget()
    frame = Frame(root, bd=10, relief=SUNKEN, height=25, width=800)
    frame.place(x=10, y=440)
    scrollbarX = Scrollbar(frame)
    scrollbarX.pack(side=RIGHT, fill=Y)
    text = Text(frame,height=7,font="comicsansms 11 bold")
    text.pack(fill=Y)
    text.propagate(0)
    scrollbarX.config(command=text.yview)
    button1 = Button(root, text="SCIENCE", image=image2, width=230, height=50, bd=0, bg='#D8E3E3', relief=FLAT,
                    command=lambda: science(text), compound="center", font="comicsansms 13 bold")
    button1.place(x=535, y=120)
    button2 = Button(root, text="BUSINESS", image=image2, width=230, height=50, bd=0, bg='#D8E3E3', relief=FLAT,
                    command=lambda: buisness(text), compound="center", font="comicsansms 13 bold")
    button2.place(x=535, y=220)
    button3 = Button(root, text="HEALTH", image=image2, width=230, height=50, bd=0, bg='#D8E3E3', relief=FLAT,
                    command=lambda: health(text), compound="center", font="comicsansms 13 bold")
    button3.place(x=10, y=120)
    button4 = Button(root, text="SPORTS", image=image2, width=230, height=50, bd=0, bg='#D8E3E3', relief=FLAT,
                     command=lambda: sports(text), compound="center", font="comicsansms 13 bold")
    button4.place(x=10, y=220)
    button5 = Button(root, text="ENTERTAINMENT", image=image2, width=230, height=50, bd=0, bg='#D8E3E3', relief=FLAT,
                     command=lambda: entertainment(text), compound="center", font="comicsansms 13 bold")
    button5.place(x=10, y=320)
    button6 = Button(root, text="TECHNOLOGY", image=image2, width=230, height=50, bd=0, bg='#D8E3E3', relief=FLAT,
                     command=lambda: technology(text), compound="center", font="comicsansms 13 bold")
    button6.place(x=535, y=320)
    root.update()
    speaker.speak("WELCOME MASTER.. WHICH NEWS YOU PREFER..CHOOSE ACCORDING YOUR PREFERENCE..")













if __name__ == '__main__':
    root=Tk()
    root.geometry("780x600")

    root.wm_maxsize(780,600)
    width=170
    height=60
    image = Image.open("3.jpg")
    photo = ImageTk.PhotoImage(image)
    image_label = Label(image=photo)
    image_label.pack()
    image2=PhotoImage(file="6.png")
    image2=image2.subsample(2,3)
    p1 = multiprocessing.Process(target=speak)
    p1.start()
    button = Button(root, text="Lets start", image=image2, width=230, height=50, bd=0,bg='#CCD9D9',relief=FLAT, command=lambda:choice(button),compound="center",font="comicsansms 13 bold")
    button.place(x=280, y=510)
    root.mainloop()


