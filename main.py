import time, os
from Classes.Roles import Warrior, Mage

Garen = Warrior('Garen',20)
Ryze = Mage('Ryze',20)

os.system('cls')

print(Ryze.lifeBar)
print(Garen.lifeBar)
time.sleep(1)

print('begin X1')

time.sleep(1)
os.system('cls')

while Garen.hp > 0 and Ryze.hp > 0:

    Ryze.autoAttack(Garen)
    Garen.lifeBar.update(Garen)

    print(Ryze.lifeBar)
    print(Garen.lifeBar)

    time.sleep(1)
    os.system('cls')

    Garen.autoAttack(Ryze)

    print(Ryze.lifeBar)
    print(Garen.lifeBar)

    time.sleep(1)
    os.system('cls')