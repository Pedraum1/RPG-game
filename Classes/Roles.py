from Character import Character
from LifeBar import LifeBar

import time, os

class Warrior(Character):
    
   def __init__(self, name:str, lvl:int = 1, xp:int = 0, hp:int = None):
      self.class_name = "Warrior"
      super().__init__(name, lvl, xp)
      self.HP = self.startHp(hp)
      self.lifeBar = LifeBar(self)

   @property
   def max_HP(self)->int:
      return 500 + self.lvl*85
   
   def startHp(self, hp)->int:
      if hp == None:
         return self.max_HP
      else:
         return min(hp,self.max_HP)

   @property
   def AD(self)->int:
      return 70 + self.lvl*4
      
   @property
   def AR(self)->int:
      return 60 + self.lvl*4
      
   @property
   def MR(self)->int:
      return 60 + self.lvl*4

   @property
   def CRIT(self)->float:
      return 0
'''   
class Mage(Character):
   
   def __init__():
      def __init__(self, name:str, lvl:int, xp:int, hp:int):
        self.class_name = "Mage"

        super().__init__(name, lvl, xp)

        self.max_HP = 300 + lvl*55
        self.HP = min(hp,self.max_HP)
        self.ad = 45 + lvl*3
        self.ar = 50 + lvl*1.5
        self.mr = 30 + lvl*2
        self.crit =  lvl*0.75

        self.lifeBar = LifeBar(self)
'''

if __name__ == '__main__':
   Garen = Warrior('Garen')
   Darius = Warrior('Darius')

   os.system('cls')

   print(Darius.lifeBar)
   print(Garen.lifeBar)
   time.sleep(1)

   print('begin X1')

   time.sleep(1)
   os.system('cls')

   while Garen.HP > 0 and Darius.HP > 0:

      Darius.autoAttack(Garen)
      Garen.lifeBar.update(Garen)

      print(Darius.lifeBar)
      print(Garen.lifeBar)

      time.sleep(1)
      os.system('cls')

      Garen.autoAttack(Darius)
      Darius.lifeBar.update(Darius)

      print(Darius.lifeBar)
      print(Garen.lifeBar)

      time.sleep(1)
      os.system('cls')

