from .Character import Character
from .LifeBar import LifeBar
from .Items import *

class Warrior(Character):
    
   def __init__(self, name:str, lvl:int = 1, xp:int = 0, hp:int = None):
      self.class_name = "Warrior"

      super().__init__(name, lvl, xp)

      self.max_hp = 500 + self.lvl*85
      self.hp     = self.startHp(hp)
      self.ad     = 65 + self.lvl*3.5
      self.ar     = 60 + self.lvl*4
      self.mr     = 60 + self.lvl*4

      self.lifeBar = LifeBar(self)

   def setupStatus(self):
      self.max_hp = 500 + self.lvl*85
      self.ad = 70 + self.lvl*3.5
      self.ar = 60 + self.lvl*4
      self.mr = 60 + self.lvl*4
   
   def startHp(self, hp)->int:
      if hp == None:
         return self.max_hp
      else:
         return min(hp,self.max_hp)
   
class Mage(Character):

   def __init__(self, name:str, lvl:int = 1, xp:int = 0, hp:int = None):
      self.class_name = "Mage"

      super().__init__(name, lvl, xp)

      self.max_hp = 300 + self.lvl*50
      self.hp     = self.startHp(hp)
      self.ad     = 50 + self.lvl*2.5
      self.ar     = 40 + self.lvl*2.5
      self.mr     = 40 + self.lvl*2

      self.lifeBar = LifeBar(self)

   def setupStatus(self):
      self.max_hp = 300 + self.lvl*50
      self.ad = 50 + self.lvl*2.5
      self.ar = 40 + self.lvl*2.5
      self.mr = 40 + self.lvl*2
         
   def startHp(self, hp)->int:
      if hp == None:
         return self.max_hp
      else:
         return min(hp,self.max_hp)

class Assassin(Character):
   
   def __init__(self, name:str, lvl:int = 1, xp:int = 0, hp:int = None):
      self.class_name = "Assassin"

      super().__init__(name, lvl, xp)

      self.max_hp = 450 + self.lvl*55
      self.hp     = self.startHp(hp)
      self.ad     = 90 + self.lvl*2.75
      self.ar     = 35 + self.lvl*2.25
      self.mr     = 30 + self.lvl*1.5

      self.lifeBar = LifeBar(self)

   def setupStatus(self):
      hp_proportion = self.hp/self.max_hp
      self.max_hp = 450 + self.lvl*55
      self.hp = self.max_hp*hp_proportion

      self.ad = 90 + self.lvl*2.75
      self.ar = 35 + self.lvl*2.25
      self.mr = 30 + self.lvl*1.5
         
   def startHp(self, hp)->int:
      if hp == None:
         return self.max_hp
      else:
         return min(hp,self.max_hp)
      
class Tank(Character):
   
   def __init__(self, name:str, lvl:int = 1, xp:int = 0, hp:int = None):
      self.class_name = "Tank"

      super().__init__(name, lvl, xp)

      self.max_hp = 650 + self.lvl*100
      self.hp     = self.startHp(hp)
      self.ad     = 50 + self.lvl*2.5
      self.ar     = 70 + self.lvl*4
      self.mr     = 70 + self.lvl*4

      self.lifeBar = LifeBar(self)

   def setupStatus(self):
      self.max_hp = 600 + self.lvl*100
      self.ad = 50 + self.lvl*2.5
      self.ar = 70 + self.lvl*4
      self.mr = 70 + self.lvl*4
         
   def startHp(self, hp)->int:
      if hp == None:
         return self.max_hp
      else:
         return min(hp,self.max_hp)