from Functions.inputs import *
from Functions.Prompt import *
from .Menu import Menu

class Game():
    def __init__(self) :
        self.difficulty_level = 0
        self.difficulty_levels = ["Easy","Medium","Hard"]
        self.difficulty = self.difficulty_levels[self.difficulty_level]

        self.start_menu = Menu(["New Game", "Settings"], "PYTHON RPG")
        self.settings_menu = Menu([f"Difficulty: {self.difficulty}"], "Settings")
        self.difficulty_menu = Menu(self.difficulty_levels, "Difficulty")

    def menu(self) -> int:
        clearPrompt()
        return self.start_menu.render()
    
    def run(self) -> None:
        while True:
            clearPrompt()
            print("Imagine the game running ...")
            anyKeyPressed()
            break

    def settings(self) -> None:
        clearPrompt()
        option = self.settings_menu.render()

        if option == 0:
            clearPrompt()
            new_difficulty = self.difficulty_menu.render()

            if new_difficulty == len(self.difficulty_levels):
                clearPrompt()
                self.settings()
            else:
                self.difficulty = self.difficulty_levels[new_difficulty]
                self.updateDifficulty(self.difficulty_levels[new_difficulty])
                self.difficulty_level = self.difficulty
                clearPrompt()
                self.settings()

        if option == len(self.settings_menu.menu_options):
            clearPrompt()
    
    def exit(self) -> None:
        exit()

    def updateDifficulty(self, new_value:str) -> None:
        self.difficulty = new_value
        self.settings_menu.menu_options = [f"Difficulty: {self.difficulty}"]
        
