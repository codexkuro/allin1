import os
import database as db
from console import console, style, red_console, blue_console, green_console
from rich.panel import Panel
import subprocess
from utils import remove_placeholders

def save():
    """Save command"""
    blue_console.print(Panel("⎙ SAVE COMMAND"))
    
    tool = input("Tool name (nmap/sqlmap/hydra/etc): ").strip()
    command = input("Full command: ").strip()
    category = input("Category (scan/exploit/crack/recon): ").strip()
    note = input("Note/Description: ").strip()
    
    if tool and command:
        db.save_command_to_db(tool, command, category, note)
    else:
        print("\n❌ Tool and Command cannot be empty!")

def list_commands():
    """List All Commands"""

    blue_console.print(Panel("🗁 LIST COMMANDS"))
    
    commands = db.get_all_commands()
    
    if not commands:
        print("\n❌ No commands found! Save some first.")
        return
    
    for cmd in commands:
        green_console.print(Panel(f"[{cmd[0]}] {cmd[1]} | {cmd[4]}\n: {cmd[2][:60]}"))

def search():
    """Search command"""
    
    blue_console.print(Panel("⌕ SEARCH COMMANDS"))
    
    keyword = input("Search keyword: ").strip()
    
    if not keyword:
        print("\n❌ Keyword cannot be empty!")
        return
    
    results = db.search_commands(keyword)
    
    if not results:
        print(f"\n❌ No commands found for '{keyword}'")
        return
    
    print(f"\n✅ Found {len(results)} command(s):")
    for cmd in results:
        green_console.print(Panel(f"[{cmd[0]}] {cmd[1]} | {cmd[4]}\n: {cmd[2][:60]}"))

def run_command():
    """Run command"""
    blue_console.print(Panel("ᯓ➤ RUN COMMAND"))
    
    commands = db.get_all_commands()
    
    if not commands:
        print("\n❌ No commands found! Save some first.")
        return
    
    print("\nAvailable commands:")
    for cmd in commands:
        green_console.print(Panel(f"[{cmd[0]}] {cmd[1]} | {cmd[4]}\n: {cmd[2][:60]}"))
    
    try:
        cmd_id = int(input("\nEnter command ID to run: ").strip())
        selected = None
        for cmd in commands:
            if cmd[0] == cmd_id:
                selected = cmd
                break
        
        if selected:
            command = selected[2]
            if "{" in selected[2]:
                value = input("Placeholder detected! Enter the value: ")
                command = remove_placeholders(selected[2], value)

            print(f"\n⚠️About to run: {command}")
            confirm = input("Are you sure? (y/n): ").strip().lower()
            
            if confirm == 'y':
                try:
                    os.system("clear")
                except:
                    os.system("cls")
                print("\n")
                #green_console.rule()
                #os.system(selected[2])
                result = subprocess.run(command.strip(), shell=True, capture_output=True, text=True)
                if result.stderr:
                    red_console.print(Panel(result.stderr, style="red"))
                else:
                    green_console.print(Panel(result.stdout))
                #green_console.rule()
            else:
                print("\n❌ Cancelled")
        else:
            print("\n❌ Command ID not found")
    except ValueError:
        print("\n❌ Invalid ID!")

def delete():
    """Delete Command"""
    
    red_console.print(Panel("⌫ DELETE COMMAND"))
    
    commands = db.get_all_commands()
    
    if not commands:
        print("\n❌ No commands found!")
        return
    
    for cmd in commands:
        green_console.print(Panel(f"[{cmd[0]}] {cmd[1]} | {cmd[4]}\n: {cmd[2][:60]}"))
    
    try:
        cmd_id = int(input("\nEnter command ID to delete: ").strip())
        
        confirm = input(f"Are you sure want to delete ID {cmd_id}? (y/n): ").strip().lower()
        
        if confirm == 'y':
            if db.delete_command_by_id(cmd_id):
                print(f"\n✅ Command ID {cmd_id} deleted!")
            else:
                print(f"\n❌ Command ID {cmd_id} not found!")
        else:
            print("\n❌ Deletion cancelled")
    except ValueError:
        print("\n❌ Invalid ID!")

