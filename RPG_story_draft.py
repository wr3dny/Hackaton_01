# Historyjka a'la RPG:
#
#     Konieczność użycia modułu random.
#     Program wypisuje kolejne "przygody" bohatera.
#     Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami,
#     np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy
#     poszedł do tawerny aby zasnąć."
#     Historyjka ma mieć zadaną długość i ma być możliwie losowa.

import random

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'n', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y']

name_parts = ['bo', 'ce', 'na', 'lu', 'xu', 'pi', 'ra', 'sa', 'ut', 'zo', 'mi', 'wa']

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
destinations_to_meet = ['inn', 'old castle', 'dwarven mine', 'town square']

actions = random.choice(actions_to_happen)
movement = random.choice(movement_to_happen)
destinations = random.choice(destinations_to_meet)

print(name_out)

if name_out[-1] == a:
    he_she = 'she'
else:
    he_she = 'he'


print(f'So our story begins when {our_heroe} stepped outside the tavern "Saturday\'s Hangover".')
print(f'{he_she.capitalize()} looked around {movement} and {actions}.')

movement_to_happen = ['moved 20 paces north', 'moved 30 paces south']
actions_to_happen = ['took a big breath', 'spited out', 'attacked wolverine', 'attacked pixie',
                     'shouted at nearest person', 'died']
destinations_to_meet = ['inn', 'old castle', 'dwarven mine', 'town square']

actions = random.choice(actions_to_happen)
movement = random.choice(movement_to_happen)
destinations = random.choice(destinations_to_meet)

print(f'After that {he_she} {actions} and {movement}.')

actions = random.choice(actions_to_happen)
movement = random.choice(movement_to_happen)
destinations = random.choice(destinations_to_meet)

print(f'{destinations.capitalize()} was opportunity for some coins, so {he_she} {actions} but first {he_she} had to {movement}')
