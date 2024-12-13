from abc import ABC, abstractmethod
from LifeBar import LifeBar

class Character(ABC):
  
  def __init__(self, name:str, lvl:int = 1, xp:int = 0):
    self.name   = name
    self.lvl    = max(lvl,1)
    self.max_xp = 1000 * lvl
    self.xp     = xp
    

    @property
    @abstractmethod
    def max_HP(self)->int:
      pass
    
    @abstractmethod
    def startHp(self)->int:
      pass
    
    @property
    @abstractmethod
    def AR(self)->int:
      pass
    
    @property
    @abstractmethod
    def MR(self)->int:
      pass
    
    @property
    @abstractmethod
    def AD(self)->int:
      pass

    @property
    @abstractmethod
    def AP(self)->int:
      pass

    @property
    @abstractmethod
    def CRIT(self)->float:
      pass

  
  def lvlUp(self):
     self.lvl = min(self.lvl+1,20)
     self.max_xp = 1000 * self.lvl

  def gainXp(self, xp_reward):
    self.xp += xp_reward

    while self.xp >= self.max_xp:
      self.xp = self.xp - self.max_xp
      self.lvlUp()

  def autoAttack(self,target):
    damage_reduction = 100/(100+self.AR)
    damage = self.AD*damage_reduction
    target.HP = max(round(target.HP - damage), 0)
