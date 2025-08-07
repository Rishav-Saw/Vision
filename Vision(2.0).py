import time
import wikipedia
import subprocess
import webbrowser
import pyjokes
import requests
import wolframalpha
import speech_recognition as sr
import pyttsx3

from textblob import TextBlob
from textblob import Word

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wolfarmAlpha (query):
	client = wolframalpha.Client("JPJPHQ-U7455W96LL")
	res = client.query(query)
	try:
			print (next(res.results).text)
			speak(next(res.results).text)
	except StopIteration:
			print ("No results")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Please Say Something...\n Listening...")
        audio = r.listen(source)
        print("OKAY...")

        try:
            said = r.recognize_google(audio, language= 'en-in')
            print("YOU Said: \n" +said)
        except Exception as e:
            print("SORRY! Unable to Understand")
            print("Exception : " + str(e))
            pass;
        return said

while True:
    text = get_audio()
    if "hello" in text:
        speak("hello Sir , Welcome back, How may i help you?")
    elif "what is your name" in text:
        speak("Sir, My name is VISION , aaaand I am your Spell assistant")

    elif"explain about this project" in text:
        speak("this is a project to take input from the user in the form of voice and print it's polarity,AND what is it about")
    elif"introduction" in text:
        speak("hello I am vision, i am your spell assistant and I am here to recognize your voice and tell it's polarity")

    elif ('wikipedia' in text or "search" in text or "what is" in text or "who is" in text) and('on youtube' not in text and "on google" not in text) :
        speak('Searching Wikipedia...')
        text = text.replace("on wikipedia", "")
        text = text.replace("search ", "")
        results = wikipedia.summary(text, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    
    elif 'exit' in text or "stop listing" in text:
        speak("Thanks for giving me your time")
        exit()

    elif 'shutdown system' in text:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
    elif "restart" in text:
        subprocess.call(["shutdown", "/r"])
    elif "hibernate" in text or "sleep" in text:
        speak("Hibernating")
        subprocess.call("shutdown / h")
    elif "log off" in text or "sign out" in text:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif 'open google' in text:
        speak("Here you go to Google\n")
        webbrowser.open_new_tab("google.com")
    
    elif 'on google' in text:
        text = text.replace("search ", "")
        text = text.replace("on google", "")
        speak("Here you go to Google\n")
        webbrowser.open_new_tab("https://www.google.com/search?q="+text)

    elif 'open youtube' in text:
        speak("Here you go to Youtube\n")
        webbrowser.open_new_tab("https://youtube.com")
    
    elif "open wikipedia" in text:
        webbrowser.open("wikipedia.com")
    
    elif 'on youtube' in text:
        text = text.replace("search ", "")
        text =text.replace("on youtube", "")
        speak("Here you go to Youtube\n")
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+text)
    
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    
    elif "weather" in text:
        api_key = "33507e541ae781813c832323b86ec6da"
        speak(" City name ")
        city_name = get_audio()
        
        complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(complete_url)
        
        if response.status_code != "404":
            x = response.json()
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature (in kelvin unit) is " +str(current_temperature)+"\n Atmospheric pressure (in hPa unit) is "+str(current_pressure) +"\n Humidity (in percentage) is " +str(current_humidiy) +"\n Description is " +str(weather_description))
        else:
            speak(" City Not Found ")
            print(" City Not Found ")
    
    elif "how are you" in text:
        speak("I'm fine, glad you asked me that")
    
    elif "play video" in text or "play music":
        pass
    
    else:
        wolfarmAlpha(text)
    

    obj = TextBlob (text)

    sentiment, subjectivity = obj.sentiment
    print(obj.sentiment)

    if sentiment == 0:
        print('\nYour words are Neutral\n')
    elif sentiment > 0:
        print('\nYour words are Positive\n')
    else:
        print('\nYour words are Negetive\n')

    nouns = list()
    for word, tag in obj.tags:
        if tag == 'NN':
            nouns.append(word.lemmatize())

    print("\nYou spoke about...\n")
    for item in nouns:
        word = Word(item)
        print(word.pluralize())
