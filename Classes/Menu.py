from Functions.Prompt import *
from Functions.inputs import getNumberOption

class Menu():

    def __init__(self, menu_options: list, title: str):
        self.menu_options = menu_options
        self.title = title

    def render(self) -> None:                
        clearPrompt()

        while True:
            print(f"{self.title}\n")
            for index, option in enumerate(self.menu_options):            
                print(f"{index+1} - {option}")
            print(f"{len(self.menu_options)+1} - Exit")

            option = getNumberOption(self.menu_options)

            if option != None:
                return option
    
    @property
    def exit(self) -> int:
        return len(self.menu_options)
