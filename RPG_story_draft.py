# Historyjka a'la RPG:
#
#     Konieczność użycia modułu random.
#     Program wypisuje kolejne "przygody" bohatera.
#     Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami,
#     np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy
#     poszedł do tawerny aby zasnąć."
#     Historyjka ma mieć zadaną długość i ma być możliwie losowa.

import random

name_parts = ['ab', 'ce', 'on', 'lu', 'xu', 'pi', 'ur', 'os', 'ut', 'zo', 'mi', 'wa']

generated_name = []

a = random.choice(name_parts)
b = random.choice(name_parts)
c = random.choice(name_parts)
d = random.choice(name_parts)

generated_name.append(a)
generated_name.append(b)
generated_name.append(c)
generated_name.append(d)

name_out = ' '.join(generated_name)
name_out = name_out.replace(' ', '')
name_out = name_out.capitalize()


nickname_base = ['Handsome', 'Bold', 'Decayed', 'Lazy', 'Oathbreaker', 'Unpleasant', 'Big', 'Necromancer', 'Blackheart']
nickname = random.choice(nickname_base)
our_heroe = str(name_out + ' the ' + nickname)
print(f'Your heroe is called {our_heroe}')
print()

movement_to_happen = ['moved 20 paces north', 'moved 30 paces south', 'shouted at nearest person', 'died']
actions_to_happen = ['took a big breath', 'spited out', 'attacked wolverine', 'attacked pixie']

actions = random.choice(actions_to_happen)
movement = movement_to_happen

if name_out[-1] == a:
    sex = 'female'
else:
    sex = 'male'

if sex == 'female':
    he_she = 'she'
else:
    he_she = 'he'



print(f'So our story begins when {our_heroe} stepped outside the tavern "Saturday\'s Hangover".')
print(f'{he_she.capitalize()} looked around {movement_to_happen} and {actions_to_happen}')
