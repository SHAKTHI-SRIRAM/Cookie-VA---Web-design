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


def cookie_docs(request):
    return render(request, 'home/cookie_docs.html')


def new_search(request):
    search = request.POST.get('search')
    response = respond(search)

    context = {
        'search': search,
        'response': response
    }
    return render(request, 'home/new_search.html', context)


def google_search(request):
    if request.method == 'GET':
        return render(request, 'home/google_search.html')
    elif request.method == 'POST':
        data = request.POST.get('record')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            voice_data = r.record(source, duration=5)
            try:
                voice_query = r.recognize_google(voice_data)
                url = 'https://google.com/search?q=' + voice_query
                webbrowser.get().open(url)
                response = 'Your search results will be opened in a new tab'
                context = {
                    'response': response,
                }
                return render(request, 'home/google_search.html', context)
            except sr.UnknownValueError:
                voice_query = "Could not understand audio"
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/google_search.html', context)
            except sr.RequestError as e:
                voice_query = "Could not request results; {0}".format(e)
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/google_search.html', context)
    


def wiki_search(request):
    if request.method == 'GET':
        return render(request, 'home/wiki_search.html')
    elif request.method == 'POST':
        data = request.POST.get('record')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            voice_data = r.record(source, duration=5)
            try:
                voice_query = r.recognize_google(voice_data)
                url = 'https://en.wikipedia.org/wiki/Special:Search?search=' + voice_query
                webbrowser.get().open(url)
                context = {
                    'response': 'Your search results will be opened in a new tab!!..',
                }
                return render(request, 'home/wiki_search.html', context)
            except sr.UnknownValueError:
                voice_query = "Could not understand audio"
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/wiki_search.html', context)
            except sr.RequestError as e:
                voice_query = "Could not request results; {0}".format(e)
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/wiki_search.html', context)
    


def ytube_search(request):
    if request.method == 'GET':
        return render(request, 'home/ytube_search.html')
    elif request.method == 'POST':
        data = request.POST.get('record')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            voice_data = r.record(source, duration=5)
            try:
                voice_query = r.recognize_google(voice_data)
                kit.playonyt(voice_query)
                context = {
                    'response': 'Your search results will be opened in a new tab!!..',
                }
                return render(request, 'home/ytube_search.html', context)
            except sr.UnknownValueError:
                voice_query = "Could not understand audio"
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/ytube_search.html', context)
            except sr.RequestError as e:
                voice_query = "Could not request results; {0}".format(e)
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/ytube_search.html', context)


def gmaps_search(request):
    if request.method == 'GET':
        return render(request, 'home/gmaps_search.html')
    elif request.method == 'POST':
        data = request.POST.get('record')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            voice_data = r.record(source, duration=5)
            try:
                voice_query = r.recognize_google(voice_data)
                url = 'https://google.nl/maps/place/' + voice_query + '/&amp;'
                webbrowser.get().open(url)
                context = {
                    'response': 'Your search results will be opened in a new tab!!..',
                }
                return render(request, 'home/gmaps_search.html', context)
            except sr.UnknownValueError:
                voice_query = "Could not understand audio"
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/gmaps_search.html', context)
            except sr.RequestError as e:
                voice_query = "Could not request results; {0}".format(e)
                context = {
                    'response': voice_query,
                }
                return render(request, 'home/gmaps_search.html', context)


def google_response(request):
    search = request.POST.get('search')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    context = {
        'response': 'Your search results will appear in new tab!!..'
    }
    return render(request, 'home/google_response.html', context)


def wiki_response(request):
    search = request.POST.get('search')
    url = 'https://en.wikipedia.org/wiki/Special:Search?search=' + search
    webbrowser.get().open(url)
    context = {
        'response': 'Your search results will appear in new tab!!..'
    }
    return render(request, 'home/wiki_response.html', context)


def ytube_response(request):
    search = request.POST.get('search')
    kit.playonyt(search)
    context = {
        'response': 'Your search results will appear in new tab!!..'
    }
    return render(request, 'home/ytube_response.html', context)


def gmaps_response(request):
    search = request.POST.get('search')
    url = 'https://google.nl/maps/place/' + search + '/&amp;'
    webbrowser.get().open(url)
    context = {
        'response': 'Your search results will appear in new tab!!..'
    }
    return render(request, 'home/gmaps_response.html', context)



def voice_search(request):
    if request.method == 'GET':
        return render(request, 'home/voice_search.html')
    elif request.method == 'POST':
        data = request.POST.get('record')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            voice_data = r.record(source, duration=5)
            try:
                voice_query = r.recognize_google(voice_data)
            except sr.UnknownValueError:
                voice_query = "Could not understand audio"
            except sr.RequestError as e:
                voice_query = "Could not request results; {0}".format(e)
        
        output = respond(voice_query)
        context = {
            'response': output,
        }
        return render(request, 'home/voice_search.html', context)


def respond(search):
    if 'good morning cookie' in search:
        response = 'good morning'
    elif 'good afternoon cookie' in search:
        response = 'good afternoon'
    elif 'how are you doing cookie' in search:
        response = 'Pretty Well'
    elif 'how are you cookie' in search:
        response = 'I am fine how about you'
    elif 'what is your name' in search:
        response = 'My name is Cookie'
    elif 'who are you' in search:
        response = 'My name is Cookie. The Virtual Assistant. Version 1.0'
    elif 'tell me about yourself' in search:
        response = 'I am Cookie. The Virtual Assistant. Version 1.0'
    elif 'hey cookie what is the time' in search:
        response = ctime()
    elif 'what is the time cookie' in search:
        response = ctime()
    elif 'what is the time' in search:
        response = ctime()
    elif 'hey cookie what time is it' in search:
        response = ctime()
    elif 'what time is it cookie' in search:
        response = ctime()
    elif 'tell me the time cookie' in search:
        response = ctime()
    elif 'hey cookie tell me the time' in search:
        response = ctime()
    else:
        response = "Sorry I can't understand you!!.. Try searching in the Google option."
    return response
