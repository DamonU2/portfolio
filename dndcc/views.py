from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Player, Character, Spell, Weapon
from .forms import RegisterForm, LoginForm, CharacterForm, UpdateForm, SpellForm, WeaponForm
from .helpers import player_required, char_required, player_login, mod, dice_roll


def ccregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if request.POST['password'] != request.POST['password2']:
                messages.warning(request, 'Passwords do not match')
            else:
                new_player = Player()
                new_player.username = request.POST['username']
                new_player.password = make_password(request.POST['password'])
                new_player.save()
                player_login(request, new_player)
                return redirect('ccindex')
    else:
        form = RegisterForm()
    return render(request, 'dndcc/ccregister.html', {'form': form})


def cclogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if Player.objects.filter(username=request.POST['username']):
            player = Player.objects.get(username=request.POST['username'])
            if check_password(request.POST['password'], player.password):
                player_login(request, player)
                return redirect('ccindex')
            else:
                messages.warning(request, 'Password does not match username')
        else:
            messages.warning(request, 'Username does not exist')
    else:
        form = LoginForm()
    return render(request, 'dndcc/cclogin.html', {"form": form})

@player_required
def cclogout(request):
    request.session['playerid'] = None
    request.session['charid'] = None
    request.session['username'] = None
    return redirect('cclogin')


@player_required
def ccindex(request):
    char = Character.objects.filter(player=request.session['playerid'])
    if char == None:
        return redirect('new_character')
    else:
        return render(request, 'dndcc/ccindex.html', {"char": char})

@player_required
def new_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            new_character = form.save(commit=False)
            new_character.player = Player.objects.get(pk=request.session['playerid'])
            new_character.save()
            return redirect('ccindex')
    else:
        form = CharacterForm()
    return render(request, 'dndcc/new_character.html', {"form": form})

@player_required
def delete_character(request):
    if request.method == 'POST':
        pk = request.POST['del_char']
        character = get_object_or_404(Character, pk=pk)
        character.delete()
    return redirect('ccindex')

@player_required
def character(request):
    if request.method == 'POST':
        request.session["charid"] = request.POST['char']
    pk = request.session["charid"]
    character = get_object_or_404(Character, pk=pk)
    weapons = Weapon.objects.filter(character=pk)
    spells = Spell.objects.filter(character=pk)
    context = {'character': character, 'weapons': weapons, 'spells': spells}
    return render(request, 'dndcc/character.html', context)

@char_required
@player_required
def ccupdate(request):
    character = get_object_or_404(Character, pk=request.session['charid'])
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            return redirect('character')
    else:
        form = UpdateForm()
    context = {"form": form, "character": character}
    return render(request, 'dndcc/ccupdate.html', context)

@char_required
@player_required
def spell(request):
    if request.method == 'POST':
        form = SpellForm(request.POST)
        if form.is_valid():
            new_spell = form.save(commit=False)
            new_spell.character = Character.objects.get(pk=request.session['charid'])
            new_spell.save()
            return redirect('character')
    else:
        form = SpellForm()
    return render(request, 'dndcc/spell.html', {"form": form})

