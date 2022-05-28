# Lets beggin with RPG Heroe name
# Generator imienia dla Wojownika RPG:
#
#     Konieczność użycia modułu random.
#     Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek
#     (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
#     Pomysł jest zainspirowany grą: http://progressquest.com/play/roster.html
#     Imię musi zaczynać się od wielkiej litery.
#     Program można kontynuować używając pomysłu poniżej.


import random

name_parts = ['ab', 'ce', 'on', 'lu', 'xu', 'yun', 'mun', 'pi', 'ur', 'os', ]

generated_name = []

a = random.choice(name_parts)
b = random.choice(name_parts)
c = random.choice(name_parts)
d = random.choice(name_parts)

generated_name.append(a)
generated_name.append(b)
generated_name.append(c)
generated_name.append(d)

print(generated_name)

name_out = ' '.join(generated_name)
name_out = name_out.replace(' ', '')
name_out = name_out.capitalize()
print(name_out)


