# from ast import Num
from array import *
from multiprocessing.dummy import Array
from more_itertools import first, lstrip
import scipy as sp
import speech_recognition as sr2
import speech_recognition as sr1
import speech_recognition as sr3
import time
# from winsound import PlaySound
from bs4 import BeautifulSoup
import pyttsx3
import requests
import datetime
# import scipy as sp #pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
# import datetime
# import wikipedia #pip install wikipedia
import webbrowser
from datetime import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# speak(voices[1].id)
engine.setProperty('voice', voices[1].id)

# import speech_recognition as sr
microphone = sr.Microphone()
recognizer = sr.Recognizer()

microphone1 = sr1.Microphone()
recognizer3 = sr1.Recognizer()

microphone2 = sr2.Microphone()
recognizer2 = sr2.Recognizer()


microphone3 = sr3.Microphone()
recognizer3 = sr3.Recognizer()
# import datetime


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Temp():

    # with microphone3 as source3:
    #     # speak("Shall i tell the temperature outside:")
    #     recognizer3.adjust_for_ambient_noise(source3,duration=0.5)
    #     audio = recognizer3.listen(source3)
    #     # speak("Say...")
    #     # print("wait....")

    #     i = recognizer3.recognize_google(audio)
    #     speak("reconizing...")
    #     i.lower()

    # if(i == "yes" or i == "Yes" or i == "Yah" or i == "yah" or i == "ON" or i== "on" or i == "s" or i == "S" or i=="hmm" or i == "Hmm"):
    #     speak("Ok I will tell the temperature")
    #     speak("where are you ?")
    #     print("where are you ?")
    # miejsce = takeCommand().lower()
    city = "Kathmandu"
    search = (f"Temperature in  {city}")
    url = (f'https://www.google.com/search?q={search}')
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    print(f"In {search} outside there is {temp}")
    speak(f"In {search} outside there is {temp}")

    # else:
    # speak("Ok")
    # takeCommand().lower()
    # speak("Ok ! so what you want me to work ?")


