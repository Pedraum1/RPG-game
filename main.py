import time, os
from Classes.Roles import Assassin, Warrior
from Classes.Items import *
from Functions.inputs import anyKeyPressed 

Zed = Assassin('Zed',3)
Garen = Warrior('Garen',3)

item1 = BlackCleaver()
#item2 = BlackCleaver()
item3 = Thornmail()

Zed.gainItem(item1)
#Garen.gainItem(item2)
Garen.gainItem(item3)

os.system('cls')

print(Garen.lifeBar)
print(Zed.lifeBar)
time.sleep(1)

print('begin X1')

time.sleep(1)
os.system('cls')

while Zed.hp > 0 and Garen.hp > 0:

    print(Garen.lifeBar)
    print(Zed.lifeBar)
    Zed.autoAttack(Garen)
    Garen.lifeBar.update(Garen)

    anyKeyPressed()
    os.system('cls')

    print(Garen.lifeBar)
    print(Zed.lifeBar)
    Garen.autoAttack(Zed)
    Zed.lifeBar.update(Zed)

    anyKeyPressed()
    os.system('cls')