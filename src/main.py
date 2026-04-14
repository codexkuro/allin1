import os
from pick import pick
import database as db
import features as allin1
from console import console, style, red_console, blue_console, green_console
from rich.panel import Panel

def main():
    db.create_commands_table()

    options = [
        "⎙ | Save Command",
        "🗁 | List All Commands", 
        "⌕ | Search Command",
        "ᯓ➤ | Run Command",
        "⌫ | Delete Command",
        "➜] | Exit"
    ]
    
    title = "\n   ⚡Allin1"

    while True:
        try:
            os.system('clear')
        except:
            os.system('cls')
            
        selected, index = pick(options, title, indicator="->")
        
        
        if index == 0:      # Save
            allin1.save()
        elif index == 1:    # List
            allin1.list_commands()
        elif index == 2:    # Search
            allin1.search()
        elif index == 3:    # Run
            allin1.run_command()
        elif index == 4:    # Delete
            allin1.delete()
        elif index == 5:    # Exit
            break
        
        input("\nPress Enter...")

if __name__ == "__main__":
    main()
