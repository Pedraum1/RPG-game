from .Character import Character
from .LifeBar import LifeBar
from .Items import *

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
   
class Mage(Character):

   def __init__(self, name:str, lvl:int = 1, xp:int = 0, hp:int = None):
      self.class_name = "Mage"

      super().__init__(name, lvl, xp)

      self.HP = self.startHp(hp)
      self.lifeBar = LifeBar(self)

   @property
   def max_HP(self)->int:
      return 300 + self.lvl*55
         
   def startHp(self, hp)->int:
      if hp == None:
         return self.max_HP
      else:
         return min(hp,self.max_HP)
        
   @property
   def AD(self)->int:
      return round(50 + self.lvl*2.5)
         
   @property
   def AR(self)->int:
      return round(48 + self.lvl*2.5)
         
   @property
   def MR(self)->int:
      return 40 + self.lvl*2
         
   @property
   def CRIT(self)->float:
      return 0
