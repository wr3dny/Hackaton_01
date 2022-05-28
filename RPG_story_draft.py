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
sleep_value = 2

user_name_lenght = int(input("Give Your heroe name lenght (please use even number): "))
user_aligmnet = input('Are You "good" or "bad": ')

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
    if abs(name_lenght % 2 != 0):
            print('You picked and odd number')
            name_length = int(input('Pick up Your number again: '))
    else:
        i = 0
        for i in range(0, int(name_lenght/2)):
            generated_name.append(random.choice(name_parts))
            i += 1

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
        #     break
        # else:
        #     print('You picked up wrong')
        return nickname


name_out = name_generator(user_name_lenght)
nickname = nickname_generator(user_aligmnet)

if name_out[-1] == 'a':
    he_she = 'she'
else:
    he_she = 'he'

# def story(how_long):
#     x = 0
#     if x in range(0, how_long):


print('Your heroe is created')
sleep(sleep_value)
print(f'{he_she.capitalize()} is called {name_out} the {nickname}')
sleep(sleep_value)

our_heroe = name_out + ' the ' + nickname

print(f'So our story begins when {our_heroe} stepped outside the tavern "Saturday\'s Hangover".')

possible_directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
who_random = ['pixie', 'wolverine ', 'wherewolf', 'skeleton', 'zombie', 'dwarf', 'bestigor', 'goblin']
occupations_random = [' bodyguard', ' hangman', ' tax collector', ' miner', ' mime', ' inkeeper', ' gardener',
                      ' servant', ' shaman']
possible_place = ['inn', 'old castle', 'deep dwarven mine', 'town square', 'shadowy forrest', 'wide road',
                  'godforsaken village', 'seashore']
actions_to_happen = ['attacked ', 'spited on ', 'brawled with ', 'whistle at ', 'argue with ', ]



sleep(sleep_value)
print(f'{he_she.capitalize()} looked around and {random.choice(actions_to_happen)}{random.choice(who_random) + random.choice(occupations_random)} and '
      f'{random.choice(actions_to_happen)}{random.choice(who_random) + random.choice(occupations_random)}.')

sleep(sleep_value)
print(f'After that {he_she} {random.choice(actions_to_happen)}{random.choice(who_random) + random.choice(occupations_random)} and moved {random.choice(possible_directions)}, traveling with companion of {random.choice(who_random) + random.choice(occupations_random)}.')

sleep(sleep_value)
print(f'{random.choice(possible_place).capitalize()} was opportunity for some coins, so {he_she} {random.choice(actions_to_happen)}{random.choice(who_random) + random.choice(occupations_random)}, then {he_she} had to move {random.randrange(2, 1500)}'
      f' meters {random.choice(possible_directions)}')

sleep(sleep_value)
print(f'The travel took some time, but the view of {random.choice(possible_place)} was magnificent, even with of {random.choice(who_random) + random.choice(occupations_random)} in view. ')

sleep(sleep_value)

print(f'Whole adventures day made {our_heroe} tired, so {he_she} found a {random.choice(possible_place)} to rest before next day.')




#
# user_long = int(input('How long (in rows) should be the story: '))
# story(user_long)


