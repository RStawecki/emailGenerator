from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def email(request):
    numbers = '0123456789'
    lowerLetters = 'abcdefghijklmnoprstuwxyz'
    upperLetters = lowerLetters.upper()
    strNumbers = lowerLetters + upperLetters
    
    if request.GET.get("numbers"):
        strNumbers += numbers
    length = int(request.GET.get('length'))
    email = ''
    for _ in range(length):
        el = random.choice(strNumbers)
        email += el
    #domains = ['@wp.pl', '@gmail.com', '@poczta.fm']
    domain = request.GET.get('domain')
    email += domain

    return render(request, 'generator/email.html', {'email': email})
