import time, os
from Classes.Roles import Tank, Warrior
from Classes.Items import *
from Functions.inputs import anyKeyPressed 

Ornn = Tank('Ornn',3)
Garen = Warrior('Garen',3)

item1 = BlackCleaver()
item3 = Thornmail()

Ornn.gainItem(item3)
Garen.gainItem(item1)

os.system('cls')

print(Garen.lifeBar)
print(Ornn.lifeBar)
time.sleep(1)

print('begin X1')

time.sleep(1)
os.system('cls')

while Ornn.hp > 0 and Garen.hp > 0:

    print(Garen.lifeBar)
    print(Ornn.lifeBar)
    Ornn.autoAttack(Garen)
    Garen.lifeBar.update(Garen)

    anyKeyPressed()
    os.system('cls')

    print(Garen.lifeBar)
    print(Ornn.lifeBar)
    Garen.autoAttack(Ornn)
    Ornn.lifeBar.update(Ornn)

    anyKeyPressed()
    os.system('cls')