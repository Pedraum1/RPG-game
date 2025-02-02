from Functions.inputs import *
from Functions.Prompt import *

class Game():
    def __init__(self):
        self.difficulty = 0

    def menu(self) -> int:
        menu_options = ['New Game', 'Settings', 'Exit']
        return printOptions(menu_options,"PYTHON RPG")
    
    def start():
        pass

    def settings():
        pass
    
    def exit(self) -> None:
        exit()
        
