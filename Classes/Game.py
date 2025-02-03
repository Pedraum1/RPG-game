from Functions.inputs import *
from Functions.Prompt import *

class Game():
    def __init__(self):
        self.difficulty_level = 0
        self.difficulty_levels = ["Easy","Medium","Hard"]
        self.difficulty = self.difficulty_levels[self.difficulty_level]

    def menu(self) -> int:
        clearPrompt()
        menu_options = ['New Game', 'Settings']
        return printOptions(menu_options,"PYTHON RPG")
    
    def run(self) -> None:
        while True:
            clearPrompt()
            print("Imagine the game running ...")
            anyKeyPressed()
            clearPrompt()
            break

    def settings(self) -> None:
        clearPrompt()
        settings_options = [f"Difficulty: {self.difficulty}"]
        option = printOptions(settings_options,"Settings")

        if option == 0:
            clearPrompt()
            new_difficulty = printOptions(self.difficulty_levels,"Difficulty")

            if new_difficulty == len(self.difficulty_levels):
                clearPrompt()
                self.settings()
            else:
                self.difficulty = self.difficulty_levels[new_difficulty]
                self.difficulty_level = self.difficulty
                clearPrompt()
                self.settings()

        if option == len(settings_options):
            clearPrompt()
    
    def exit(self) -> None:
        exit()
        
