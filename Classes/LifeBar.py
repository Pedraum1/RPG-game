class LifeBar:  

  def __init__(self, target): 
    self.length    = 40
    self.entity    = target
    self.square    = '\u2588'

  def __str__(self): 
    life      = round(self.entity.hp*self.length/self.entity.max_hp)
    lost_life = self.length - life

    return f"{self.entity.name} - {self.entity.max_hp}/{self.entity.hp} - {self.entity.class_name} - lvl.{self.entity.lvl}\n|{life*self.square}{lost_life*'_'}|\n"
  
  def update(self,target):
    self.entity = target