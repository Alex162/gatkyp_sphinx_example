# Resource: https://medium.com/@rahulkumarmk/10-fun-python-scripts-that-generate-random-stories-e40477acb3d8

import random
characters = ['Cowboy', 'Outlaw', 'Sheriff', 'Bounty Hunter']
settings = ['Saloon', 'Desert', 'Town', 'Ranch']
actions = ['Shoot', 'Rob', 'Capture', 'Escape']
objects = ['Pistol', 'Horse', 'Money Bag', 'Whiskey Bottle']
character = random.choice(characters)
setting = random.choice(settings)
action = random.choice(actions)
object = random.choice(objects)
story = f"{character} is on a mission to {action} a {setting} using a {object}, but must face off against {random.choice(characters)} in a showdown at high noon.\n"
print(story)


import random
characters = ['Captain', 'Alien', 'Robot', 'Scientist']
settings = ['Spaceship', 'Space Station', 'Exoplanet', 'Black Hole']
challenges = ['Invasion', 'Exploration', 'Survival', 'Time Travel']
character1 = random.choice(characters)
character2 = random.choice(characters)
while character2 == character1:
    character2 = random.choice(characters)
setting = random.choice(settings)
challenge = random.choice(challenges)
story = f"{character1} and {character2} embark on a mission to {challenge} a {setting}, using advanced technology to overcome the challenges of space travel. But when they arrive, they discover a threat more dangerous than they ever imagined.\n"
print(story)
