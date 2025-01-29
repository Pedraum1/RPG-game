from Classes.Roles import Warrior,Mage
from Classes.Items import BlackCleaver
import time, os


Garen = Warrior('Garen',20)
Ryze = Mage('Ryze',20)
blackCleaver =  BlackCleaver()
Garen.items.append(blackCleaver)

os.system('cls')

print(Ryze.lifeBar)
print(Garen.lifeBar)
time.sleep(1)

print('begin X1')

time.sleep(1)
os.system('cls')

while Garen.HP > 0 and Ryze.HP > 0:

    Ryze.autoAttack(Garen)
    Garen.lifeBar.update(Garen)

    print(Ryze.lifeBar)
    print(Garen.lifeBar)

    time.sleep(0.5)
    os.system('cls')

    Garen.autoAttack(Ryze)

    print(Ryze.lifeBar)
    print(Garen.lifeBar)

    time.sleep(0.5)
    os.system('cls')