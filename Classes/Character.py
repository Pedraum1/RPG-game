from abc import ABC, abstractmethod
from Functions.gameplay import calculateReduction
class Character(ABC):
  
  def __init__(self, name:str, lvl:int = 1, xp:int = 0):
    self.name   = name
    self.lvl    = max(lvl,1)
    self.max_xp = 1000 * lvl
    self.xp     = xp
    self.items  = list()

    self.max_hp = 0
    self.hp = 0
    self.ar = 0
    self.mr = 0
    self.ad = 0
    self.ap = 0
    self.crit = 0
  
  def setupStatus(self):
      pass
  
  def lvlUp(self):
     self.lvl = min(self.lvl+1,20)
     self.max_xp = 1000 * self.lvl
     setupStatus(self)

  def gainXp(self, xp_reward):
    self.xp += xp_reward

    while self.xp >= self.max_xp:
      self.xp = self.xp - self.max_xp
      self.lvlUp()

  def gainItem(self, item):
    self.items.append(item)
    self.hp += item.hp
    self.ar += item.ar
    self.mr += item.mr
    self.ad += item.ad
    self.ap += item.ap
    self.crit += item.crit


  def autoAttack(self,target):
    for item in self.items:
       if item.hasOnHitEffect:
          item.onHit(target)

    damage = self.ad * calculateReduction(target.ar)
    target.hp = max(round(target.hp - damage), 0)
    target.lifeBar.update(target)

  def qSpell(self, entity = None):
        pass

  def wSpell(self, entity = None):
        pass

  def eSpell(self, entity = None):
        pass

  def rSpell(self, entity = None):
        pass
