from random import randint

def percent(value:int, origin:float) -> float:
    return origin*value/100

def calculateReduction(armor:float) -> float:
    return 100/(100+armor)

def randomFactor() -> int:
    return randint(0, 100)