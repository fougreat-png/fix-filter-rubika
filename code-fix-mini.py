import random
import time
import os
from os import system
from time import sleep
import sys
# datetime and requests were imported but not used in the provided code,
# so they are removed for cleaner code.

# Clear the screen at the very beginning for a clean start
system("clear")
os.system("") # Ensures ANSI escape codes work on some systems

# Define color class for console output
class color:
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    pink = "\033[35m"
    yellow = "\033[93m"
    darkblue = "\033[34m"
    white = "\033[00m" # Reset to default color
    mark = '\x1b[38;5;4m' # Specific blue-ish foreground
    mark1 = '\x1b[48;5;15m' # Specific background (white)
    mark2 = '\x1b[0m' # Reset all attributes (color, background, bold, etc.)

# Welcome message with a small delay
print(color.mark + "WELCOME", end='', flush=True)
sleep(1)
print(color.blue) # Set color to darkblue for subsequent output, then print newline

# List of Rubika links/codes to choose from
repoestsrub = [
    'Rubika.ir/raf-filter', 'Rubika.ir/fixing-filter', 'Rubika.ir/Account-liberation',
    'Rubika.ir/rf-fil-rubuk', 'Rubika.ir/Please-unfilter-this-account',
    'Rubika.ir/plase-fix-filter-this-account', 'Rubika.ir/fix-fix-fil',
    'Rubika.ir/fixing-fil', 'Rubika.ir/moslim-account', 'Rubika.ir/Religious-account',
    'Rubika.ir/Support-fix-filter', 'Rubika.ir/This-Account-Undertone-Do-Not',
    'Rubika.ir/This-Account-Mistake-Filtered', 'Rubika.ir/This-Account-must-fix-Filter',
    'Rubika.ir/Bring-this-account-from-the-sanctuary', 'Rubika.ir/rf-filtering'
]
# Select a random code from the list
coderize = random.choice(repoestsrub)

# Prompt for the user to generate a code
y0y = f"""
for give code enter 1

OK?
(ravesh 20 ta sayer baede 2 daghighe 10 ta sayer)
"""
# Display the prompt character by character
for i in y0y:
    sleep(0.05)
    print(color.pink + i, end='', flush=True)

# Get user input
gottt = input(color.pink + 'Enter 1 to generate code >>> ')

# Check if the user entered '1' (input() returns a string)
if gottt == '1':
    print(color.pink + "Generated Code: " + coderize)
else:
    print(color.red + "Invalid input. Please enter 1 to get a code.")

# Wait for user input to return to the main menu
input(color.green + "Press Enter to return to the main menu >>> ")
print('Returning to menu...')
time.sleep(1) # Small delay before clearing and exiting

system("clear")
# This script will now simply end, allowing the main calling script (e.g., fix-filter.py)
# to regain control and re-display its menu.
