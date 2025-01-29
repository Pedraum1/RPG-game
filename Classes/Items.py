from abc import ABC, abstractmethod
from Functions.gameplay import percent

class Item(ABC):
    def __init__(self, HP:int = 0, AD:int = 0, AP:int = 0, AR:int = 0, MR:int = 0, CRIT:float = 0):
        self.HP   = HP
        self.AD   = AD
        self.AP   = AP
        self.AR   = AR
        self.MR   = MR
        self.CRIT = CRIT
        self.onHit = False

    @abstractmethod
    def effect(self, target = None):
        pass

    def resetEffects(self,target = None):
        pass

class BlackCleaver(Item):
    def __init__(self):
        super().__init__(400, 40)
        self.onHit = True
        self.counter = 0
        self.target_armor = 0

    def onHit(self, target):
        if self.target_armor == 0:
            self.target_armor = target.AR
        target.AR = round(self.target_armor - percent(6)*self.target_armor*self.counter, 0)
        self.counter = min(6,self.counter+1)

    def resetEffects(self, target=None):
        self.target_armor = 0
        self.counter = 0

    def effect(self, target = None):
        pass