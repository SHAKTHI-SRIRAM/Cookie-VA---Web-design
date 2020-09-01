from django.shortcuts import render

import os
import time
import speech_recognition as sr
import playsound
import random
from gtts import gTTS
from time import ctime
import webbrowser
import wikipedia
import pywhatkit as kit

# Create your views here.
def index(request):
    return render(request, 'home/home.html')


def new_search(request):
    search = request.POST.get('search')
    if 'good morning cookie' in search:
        response = 'good morning'
        print(response)
    return render(request, 'home/new_search.html')


def respond(voice_data):
    if 'good morning cookie' in voice_data:
        response = 'good morning'
        return response


def listen_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            print(ask)
        voice_data = r.record(source, duration=5)
        try:
            said = r.recognize_google(voice_data)
            print(said)
        except Exception as e:
            print('Recognizing' + str(e))
    return said


def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    r = random.randint(1, 100000000)
    ado_file = 'ado-' + str(r) + '.mp3'
    tts.save(ado_file)
    playsound.playsound(ado_file)
    print(text)
    os.remove(ado_file)
