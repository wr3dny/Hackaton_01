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
        name_length = int(input('Pick up Your number again: '))
    else:
        j = 0
        for j in range(0, int(name_lenght/2)):
            generated_name.append(random.choice(name_parts))
            j += 1

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


name_out = name_generator(user_name_lenght)
nickname = nickname_generator(user_alignment)

if name_out[-1] == 'a':
    he_she = 'she'
else:
    he_she = 'he'

print('Your hero is created')
sleep(1)
print(f'{he_she.capitalize()} is called {name_out} the {nickname}')
sleep(sleep_value)

our_hero = name_out + ' the ' + nickname

def story_rows(yes_no):
    possible_directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
    who_random = ['pixie', 'banshee', 'werewolf', 'skeleton', 'zombie', 'dwarf', 'bestigor', 'goblin', 'skaven']
    occupations_random = [' bodyguard', ' hangman', ' tax collector', ' miner', ' mime', ' innkeeper', ' gardener',
                          ' servant', ' shaman', ' archer', ' cook', ' ring bearer', ' troll slayer']
    possible_place = ['inn', 'old castle', 'deep dwarven mine', 'town square', 'shadowy forrest', 'wide road',
                      'godforsaken village', 'seashore', 'abandoned graveyard', 'unicorn glade', ]
    actions_to_happen = ['attacked ', 'spited on ', 'brawled with ', 'whistle at ', 'argue with ', ]

    line_1 = f'So our story begins when {our_hero} stepped outside the tavern "Saturday\'s Hangover".'
    line_2 = f'{he_she.capitalize()} looked around and {random.choice(actions_to_happen)}' \
             f'{random.choice(who_random) + random.choice(occupations_random)} and ' \
             f'{random.choice(actions_to_happen)}{random.choice(who_random) + random.choice(occupations_random)}.'
    line_3 = f'After that {he_she} {random.choice(actions_to_happen)}' \
             f'{random.choice(who_random) + random.choice(occupations_random)} and moved ' \
             f'{random.choice(possible_directions)}, traveling with companion of ' \
             f'{random.choice(who_random) + random.choice(occupations_random)}.'
    line_4 = f'{random.choice(possible_place).capitalize()} was opportunity for some coins, so {he_she} ' \
             f'{random.choice(actions_to_happen)}{random.choice(who_random) + random.choice(occupations_random)},' \
             f' then {he_she} had to travel for {random.randrange(1, 8)} hours {random.choice(possible_directions)}'
    line_5 = f'The journey took its tall, but the view of {random.choice(possible_place)} was magnificent, even with ' \
             f'a pair of {random.choice(who_random) + random.choice(occupations_random)} standing in the way. '
    line_6 = f'Whole adventures day made {our_hero} tired, so {he_she} found a {random.choice(possible_place)} ' \
             f'to rest before next heroic day.'
    line_7 = 'The End'
    yes_no = yes_no.lower()
    if yes_no == 'yes':
        print(line_1)
        sleep(2)
        print(line_2)
        sleep(2)
        print(line_3)
        sleep(2)
        print(line_4)
        sleep(2)
        print(line_5)
        sleep(2)
        print(line_6)
        sleep(2)
        print(line_7)
    elif yes_no == 'no':
        print('So You don\'t want to know the tale')
    else:
        print('That is not the correct answer.')

user_rows = input('Do You want to hear the tale (yes/no) : ')
story_rows(user_rows)