@char_required
@player_required
def weapon(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            new_weapon = form.save(commit=False)
            new_weapon.character = Character.objects.get(pk=request.session['charid'])
            new_weapon.save()
            return redirect('character')
    else:
        form = WeaponForm()
    return render(request, 'dndcc/weapon.html', {"form": form})

@char_required
@player_required
def delete_spell(request):
    if request.method == 'POST':
        pk = request.POST['del_spell']
        spell = get_object_or_404(Spell, pk=pk)
        spell.delete()
    return redirect('character')

@char_required
@player_required
def delete_weapon(request):
    if request.method == 'POST':
        pk = request.POST['del_weap']
        weapon = get_object_or_404(Weapon, pk=pk)
        weapon.delete()
    return redirect('character')

@char_required
@player_required
def combat(request):
    character = get_object_or_404(Character, pk=request.session['charid'])
    weapons = Weapon.objects.filter(character=request.session['charid'])
    spells = Spell.objects.filter(character=request.session['charid'])
    context = {'character': character, 'weapons': weapons, 'spells': spells}
    return render(request, 'dndcc/combat.html', context)

@char_required
@player_required
def init(request):
    character = get_object_or_404(Character, pk=request.session['charid'])
    dex_mod = mod(character.dex)
    roll = dice_roll(20)
    messages.warning(request, "You rolled {}, plus {}, gives initiative of {}" .format(roll, dex_mod, dex_mod + roll))
    return redirect('combat')

@char_required
@player_required
def weapon_attack(request):
    weapon = get_object_or_404(Weapon, pk=request.POST['weapon_attack'])
    character = get_object_or_404(Character, pk=request.session['charid'])
    if weapon.prof:
        prof = ((character.level - 1) // 4) + 2
    else:
        prof = 0
    att = mod(getattr(character, weapon.mod))
    damage = 0
    roll = dice_roll(20)
    # Special scenario if 20 or 1 are rolled
    if roll == 20:
        # Damage dice are doubled for a critical hit
        dicenum = weapon.diceNum * 2
        # Roll damage dice dicenum times
        for i in range(0, dicenum):
            damage += dice_roll(weapon.diceType)
        # Add bonus and attribute bonus to damage
        damage = damage + weapon.bonus + att
        # Display roll info in alert
        messages.warning(request, "Critical Hit for {} {} damage!".format(damage, weapon.damType))
    elif roll == 1:
        # If a one is rolled, no further calculations are necessary
        messages.warning(request, "1! Miss!")
    else:
        # Roll damage die dicenum times
        for i in range(0, weapon.diceNum):
            damage += dice_roll(weapon.diceType)
        # Add bonuses to damage
        damage = damage + weapon.bonus + att
        # Display roll info
        messages.warning(request, "Attack roll of {}, plus {} is {}. If the attack hits, it does {} {} damage".format(roll, weapon.bonus + att + prof, roll + weapon.bonus + att + prof, damage, weapon.damType))
    return redirect('combat')


@char_required
@player_required
def spell_attack(request):
    spell = get_object_or_404(Spell, pk=request.POST['spell_attack'])
    character = get_object_or_404(Character, pk=request.session['charid'])
    prof = ((character.level - 1) // 4) + 2
    ab = 0
    # Determines spell ability modifier based on class
    if character.clss == "Bard" or character.clss == "Sorcerer" or character.clss == "Paladin" or character.clss == "Warlock":
        ab = mod(character.cha)
    elif character.clss == "Wizard" or character.clss == "Fighter" or character.clss == "Rogue":
        ab = mod(character.inl)
    else:
        ab = mod(character.wis)
    damage = 0
    # Roll 20 sided dice
    roll = dice_roll(20)
    # Special scenario if 20 or 1 are rolled
    if roll == 20:
        # Damage dice are doubled for a critical hit
        dicenum = spell.diceNum * 2
        # Roll damage die dicenum times
        for i in range(0, dicenum):
            damage += dice_roll(spell.diceType)
        # Display roll info
        messages.warning(request, "Critical Hit for {} {} damage!".format(damage, spell.damType))
    elif roll == 1:
        # If a one is rolled, no further calculations are necessary
        messages.warning(request, "1! Miss!")
    else:
        # Roll damage die dicenum times
        for i in range(0, spell.diceNum):
            damage += dice_roll(spell.diceType)
        # Display roll info
        messages.warning(request, "Attack roll of {}, plus {} is {}. If the attack hits, it does {} {} damage".format(roll, ab + prof, roll + ab + prof, damage, spell.damType))
    return redirect('combat')

@char_required
@player_required
def saving_throw(request):
    attribute = request.POST['saving_throw']
    character = get_object_or_404(Character, pk=request.session['charid'])
    prof = ((character.level - 1) // 4) + 2
    att = mod(getattr(character, attribute))
    # Adds saving throw proficiencies to attribute mocifiers according to class bonuses 
    if attribute == "stn":
        if character.clss == "Barbarian" or character.clss == "Fighter" or character.clss == "Monk" or character.clss == "Ranger":
            att += prof
    elif attribute == "dex":
        if character.clss == "Bard" or character.clss == "Monk" or character.clss == "Ranger" or character.clss == "Rogue":
            att += prof
    elif attribute == "con":
        if character.clss == "Barbarian" or character.clss == "Fighter" or character.clss == "Sorcerer":
            att += prof
    elif attribute == "inl":
        if character.clss == "Druid" or character.clss == "Rogue" or character.clss == "Wizard":
            att += prof
    elif attribute == "wis":
        if character.clss == "Cleric" or character.clss == "Druid" or character.clss == "Paladin" or character.clss == "Warlock" or character.clss == "Wizard":
            att += prof
    elif attribute == "cha":
        if character.clss == "Bard" or character.clss == "Cleric" or character.clss == "Paladin" or character.clss == "Sorcerer" or character.clss == "Warlock":
            att += prof
    # Roll 20 sided die
    roll = dice_roll(20)
    # Flash roll info in alert
    messages.warning(request, "You rolled {}, plus {}, gives {}" .format(roll, att, att + roll))
    return redirect('combat')