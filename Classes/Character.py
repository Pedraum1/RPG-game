from abc import ABC, abstractmethod

class Character(ABC):
  
  def __init__(self, name:str, lvl:int = 1, xp:int = 0):
    self.name   = name
    self.lvl    = max(lvl,1)
    self.max_xp = 1000 * lvl
    self.xp     = xp
    self.items  = list() 

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
    for item in self.items:
       if item.onHit:
          item.onHit(self, target)

    damage = self.AD * 100/(100+target.AR)
    target.HP = max(round(target.HP - damage), 0)
    target.lifeBar.update(target)

  def qSpell(self, entity = None):
        pass

  def wSpell(self, entity = None):
        pass

  def eSpell(self, entity = None):
        pass

  def rSpell(self, entity = None):
        pass
