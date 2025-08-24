import random
import time
import os
from os import system
from time import sleep
import sys
import datetime
import requests

# Clear the screen at the very beginning
system("clear")
os.system("")

# Define color class for console output
class color:
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    pink = "\033[35m"
    yellow = "\033[93m"
    darkblue = "\033[34m"
    white = "\033[00m"
    mark = '\x1b[38;5;4m'
    mark1 = '\x1b[48;5;15m'
    mark2 = '\x1b[0m'

# Installation message with a loading animation
print(color.mark + "INSTALLING", end='')
sleep(1)
print(color.green + ".", end='', flush=True)
sleep(1)
print(color.green + ".", end='', flush=True)
sleep(1)
print(color.green + ".", end='', flush=True)
sleep(1)
print(f"\033[34m")

# Banner display (Simplified to a standard multiline string)
banner = """
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠃⠀⠀⠀⠀⢀⠀⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⣴⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡇⠀⠀⢀⡰⣡⣾⣿⣿⡟⠀⠀⠀⠀⠀⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡁⠀⡠⢋⣼⣿⣿⣿⢸⠁⠀⠀⠀⠀⣠⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡿⡄⢈⣴⣿⣿⣿⣿⣽⡏⠀⠀⠀⢀⣾⣿⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣠⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣠⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⠀⣠⣼⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣠⣼⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣼⣿⣿⣿⣿⣿⣿⡟⡇⠀⠀⠀⣠⣾⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⠃⢀⣠⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣰⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⡿⣟⠋⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣟⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⡿⡿⢿⡽⠁⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣧⣾⠂⢵⡆⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣟⣞⡆⣾⠀⢀⣀⣤⣶⣦⣤⣄⣀⠠⡀⠀⠀⠀⠊⠙⠻⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣾⣾⣾⣿⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣯⢹⠙⡏⢿⠁⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⣠⠶⢓⣠⣄⠀⠠⣹⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣼⢠⠇⠀⡀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠃⢀⠾⣫⣾⣿⣿⣿⣿⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠃⡿⣷⣴⣌⠀⠈⠙⢿⣿⣿⣿⡿⠋⢀⣇⢧⢹⣿⣿⣿⣿⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣏⡏⢯⣿⣻⣷⣾⣯⠦⠄⠀⠈⠉⣁⣠⣴⣾⣿⣾⢽⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠟⣿⣿⣿⣿⣿⡛⣿⣧⡄⢰⣾⣿⣿⣿⣿⣷⠞⠛⠻⠟⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣸⣿⣿⣿⣛⣿⢦⣝⠃⠈⠝⠟⢋⡉⢺⡿⠏⠹⣷⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡌⠻⣯⣿⣿⣻⢦⣞⡿⣦⣤⢀⢻⢋⣴⡚⠋⣴⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣆⠙⡻⡿⣷⣿⡿⣿⡛⣿⢻⣿⣷⣭⣥⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠉⣿⣿⣟⣿⣷⣿⣿⣻⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢇⠀⠀⠻⠻⣷⣾⣵⣻⣫⣿⣯⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣀⠈⠉⢉⣡⣾⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

█▀▀ █ ▀▄▀   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█   █▀█ █░█ █▄▄ █ █▄▀ ▄▀█
█▀░ █ █░█   █▀░ █ █▄▄ ░█░ ██▄ █▀▄   █▀▄ █▄█ █▄█ █ █░█ █▀█ v1.1
"""
for bnr in banner:
    sys.stdout.write(bnr)
    sys.stdout.flush()
    time.sleep(0.009)

# Main loop for the menu
while True:
    yty = """ 
1. Code with ID
2. Code without ID
3. Exit
 """
    for i in yty:
        sleep(0.01) # Reduced sleep for faster menu display
        print(color.pink + i, end='', flush=True)

    get = input(color.pink + 'Enter number here>>> ')

    if get == '1':
        system("clear")
        print(color.blue + "Starting code with ID...")
        system("python code-fix.py")
        print(color.green + "Code with ID finished. Returning to menu.")
        sleep(2) # Give user time to read message
    elif get == '2':
        system("clear")
        print(color.blue + "Starting code without ID...")
        system("python code-fix-mini.py")
        print(color.green + "Code without ID finished. Returning to menu.")
        sleep(2) # Give user time to read message
    elif get == '3':
        system("clear")
        print(color.yellow + "Exiting the main script. Goodbye!")
        break # Exit the while loop
    else:
        system("clear") # Clear before showing error and re-displaying menu
        print(color.red + "Invalid input. Please enter 1, 2, or 3.")
        sleep(2) # Give user time to read error message
    
    # Clear screen before re-displaying the menu for a clean look
    system("clear")
