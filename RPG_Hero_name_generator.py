# Generator imienia dla Wojownika RPG:
#
#     Konieczność użycia modułu random.
#     Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek
#     (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
#     Pomysł jest zainspirowany grą: http://progressquest.com/play/roster.html
#     Imię musi zaczynać się od wielkiej litery.
#     Program można kontynuować używając pomysłu poniże

import random
from time import sleep

user_name_lenght = int(input("Give Your hero name length (please use even number): "))
user_alignment = input('Are You "good" or "evil": ')

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'n', 'q', 's', 't', 'v',
             'x', 'z', 'h', 'r', 'w', 'y']
name_parts = []
i = 0
while i <= 200:
    vr = random.choice(vowel)
    cr = random.choice(consonant)
    syllables = cr + vr
    name_parts.append(syllables)
    i += 1
    name_parts = list(set(name_parts))

def name_generator(name_lenght):
    generated_name = []
    if abs(name_lenght % 2 != 0):
        print('You picked and odd number')
    else:
        j = 0
        for j in range(0, int(name_lenght/2)):
            generated_name.append(random.choice(name_parts))
            j += 1

    name_out: str = ' '.join(generated_name)
    name_out = name_out.replace(' ', '')
    name_out = name_out.capitalize()
    return name_out

    name_out: str = ' '.join(generated_name)
    name_out = name_out.replace(' ', '')
    name_out = name_out.capitalize()
    return name_out


def nickname_generator(alignment):
    if alignment == 'good':
        nickname_good = ['Handsome', 'Bold', 'Big', 'Swift', 'Pure', 'Fair', 'Peacebringer']
        nickname = random.choice(nickname_good)
    elif alignment == 'evil':
        nickname_evil = ['Decayed', 'Sinister', 'Oathbreaker', 'Unpleasant', 'Blackheart', 'Wicked', 'Skullcrusher']
        nickname = random.choice(nickname_evil)
    else:
        print('You picked up wrong - only good and evil are worthy of choice')

    return nickname


nickname = nickname_generator(user_alignment)
name_out = name_generator(user_name_lenght)

if name_out[-1] == 'a':
    he_she = 'she'
else:
    he_she = 'he'

print('Your hero is created')
sleep(1)
print(f'{he_she.capitalize()} is called {name_out} the {nickname}')
sleep(2)

our_hero = name_out + ' the ' + nickname