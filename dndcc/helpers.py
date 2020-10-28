import os
import random

from django.shortcuts import render, redirect
from functools import wraps

# Make sure player is logged in
def player_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if request.session['playerid'] is None:
            return redirect('cclogin')
        return f(request, *args, **kwargs)
    return decorated_function

# Make sure character is selected
def char_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if request.session['charid'] is None:
            return redirect('ccindex')
        return f(request, *args, **kwargs)
    return decorated_function

# Function for any diceroll
def dice_roll(dicetype):
    number = random.randint(1, dicetype)
    return number

def player_login(request, player):
    request.session['charid'] = None
    request.session['playerid'] = player.pk
    request.session['username'] = player.username

#Calculate ability modifiers function
def mod(ability):
    return (ability-10)//2