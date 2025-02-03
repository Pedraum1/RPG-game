from abc import ABC
from Functions.gameplay import calculateReduction
class Character(ABC):
  
  def __init__(self, name:str, lvl:int = 1, xp:int = 0):
    self.name   = name
    self.lvl    = max(lvl,1)
    self.max_xp = 1000 * lvl
    self.xp     = xp
    self.items  = dict()

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
    self.items[item.name] = item
    self.max_hp += item.hp
    self.hp += item.hp
    self.ar += item.ar
    self.mr += item.mr
    self.ad += item.ad
    self.ap += item.ap
    self.crit += item.crit

  def removeItem(self, item_name):
      item = self.items[item_name]
      self.items.pop('item_name')
      self.hp -= item.hp
      self.ar -= item.ar
      self.mr -= item.mr
      self.ad -= item.ad
      self.ap -= item.ap
      self.crit -= item.crit
      

  def autoAttack(self,target):

    damage = self.ad * calculateReduction(target.ar)
    target.hp = max(round(target.hp - damage), 0)
    print(f"{target.name} has been hit for {damage:.0f} damage")
    
    for item in self.items.values():
       if item.hasOnHitEffect:
          item.onHit(target)

    for item in target.items.values():
        if item.hasOnHitOnEnemyEffect:
            item.onHitOnEnemy(target, self)

  def qSpell(self, entity = None):
        pass

  def wSpell(self, entity = None):
        pass

  def eSpell(self, entity = None):
        pass

  def rSpell(self, entity = None):
        pass
