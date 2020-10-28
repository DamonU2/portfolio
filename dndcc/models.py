from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Player(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username

class Character(models.Model):
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

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    clss = models.CharField(max_length=9, choices=CLASSES)
    level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

    stn = models.PositiveSmallIntegerField("strength", choices=ABILITY)
    dex = models.PositiveSmallIntegerField("dexterity", choices=ABILITY)
    con = models.PositiveSmallIntegerField("constitution", choices=ABILITY)
    inl = models.PositiveSmallIntegerField("intelligence", choices=ABILITY)
    wis = models.PositiveSmallIntegerField("wisdom", choices=ABILITY)
    cha = models.PositiveSmallIntegerField("charisma", choices=ABILITY)
    
    class Meta:
        ordering = ["level"]

    def __str__(self):
        return self.name

class Spell(models.Model):
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

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    diceNum = models.PositiveSmallIntegerField(choices=DICENUM)
    diceType = models.PositiveSmallIntegerField(choices=DICE)
    damType = models.CharField(max_length=11, choices=DAMAGE)

class Weapon(models.Model):
    DICE = (
        (4, 'd4'),
        (6, 'd6'),
        (8, 'd8'),
        (10, 'd10'),
        (12, 'd12'),
    )

    BONUS = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
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

    MOD = (
        ('stn', 'Strength'),
        ('dex', 'Dexterity'),
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

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    bonus = models.PositiveSmallIntegerField(choices=BONUS)
    prof = models.BooleanField
    mod = models.CharField(max_length=3, choices=MOD)
    diceNum = models.PositiveSmallIntegerField("diceNum", choices=DICENUM)
    diceType = models.PositiveSmallIntegerField(choices=DICE)
    damType = models.CharField(max_length=11, choices=DAMAGE)