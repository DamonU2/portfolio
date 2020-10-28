from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import MaxValueValidator, MinValueValidator

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Div

from .models import Player, Character, Spell, Weapon


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label = "Username",
        max_length = 32,
        required = True
    )

    password = forms.CharField(
        label = "Password",
        max_length = 32,
        required = True,
        widget = forms.PasswordInput
    )

    password2 = forms.CharField(
        label = "Confirm Password",
        max_length = 32,
        required = True,
        widget = forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Sign up', 'Sign up', css_class='btn-secondary'))
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False

    class Meta:
        model = Player
        fields = ('username', 'password', 'password2',)


class LoginForm(AuthenticationForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Log In', 'Log In', css_class='btn-secondary'))
    class Meta:
        model = Player
        fields = ('username', 'password',)

class CharacterForm(forms.ModelForm):
    CLASSES = (
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard'),
    )

    ABILITY = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
    )

    LEVEL = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
    )

    name = forms.CharField(
        label = "Name",
        max_length = 32,
        required = True
    )

    clss = forms.ChoiceField(
        label = "Class",
        choices = CLASSES,
        required = True
    )

    level = forms.ChoiceField(
        label = "Level",
        choices = LEVEL,
        initial = 1,
        required = True
    )

    stn = forms.ChoiceField(
        label = "Strength",
        choices = ABILITY,
        required = True,
        initial = 12
    )

    dex = forms.ChoiceField(
        label = "Dexterity",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    con = forms.ChoiceField(
        label = "Constitution",
        choices = ABILITY,
        required = True,
        initial = 12
    )

    inl = forms.ChoiceField(
        label = "Intelligence",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    wis = forms.ChoiceField(
        label = "Wisdom",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    cha = forms.ChoiceField(
        label = "Charisma",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Create', 'Create', css_class='btn-secondary'))
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False
        self.helper.layout = Layout(
            Div(Row('name', 'level', 'clss')),
            Row(Column('stn', 'dex', 'con'), 
                Column('inl', 'wis', 'cha')
            )
        )

    class Meta:
        model = Character
        fields = ['name', 'level', 'clss', 'stn', 'dex', 'con', 'inl', 'wis', 'cha']

class UpdateForm(forms.ModelForm):

    ABILITY = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
    )

    LEVEL = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
    )

    level = forms.ChoiceField(
        label = "Level",
        choices = LEVEL,
        initial = 1,
        required = True
    )

    stn = forms.ChoiceField(
        label = "Strength",
        choices = ABILITY,
        required = True,
        initial = 12
    )

    dex = forms.ChoiceField(
        label = "Dexterity",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    con = forms.ChoiceField(
        label = "Constitution",
        choices = ABILITY,
        required = True,
        initial = 12
    )

    inl = forms.ChoiceField(
        label = "Intelligence",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    wis = forms.ChoiceField(
        label = "Wisdom",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    cha = forms.ChoiceField(
        label = "Charisma",
        choices = LEVEL,
        required = True,
        initial = 12
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Update', 'Update', css_class='btn-secondary'))
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False
        self.helper.layout = Layout(
            Div(Row('level')),
            Row(Column('stn', 'dex', 'con'), 
                Column('inl', 'wis', 'cha')
            )
        )

    class Meta:
        model = Character
        fields = ['level', 'stn', 'dex', 'con', 'inl', 'wis', 'cha']

class SpellForm(forms.ModelForm):
    DICE = (
        (4, 'd4'),
        (6, 'd6'),
        (8, 'd8'),
        (10, 'd10'),
        (12, 'd12'),
    )

    DICENUM = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
    )

    DAMAGE = (
        ('acid', 'acid'),
        ('bludgeoning', 'bludgeoning'),
        ('cold', 'cold'),
        ('fire', 'fire'),
        ('force', 'force'),
        ('lightning', 'lightning'),
        ('necrotic', 'necrotic'),
        ('piercing', 'piercing'),
        ('poison', 'poison'),
        ('psychic', 'psychic'),
        ('radiant', 'radiant'),
        ('slashing', 'slashing'),
        ('thunder', 'thunder'),
    )

    name = forms.CharField(
        label = "Name",
        max_length = 32,
        required = True
    )

    diceNum = forms.ChoiceField(
        label = "Dice",
        choices = DICENUM,
        required = True
    )

    diceType = forms.ChoiceField(
        label = "",
        choices = DICE,
        required = True
    )

    damType = forms.ChoiceField(
        label = "Damage Type",
        choices = DAMAGE,
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Create', 'Create', css_class='btn-secondary'))
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False
        self.helper.layout = Layout(
            
        )

    class Meta:
        model = Spell
        fields = ['name', 'diceNum', 'diceType', 'damType']

class WeaponForm(forms.ModelForm):
    MOD = (
        ('stn', 'Strength'),
        ('dex', 'Dexterity'),
    )

    BONUS = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    DICE = (
        (4, 'd4'),
        (6, 'd6'),
        (8, 'd8'),
        (10, 'd10'),
        (12, 'd12'),
    )

    DICENUM = (
        (1, '1'),
        (2, '2'),
    )

    DAMAGE = (
        ('acid', 'acid'),
        ('bludgeoning', 'bludgeoning'),
        ('cold', 'cold'),
        ('fire', 'fire'),
        ('force', 'force'),
        ('lightning', 'lightning'),
        ('necrotic', 'necrotic'),
        ('piercing', 'piercing'),
        ('poison', 'poison'),
        ('psychic', 'psychic'),
        ('radiant', 'radiant'),
        ('slashing', 'slashing'),
        ('thunder', 'thunder'),
    )

    name = forms.CharField(
        label = "Name",
        max_length = 32,
        required = True
    )

    prof = forms.BooleanField(
        label = "Proficient With?"
    )

    bonus = forms.ChoiceField(
        label = "Bonus",
        choices = BONUS,
        required = True
    )

    mod = forms.ChoiceField(
        label = "Ability Modifier",
        choices = MOD,
        required = True
    )

    diceNum = forms.ChoiceField(
        label = "Dice",
        choices = DICENUM,
        required = True
    )

    diceType = forms.ChoiceField(
        label = "",
        choices = DICE,
        required = True
    )

    damType = forms.ChoiceField(
        label = "Damage Type",
        choices = DAMAGE,
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Create', 'Create', css_class='btn-secondary'))
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False
        self.helper.layout = Layout(
            
        )

    class Meta:
        model = Weapon
        fields = ['name', 'prof', 'mod', 'bonus', 'diceNum', 'diceType', 'damType']