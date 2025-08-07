import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import nltk
from textblob import TextBlob
from textblob import Word


def speak(text):
    tts=gTTS(text=text, lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

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

text = get_audio()
if "hello" in text:
    speak("hello Sir , Welcome back, How may i help you?")
elif "what is your name" in text:
    speak("Sir, My name is VISION , aaaand I am your Spell assistant")
elif "exit" in text:
    speak("Exiting...")
elif"explain about this project" in text:
    speak("this is a project to take input from the user in the form of voice and print it's polarity,AND what is it about")
elif"introduction" in text:
    speak("hello I am vision, i am your spell assistant and I am here to recognize your voice and tell it's polarity")

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
