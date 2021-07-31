

import random

friendsList = [
    'Ram',
    'John',
    'Adam',
    'Naman',
    'Sunakshi',
    'Skye',
    'Mack',
    'Jamie',
    'Nadiya'
]

# random.randint(1, 9) --> random number between 1 and 9
# random.choice(list) --> random item in this list

callSelected = random.choice(friendsList) # randomly chooses a friend

print('Who should I Whatsapp Call today?')
print(callSelected)