from abc import ABC, abstractmethod
from Functions.gameplay import percent

class Item(ABC):
    def __init__(self, hp:int = 0, ad:int = 0, ap:int = 0, ar:int = 0, mr:int = 0, crit:float = 0):
        self.hp   = hp
        self.ad   = ad
        self.ap   = ap
        self.ar   = ar
        self.mr   = mr
        self.crit = crit
        self.hasOnHitEffect = False
        self.name = None

    @abstractmethod
    def effect(self, target = None):
        pass

    def resetEffects(self,target = None):
        pass

class BlackCleaver(Item):
    def __init__(self):
        super().__init__(400, 40)
        self.name = 'Black Cleaver'
        self.counter = 0
        self.target_armor = None
        self.hasOnHitEffect = True

    def onHit(self, target):
        if self.target_armor == None:
            self.target_armor = target.ar
        self.counter = min(6,self.counter+1)
        target.ar = round(self.target_armor - percent(6,self.target_armor)*self.counter, 0)

    def resetEffects(self, target=None):
        self.target_armor = 0
        self.counter = 0

        target.ar = self.target_armor

    def effect(self, target = None):
        pass