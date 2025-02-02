from .Prompt import clearPrompt

def anyKeyPressed():
    while True:
        exit = input()
        if exit or exit == '':
            return
        
def printOptions(options:list, text:str="") -> int:

    while True:
        print(f"{text}\n")
        for index, option in enumerate(options):            
            print(f"{index+1} - {option}")
        print(f"{len(options)+1} - Exit")

        option = getNumberOption(options)

        if option != None:
            return option
        
        clearPrompt() 

def getNumberOption(options:list):
    while True:
        try:
            option = int(input("\nEnter the number of the option: "))-1
            if option < 0 or option > len(options):
                print("Invalid option")
                return None
            return option
        except ValueError:
            print("Invalid option")
            return None