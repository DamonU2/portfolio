from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index/home.html')

def BJ(request):
    return render(request, 'index/blackjack.html')