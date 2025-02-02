from os import system
from time import sleep

def clearPrompt() -> None:
    system("cls")

def delay(time:float) -> None:
    sleep(time)