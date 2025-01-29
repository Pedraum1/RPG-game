class LifeBar:  

  def __init__(self, target): 
    self.length    = 40
    self.entity    = target
    self.square    = '\u2588'

  def __str__(self): 
    life      = round(self.entity.HP*self.length/self.entity.max_HP)
    lost_life = self.length - life

    return f"{self.entity.name} - {self.entity.class_name} - lvl.{self.entity.lvl}\n|{life*self.square}{lost_life*'_'}|\n"
  
  def update(self,target):
    self.entity = target