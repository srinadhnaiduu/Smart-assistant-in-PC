import speech_recognition as sr
import pyaudio
import pyttsx3
import webbrowser
import pywhatkit
import datetime
import pyjokes
import wikipedia
import smtplib
import requests
import ecapture
import wolframalpha
import os
import qrcode

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(" hello srinadh")
engine.runAndWait()

a = True
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source)
            global command
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'srinadh' in command:
                command = command.replace('srinadh','')
                print(command)
    except:
        pass
    return command

def show_snapqr():
    img = qrcode.make(
    'https://www.snapchat.com/add/srinadhnaiduu'
)






def show_instaqr():
    img=qrcode.make('https://www.instagram.com/itzz_srinadh?igsh=MjA1eWJ3bDlpMm03')
    img.show()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("naidusrinath96@gmail.com", "jjys bdnt rslq lttu")
    server.sendmail("naidusrinath96@gmail.com", "sunnyenjamuri4456@gmail.com", "hello")
    server.quit()

def run():
    command = take()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'who ' in command:
        person = command.replace('who', '')
        about = wikipedia.summary(person, 1)
        print(about)
        talk(about)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open amazon" in command:
        webbrowser.open('https://www.amazon.com')
    elif "open spotify" in command:
        webbrowser.open('https://www.spotify.com')
    elif "open wikipedia" in command:
        webbrowser.open('https://www.wikipedia.org/')
    elif "open chat gpt" in command:
        webbrowser.open('https://chat.openai.com/')
    elif "open whatsapp" in command:
        webbrowser.open('https://www.whatsapp.com/')
    elif "open facebook" in command:
        webbrowser.open('https://www.facebook.com')
    elif "open snapchat" in command:
        talk("I am not able to open SnapChat as it is a private platform.")
    elif "open google translator" in command:
        webbrowser.open('https://translate.google.co.in/')
    elif "open maps" in command:
        webbrowser.open('https://maps.google.com')
    elif "open sbtet" in command:
        webbrowser.open('https://sbtet.telangana.gov.in/index.html')
    elif "open ts ecet" in command:
        webbrowser.open('https://ecet.tsche.ac.in/')    
    elif "open i bomma" in command:
        webbrowser.open('https://men.ibomma.bond/')
    elif "open telegram" in command:
        webbrowser.open = ('https://web.telegram.org/a/')
    elif "open flipkart" in command:
        webbrowser.open('https://www.flipkart.com/')
    elif "open calender" in command:
        webbrowser.open('https://www.timeanddate.com/calendar/')    
    elif "open calculator" in command:
        webbrowser.open('https://www.calculator.net/scientific-calculator.html')    
    elif "open zoom call" in command:
        webbrowser.open('https://zoom.us/')  
    elif "open netflix" in command:
        webbrowser.open('https://www.netflix.com/in/')      
    elif "open pinterest" in command:
        webbrowser.open('https://in.pinterest.com/')    
    elif "open discord" in command:
        webbrowser.open('https://discord.com/') 
    elif "open linkdin" in command:
        webbrowser.open('https://in.linkedin.com/')     
    elif "open disney hotstar" in command:
        webbrowser.open('https://www.hotstar.com/in/home?ref=%2Fin')    
    elif "open dino game" in command:
        webbrowser.open('https://poki.com/en/g/dinosaur-game')
    elif 'i am single' in command:
        talk('oh then i love you')   
    elif 'who designed you' in command:
        talk('srinath my friend !')   
    elif 'can you show my current location' in command:
        talk('oh yeah definitely')
        webbrowser.open('https://www.google.com/maps/place/SREE+ACADEMY+JEE+MAINS+ECET+EAMCET+EAPCET/@17.3667843,78.5202507,18.9z/data=!4m6!3m5!1s0x3bcb98f61b82d9a9:0x12f44a99772b8ebf!8m2!3d17.3668508!4d78.5210059!16s%2Fg%2F1ptyb9w1j?entry=ttu')
    elif 'show my instagram id' in command:
        talk('showing')
        show_instaqr()   
    elif 'show my snapchat id' in command:
        talk('showing')
        show_snapqr()
            
        
     

            
    elif 'are you single' in command:
        talk('i have connection with you')
    elif 'love you' in command:
        talk('love you too')
    elif 'hate you' in command:
        talk('dont do that')
    elif 'sreenath lover name' in command:
        talk('error 404')
    elif 'how are you' in command:
        talk('I am fine,What about you?')
    elif 'what are you doing' in command:
        talk('finding something for you')
    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
        talk("srinath")
        print("srinath")
    elif "open camera" in command or "take a photo" in command or "take a snap" in command:
        ecapture.capture(0, "robo camera", "img.jpg")
    elif "send email" in command:
        talk("check out, srinadhnaidu1215@gmail.com")

    elif "weather" in command:
        api_key = "e9d5ef67ce396bc350cb6c486e640d29"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        talk("whats the city name")
        city_name = take()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(" Temperature in kelvin unit is " + str(current_temperature) + "\n humidity in percentage is " + str(current_humidiy) + "\n description  " + str(weather_description))
            print(" Temperature in kelvin unit = " + str(current_temperature) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
        else:
            talk(" City Not Found ")

    elif 'ask' in command:
        talk(' what question do you want to ask now')
        question = take()
        app_id = "ATHWPX-UGRRK2AH4A"
        client = wolframalpha.Client('ATHWPX-UGRRK2AH4A')
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)
    elif "email" in command:
        receiver = command.split("to")[-1].strip()
        subject = command.split("subject")[-1].strip()
        message = command.split("message")[-1].strip()
        send_email()
        talk("Email has been sent")   
    
    elif "news" in command:
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=274360823bad4be49a0dad4ceac605e8"
        data = requests.get(url).json()
        article = data["articles"]
        result = []
        for text in article:
            result.append(text["title"])
        for i in range(5):
            print(i + 1, result[i])
            talk(result[i])
    elif 'search' in command:
        query = command.replace('search', '')
        talk('Searching Google for '+query) 
        pywhatkit.search(query)
        
    elif "ok bye" in command:
        talk("goodbye see you later buddy!")
        global a
        a = False
while a:
    run()