def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("It is")
    # speak(Time)

    now = datetime.now().hour
    if (now > 12):
        now = now - 12
    am_pm = "AM"
    if(now < 12):
        am_pm = "PM"
    now1 = datetime.now().minute
    now2 = datetime.now().second
    tme = now, am_pm, now1, "Minutes", now2, "second"
    speak(tme)
    Temp()

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # speak("Current Time =", current_time)
    # speak("Current Time =", current_time)

    speak("I am Your Personal assistant AI")
    speak("Thank you for creating me ")
    speak("Hello Niraj")
    speak("Good to see you again")
    speak("Please tell how may i help you ?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognized...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # speak(f" {query}\n")

    except Exception as e:
        # speak(e)
        speak("Say that again please...")
        return "None"
    return query

# def Temp():
#     search = "Temperatur in Kirtipur"
#     url = f"https://www.google.com/search?1={search}"
#     r = requests.get(url)
#     data = BeautifulSoup(r.text,"html.parser")
#     temperature = data.find("div",class_="BNeawe").text
#     speak(f"The temperatur Outside is {temperature} celcius")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nirajkumarchaurasiya6@gmail.com', 'FUTUREROBOTICS@1234')
    server.sendmail('nirajkumarchaurasiya29@gmail.com', to, content)
    server.close()


def takeCommandAlarm():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognized...")
        speak("Recognizing...")
        hour = r.recognize_google(audio, language='en-in')
        # speak(f" {query}\n")

    except Exception as e:
        # speak(e)
        speak("Say that again please...")
        hour1 = datetime.now().hour
        return (f"{hour1}")
    return (f"{hour}")


def takeCommandfirstnum():
    # It takes microphone input from the user and returns string output
    # speak("Speak first number")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognized...")
        speak("Recognizing...")
        firs = r.recognize_google(audio, language='en-in')
        # speak(f" {query}\n")

    except Exception as e:
        # speak(e)
        speak("Say that again please...")

        return "None"
    return (firs)


def takeCommandsecondnum():
    # It takes microphone input from the user and returns string output
    speak("How many numbers:")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognized...")
        speak("Recognizing...")
        n = r.recognize_google(audio, language='en-in')
        # speak(f" {query}\n")

    except Exception as e:
        # speak(e)
        speak("Say that again please...")

        return "None"

    return (n)


def takeCommandoperator():
    # It takes microphone input from the user and returns string output
    speak("operator....")
    speak("1 for addition , 2 for subtraction , 3 for multiplication , 4 for division")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognized...")
        speak("Recognizing...")
        op = r.recognize_google(audio, language='en-in')
        # speak(f" {query}\n")

    except Exception as e:
        # speak(e)
        speak("Say that again please...")

        return ("None")
    return (op)


def takeCommandAlarm1():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognized...")
        speak("Recognizing...")
        min = r.recognize_google(audio, language='en-in')
        # speak(f" {query}\n")

    except Exception as e:
        # speak(e)
        speak("Say that again please...")
        mins = datetime.now().minute + 2
        return (f"{mins}")
    return (f"{min}")


# def takeCommandAlarm2():
#     # It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")

#         r.pause_threshold = 0.5
#         audio = r.listen(source)

#     try:
#         print("Recognized...")
#         speak("Recognizing...")
#         am_pm = r.recognize_google(audio, language='en-in')
#         # speak(f" {query}\n")

#     except Exception as e:
#         # speak(e)
#         speak("Say that again please...")
#         return "None"
#     return am_pm


if __name__ == "__main__":
    wishMe()

    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            # results = wikipedia.summary(query, sentences=2)
            webbrowser.open(query)
            speak("According to Wikipedia")
            speak("Listening......")
            # speak(results)
            # speak(results)

        elif 'good morning' in query:
            speak("Good morning sir ?")
            print("good morning sir")
            speak("tell me set an alarm")
        
        elif 'set alarm' in query:
            # speak("Ok i will set alarm")
            speak("Offcourse I will set alarm for you ")
            speak(" at what time  ")
            speak("Ok first of all say ")
            speak("At what hour")
            hour = takeCommandAlarm().lower()
            am_pm = "AM"
            if(datetime.now().hour > 12):
                am_pm = "PM"

            if (am_pm == "PM" and int(hour) < 12):
                hour = int(hour) + 12

            speak(f"Ohh so hour is {hour}")
            speak("But this is not enought to set")
            speak("Can you tell me the minute please")
            min = takeCommandAlarm1().lower()
            speak(F"Ohh so minute is {min}")
            speak("Few step to go")
            sec = 0
            # am_pm = takeCommandAlarm2().lower()
            # if(am_pm == "am" or am_pm == "AM" or am_pm=="ON" or am_pm == "1" or am_pm == "True" or am_pm == "true"  ):
            #     hour += 12
            speak(f"Ok got it your alarm is set as {hour} {min} ")

            print(f"{hour},{min}")
            n = 1
            while(n > 0):

                if time.localtime().tm_hour == int(hour) and time.localtime().tm_min == int(min) and time.localtime().tm_sec == sec:

                    # os.startfile('a.mp3')
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=at1HzOgfxfU")
                    for x in range(1, 10):
                        if(x == 1):
                            speak("Hello mister ")
                            speak("Your alarm is over")
                            speak("Wake up")
                            speak("Times up")
                            Temp()

                        elif (x >= 2 and x <= 4):
                            speak("BE THE PERSON VALUE RATHER THAN SUCCESS:")
                            speak("Wake up")
                            speak("Wake up")
                            speak("Times up")
                            Temp()
                            speak("Wake up")

                        # elif (x==6):
                            # webbrowser.open("https://www.youtube.com/watch?v=a1CwygQ13VI")

                        elif (x >= 4 and x <= 7):
                            speak("A CHAMPION IS ONE WHO WAKES UP WHEN HE CAN'T")
                            speak("Oh my god:")
                            speak(" wake up:")
                            speak("Wake up")
                            # speak("Wake up")
                            speak("Times up")
                            Temp()
                            speak("Wake up")
                        elif (x == 8):
                            os.startfile('a.mp3')
                        else:
                            # speak("Ohh my go wake up man:")
                            speak("Wake up")
                            speak("Wake up")
                            speak("helloooo")
                            speak("Times up")
                            speak("Now stand up")
                            # Temp()
                            speak("Wake up")

                    # speak("Wake up mister")
                    # speak("Wake up")
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=wUif7y2FUWU")

                    break
                else:
                    n += 1

        elif 'what can you do' in query:
            speak(
                "I can open youtube , search you anything open stackoverflow , open music etc")
            speak("What do you wanna me to play ?")
        elif 'friend' in query:
            speak("Ok I Know who you are ")
            speak("So I am searching ?")
            print("Searching...")
            query = query.replace("friend", "")
            webbrowser.open(query)
            speak("Listening !!")

        elif 'open team' in query:
            codepath = "C://Users//niraj//AppData//Local//Microsoft//Teams//current//Teams.exe"
            os.startfile(codepath)
            speak("Listening....")

        elif 'open idea' in query:
            codePath = "C://Program Files//JetBrains//IntelliJ IDEA Community Edition 2021.3.2//bin//idea64.exe"
            os.startfile(codePath)
            speak("Listening.....")

        elif 'open pycharm' in query:
            pycharm = "C://Program Files//JetBrains//PyCharm Community Edition 2021.3.3//bin//pycharm64.exe"
            os.startfile(codePath)
            speak("Listening.....")
        elif 'cortana' in query:
            print("Yes . What can i do ?")
            speak("Yes what can i do ?")
        elif 'open block' in query:
            pathname = "C://Program Files//CodeBlocks//codeblocks.exe"
            os.startfile(pathname)
            speak("Opening...")
            speak("Listening...")
        elif 'open cpp' in query:
            pathname = "C://Program Files (x86)//Dev-Cpp//devcpp.exe"
            os.startfile(pathname)
            speak("Opening....")

            speak("Speaking...")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening.....")
            speak("listening....")

        elif 'open github' in query:
            webbrowser.open("github.com")
            speak("Opening....")
            speak("Listening...")

        elif 'open over' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening...")
            speak("Listening.....")

    #     elif "set alarm" in query:
    #         speak("Ok I will set an alarm for you")
    #         speak("At what time dear ?")
    #         speak("Ok first tell me the hour?")

    #         # For getting hours

    #         with microphone as source:
    #             recognizer.adjust_for_ambient_noise(source, duration=0.5)
    #             audio = recognizer.listen(source)
    # # try:

    #             print("say....")
    #             speak("reconizing...")

    #             alarmhr = recognizer.recognize_google(audio)
    #             alarmhr.lower()

    # # except Exception as e:
    # #     speak(e)
    # #     print(e)
    # #     speak("say that again sir")

    # # For
    #             print(alarmhr)
    #             speak("Ok i got it . And What about minutes")

    #         # For getting minute

    #         with microphone1 as source1:
    #             recognizer3.adjust_for_ambient_noise(source1, duration=0.5)
    #             audio = recognizer3.listen(source1)
    # # try:
    #             print("wait....")
    #             speak("reconizing...")
    #             alarmMin = recognizer3.recognize_google(audio)
    #             alarmMin.lower()
    #             print(alarmMin)

    #         speak("Ok i got it my friend. Tell me am or pm")

    #         # For getting second

    #         with microphone2 as source12:
    #             recognizer2.adjust_for_ambient_noise(source12, duration=0.5)
    #             audio = recognizer2.listen(source12)
    # # try:
    #             speak("reconizing...")
    #             print("wait....")
    # # label
    #             alarmAm = recognizer2.recognize_google(audio)
    #             alarmAm.lower()
    #             print(alarmAm)

    #         if alarmhr == "1":
    #             alarmhr += 12

            # speak(f"Ok got it your alarm is set as {alarmhr} {alarmMin}")
            # sec = 0
            # print(f"{alarmhr},{alarmMin}")
            # n = 1
            # while(n > 0):
            #     if time.localtime().tm_hour == int(alarmhr) and time.localtime().tm_min == int(alarmMin) and time.localtime().tm_sec == sec:
            #         os.startfile('a.mp3')
            #         break
            #     else:
            #         n += 1


        elif 'make a picture of celebrity' in query:
            from sketchpy import library as lib
            object = lib.rdj()
            object.draw()
        elif 'terminate yourself' in query:
            speak("Oh ok ")
            speak("I am terminating my self")
            speak("I will apreciate working with you")
            break
        elif 'play old song' in query:
            music_dir = 'A://music'
            songs = os.listdir(music_dir)
            speak(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Listening.....")

        elif 'play movie' in query:
            video_src = 'A://AAAAAAAAAAAAAAA'
            video = os.listdir(video_src)
            speak(video)
            os.startfile(os.path.join(video_src, video[0]))
            speak("opening...")

        elif 'apple' in query:
            webbrowser.open("https://www.youtube.com/watch?v=n6L31s9B8L8")
            speak("opening...")

        elif 'open genius' in query:
            webbrowser.open(
                "https://drive.google.com/drive/folders/10geTs-YTAApYk8xfREawQUPIvRSuzKJz")
            speak("opening...")

        elif 'open telegram' in query:
            path = "C://Users//niraj//AppData\Roaming//Telegram Desktop//Telegram.exe"
            os.startfile(path)
            speak("opening...")

        elif 'open php' in query:
            path = "C://xampp//xampp-control.exe"
            os.startfile(path)
            speak("opening...")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Dear, the time is {strTime}")
            speak("Listening.....")
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
            speak("Listening...")

        elif 'open steam' in query:
            path = "C://Program Files (x86)//Steam//steam.exe"
            os.startfile(path)
            speak("opening...")
            # speak("")
        elif 'open firefox' in query:
            path = "C://Program Files//Mozilla Firefox//firefox.exe"
            os.startfile(path)
            speak("opening...")

        elif 'open microsoft' in query:
            path = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"
            os.startfile(path)
            speak("opening....")
        elif 'open rockstar game' in query:
            path = "C://Program Files//Rockstar Games//Launcher//LauncherPatcher.exe"
            os.startfile(path)
            speak("opening....")

        elif 'what is your name' in query:
            speak("My name is Jarvis !  ")
            speak("How many times should I say ?")
            speak("I have been created by Mr.Niraj")
            speak("Please tell me how may i help you ?")
            speak("Listening.....")
            # speak("Listening.......")

        elif 'who are you' in query:
            speak("My name is Jarvis !  ")
            speak("How many times should I say ?")
            speak("I have been created by Mr.Niraj")
            speak("Please tell me how may i help you ?")
            speak("Listening.....")
            # speak("Listening.......")

        elif 'open code' in query:
            codePath = "C://Users//niraj//AppData//Local//Programs//Microsoft VS Code//Code.exe"
            os.startfile(codePath)
            speak("Listening.....")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nirajkumarchaurasiya29@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                speak("Listening.....")
            except Exception as e:
                speak(e)
                speak("Sorry my friend Niraj. I am not able to send this email")
                speak("Listening.....")
        # elif "Yes" in query:
        #     speak("where are you ?")
        #     print("where are you ?")
        # miejsce=takeCommand().lower()
        # search = (f"Temperature in  {miejsce}")
        # url = (f'https://www.google.com/search?q={search}')
        # r = requests.get(url)
        # data = BeautifulSoup(r.text , "html.parser")
        # temp = data.find("div", class_="BNeawe").text
        # print(f"In {search} there is {temp}")
        # speak(f"In {search} there is {temp}")

        elif 'tell jokes' in query:
            speak("I think you are upset")
            speak("Ok dear I will tell jokes for you")
            speak('''1. What do you call a boomerang that won't come back?
            A stick.

            2. What does a cloud wear under his raincoat?
            Thunderwear.

            3. Two pickles fell out of a jar onto the floor. What did one say to the other?
            Dill with it.

            4. What time is it when the clock strikes 13?
            Time to get a new clock.

            5. How does a cucumber become a pickle?
            It goes through a jarring experience''')

        elif 'motivation story' in query:
            speak("I am impressed you want to listen motivational story")
            speak("Here i found for you")
            speak("Arnold")
            speak('''
            Arnold's father was an abusive alcoholic Nazi cop. He used to beat Arnold with belts. As an escape,
             Arnold watched action movies, and he developed a love for America. Arnold felt his real future awaited him there,
              but his father ridiculed his dreams. His father wanted him to be a police officer, but Arnolds 
            will would not be broken. This belief made it to the Some of the True motivational stories. one day he escaped 
            Arnold Schwarzenegger Biography | A true motivational story
            A true motivational Arnold Schwarzenegger Biography.

            arnold schwarzenegger biography, true motivational, inspirational, motivational stories.

                Arnold’s father was an abusive alcoholic Nazi cop. He used to beat Arnold with belts. As an escape,
                 Arnold watched action movies, and he developed a love for America. Arnold felt his real future awaited him there,
                  but his father ridiculed his dreams.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                His father wanted him to be a police officer, but Arnold’s will would not be broken.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                Bodybuilding was his only way out. So he did everything he could to train for competitions. He even escaped basic
                 army training to compete and spent a week in a military prison as punishment.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                With only a dream and $20 in his pocket, Arnold left for America.

                “If you want to turn a vision into reality, you have to give 100 and never stop believing in your dream”

                He arrived in California when he was 21 years old. He worked as a bricklayer during the day, at night, he would focus 
                on his dream of making it in America. Many of his friends helped him out, giving him dishes and pillows because he was so broke. 
                He started selling gym equipment, He then took any leftover money and made small investments in real estate.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                Arnold had his sights set on Hollywood but he struggled early in his acting career.

                He was told:

                His body was too big and weird,

                arnold schwarzenegger biography, inspirational, true motivational, stories

                He was told:

                He had a funny accent,

                He was told:

                his name was too long – Schwarzenegger

                Everywhere I turned, I was told that:

                I had no chance.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                But Arnold stayed true to himself and his dream, and quickly make a name for himself as an actor.
                 He got a small role after small role, even won a Golden Globe for New Star of the year in 1976.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                With the money he made from his side hustle, Arnold decided to focus on acting full-time.

                It was a fateful decision, as he got a big role, even though it was in a low budget movie. A role turned down by Mel Gibson, 
                Tom Selleck, Chevy Chase, and almost given to Oj Simpson. But in 1984, “the Terminator” launched Arnold to stardom, and he became an action hero icon,

                arnold schwarzenegger biography, inspirational, true motivational, stories

                The meaning of life is not simply to exist, to survive, but to move ahead, to go up, to achieve, to conquer.

                With a bag full of blockbusters, Arnold reinvented himself yet again in 2003, when he left the world of 
                entertainment to devote himself fully to public service, eventually being elected Governor of California.

                arnold schwarzenegger biography, inspirational, true motivational, stories

                Arnold is involved with the Special Olympics, and found programs that educate youth about health, Befitting 
                this real-life action hero, he once saved a drowning man off the coast of Maui.

                His movies have made billions but more importantly, he is the embodiment of the American Dream and a reminder 
                that no matter where we come from, We are the masters of our own destiny.

                Arnold schwarzenegger, motivational, inspirational, true story, arnold schwarzenegger biography

                 “Your struggles develop your strengths, when you go through hardships and decide not to surrender, that is strength.”
                  Arnold Schwarzenegger

                Never stop believing.

                Arnold Schwarzenegger biography.''')

        elif 'another' in query:
            speak("Here you go again")
            speak("The theme is")
            speak('''Tesla: I don't care that they stole my idea but…''')
            speak('''His father was a priest, his mother, an inventor.

            He was born during a lightning storm. he had a photographic memory.
            He was smart enough to memorize books, images, and even 3D structures. As a teenager, he contracted cholera. For over 9 months,
            he was bedridden for 9 months and had almost died. In college, he became fascinated with electricity.
            He moved to the US in 1884 to work for the famous inventor Thomas Edison.
            Edison said his ideas were “splendid”, but “utterly impractical”. The company once offered him $12 million 
            to improve his DC motor, and he did. But Edison failed to pay him, saying, “you don't understand American humor.”
            Instead, he offered him a raise of $10 a week. He quit working for him after this incident.
            ” I do not care that they stole my idea. I only care that they don’t have any of their own.”
            Edison and Tesla maintained their rivalry for years. It was called “the War of the Currents”

            He eventually won and helped bring electricity to America. years later, he demonstrated radio transmission but a fire destroyed his lab as he 
            prepared the first real radio signal. Marconi then took his ideas and his technology
            to win the Nobel Price. Tesla was inflamed, especially when he found out, Marconi had received all his financial support from his old rival Edison.
            The court invalidated Marconi’s radio patents because they were based on Tesla’s work. Justice finally prevails, true, but unfortunately it happened 
            two years after his death. He once didn’t even sleep and worked for continuous 84 hours. He spoke eight languages. and filled more than 300 patents. 
            Some of his work is still classified by the U.S. Government.

            Truthfully he never really cared about the money. Years after he died a statue of him was erected in Silicon Valley. The statue is equipped with free wi-fi connection.

            “Science is but a perversion of itself unless it has as its ultimate goal the betterment of humanity. “
            7 life lessons from Nikola Tesla
            Once you learn the 7 life lessons from Nikola Tesla you’ll live a much better life.

            Don’t pay attention to what others are doing.
            instead of focusing on what the world can take form us, we need to focus on what we can put into the world.

            Looking inward, help you see clearer.
            Reflection is an important part of being your authentic self and being true to what you want in life.

            It’s okay to be ahead of everyone else
            Tesla reminds us that real creators are okay with people not accepting their ideas. Don’t give up. Be proud of what you are capable of.

            Never stop learning and reading
            The internet is full of information and ideas. Rather than sift through journals, reading stories and ideas of how things were done can ignite real creativity in people.

            Be patient and just push on
            Patience goes a long way. Don’t worry about how long it will take to achieve your dreams. Just keep working on them.
            Never stop creating.
            No matter what anyone says- even you, don’t stop making things. Use your talent to help make the world better.

            Money isn’t everything.
            Tesla cheers us to create for creation’s sake. If there are rewards to be had, great: but if not, creation can be reward enough.

            
            ''')
            speak("This is much about Tesla")
            speak("Hope you like it")
        elif 'thank you' in query:
            speak("Are you saying thank you to machine ")
            speak("Welcome")

        # elif 'calculator' in query:
        #     speak("SO you wanna calculate")
        #     # speak("Speak 1st number:")
        #     # a = takeCommandfirstnum().lower()  # first number
        #     speak("turn for operator :")
        #     op = takeCommandoperator().lower()
        #     print(op) #operator
        #     speak("By the way how many numbers:")
        #     c = (takeCommandsecondnum().lower())
        #     print(c)  # second number
        #     d =array("i",[])
        #     for i in range(1,int(c)+1):
        #         x = speak(int("speak the next value:"))
        #         d.append(x)
        #         print(d)
        #     sum = 0
        #     if(op == 1):
        #         for i in range(1,int(c)+1):
        #             sum += c[i]

        elif "exit" in query:
            print("Ok")
            speak("Oh ok I will exit")

            break

        else:
            speak("I repeat Please say that again please")
            speak("because I did not catch that")
            # speak("Please Tell me another task to do .")
