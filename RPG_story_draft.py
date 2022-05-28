# Historyjka a'la RPG:
#
#     Konieczność użycia modułu random.
#     Program wypisuje kolejne "przygody" bohatera.
#     Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami,
#     np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy
#     poszedł do tawerny aby zasnąć."
#     Historyjka ma mieć zadaną długość i ma być możliwie losowa.

import random
from time import sleep

user_name_lenght = int(input("Give Your heroe name lenght (please use even number): "))
user_aligmnet = input('Are You "good" or "bad"')

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'n', 'q', 's', 't', 'v',
             'x', 'z', 'h', 'r', 'w', 'y']
name_parts = []
i = 0
while i <= 105:
    vr = random.choice(vowel)
    cr = random.choice(consonant)
    syllables = cr + vr
    name_parts.append(syllables)
    i += 1
    name_parts = list(set(name_parts))

def name_generator(name_lenght):
    generated_name = []
    while True:
        if abs(name_lenght % 2 != 0):
            print('You picked and odd number')
        else:
            i = 0
            for i in range(0, int(name_lenght/2)):
                generated_name.append(random.choice(name_parts))
                i += 1
            break
    name_out: str = ' '.join(generated_name)
    name_out = name_out.replace(' ', '')
    name_out = name_out.capitalize()
    return name_out

def nickname_generator(alignment):
    while True:
        if alignment == 'good':
            nickname_good = ['Handsome', 'Bold', 'Big', 'Swift', 'Pure', 'Fair']
            nickname = random.choice(nickname_good)
        elif alignment == 'bad':
            nickname_bad = ['Decayed', 'Sinister', 'Oathbreaker', 'Unpleasant', 'Blackheart', 'Wicked']
            nickname = random.choice(nickname_bad)
            break
        else:
            print('You picked up wrong')
    return nickname


name_out = name_generator(user_name_lenght)
nickname = nickname_generator(user_aligmnet)

if name_out[-1] == 'a':
    he_she = 'she'
else:
    he_she = 'he'

print('Your heroe is created')
print(f'{he_she.capitalize()} is called {name_out} the {nickname}')







# nickname_base = ['Handsome', 'Bold', 'Decayed', 'Lazy', 'Oathbreaker', 'Unpleasant', 'Big', 'Necromancer', 'Blackheart']
# nickname = random.choice(nickname_base)
# our_heroe = str(name_out + ' the ' + nickname)
# print(f'Your heroe is called {our_heroe}')
# print()
#

#
# distance = random.randrange(1, 100)
# possible_directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
# actions_to_happen = ['took a big breath', 'spited out', 'attacked wolverine', 'attacked pixie',
#                      'shouted at nearest person', 'fall a sleep', 'brawled with NPC', ]
# # attacked_things = ['pixie', 'wolverine','wherewolf','skeleton', 'zombie', 'chaos dwarf', 'nurgle spawn', 'goblin',
# # 'human bodyguard', 'hangman', 'tax collector']
# possible_place = ['inn', 'old castle', 'deep dwarven mine', 'town square', 'shadowy forrest', 'wide road',
#                   'godforsaken village', 'seashore']
#
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
#
# print(f'1 So our story begins when {our_heroe} stepped outside the tavern "Saturday\'s Hangover".')
# sleep(2)
# print(f'2 {he_she.capitalize()} looked around {random.choice(actions_to_happen)} and {random.choice(actions_to_happen)}.')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
# print(f'3 After that {he_she} {action} and moved {direction} .')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
#
# print(f'4 {place.capitalize()} was opportunity for some coins, so {he_she} {action} , then {he_she} '
#       f'had to move {distance} {direction}')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
#
# print(f'5 The {place} was opportunity for some coins, so {he_she} {action} , then {he_she} '
#       f'had to move {distance} {direction}')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
#
# print(f'6 The {place} was opportunity for some coins, so {he_she} {action} , then {he_she} '
#       f'had to move {distance} {direction}')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
#
# print(f'7 The {place} was opportunity for some coins, so {he_she} {action} , then {he_she} '
#       f'had to move {distance} {direction}')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'
#
# print(f'8 The {place} was opportunity for some coins, so {he_she} {action} , then {he_she} '
#       f'had to move {distance} {direction}')
# sleep(2)
# action = random.choice(actions_to_happen)
# direction = random.choice(possible_directions)
# place = random.choice(possible_place)
# distance = str(distance) + ' paces'

# def randomized (all):
#     action = random.choice(actions_to_happen)
#     direction = random.choice(possible_directions)
#     place = random.choice(possible_place)
#     distance = random.randrange(1, 100)
#     distance = str(distance) + ' paces'

