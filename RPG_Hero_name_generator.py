import random
from time import sleep
sleep_value = 2

user_name_lenght = int(input("Give Your hero name lenght (please use even number): "))
user_alignment = input('Are You "good" or "bad": ')

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
nickname = nickname_generator(user_alignment)

if name_out[-1] == 'a':
    he_she = 'she'
else:
    he_she = 'he'

# def story(how_long):
#     x = 0
#     if x in range(0, how_long):


print('Your hero is created')
sleep(sleep_value)
print(f'{he_she.capitalize()} is called {name_out} the {nickname}')
sleep(sleep_value)

our_hero = name_out + ' the ' + nickname