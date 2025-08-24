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

# Add a small delay for better readability at the start
time.sleep(1.0)

# Prompt for user ID
p = """
Enter ID FILTER ACCOUNT BUT NOT (@)


OK?
"""
# Display the prompt character by character
for i in p:
    sleep(0.05)
    print(color.pink + i, end='', flush=True)

# Get the user's ID input and store it in 'user_id'
user_id = input(color.pink + 'Enter your ID ACCOUNT FOR FIX>>> ')

# Define the codes using the captured 'user_id'
# Ensure to remove any leading/trailing whitespace from user_id if necessary
user_id = user_id.strip()

code1 = f"fix.filter.rubika.ir(rubika.ir/{user_id})This-account-was-for-a-hild's-study-and-was-filtered-by-hackers-please-delete-his-account-Please-fix-filter-this-account"
code2 = f"order=fix.filter>rubika.ir(rubika.ir/{user_id})This-account-has-not-been-violated-remove-it-from-the-ilter"
code3 = f"liberation.account.in.filter/sport(rubika.ir/{user_id})This-account-has-a-religious-owne-who-is-the-admin-of-a-channel-and-the-hackers-have-filtered-it-remove-it-from-the-filter"
code4 = f"Getting.out.of.suspension.spport.bot(rubika.ir/{user_id})This-account-was-hacked-and-the-violations-were-committed-in-the-hack-mode-and-the-real-admin-did-not-do-this-please-remove-it-from-filter"

# Display code1
print(color.green + f"code1 ", end='', flush=True)
sleep(1)
for s in code1:
    sleep(0.03)
    print(color.mark + s, end='', flush=True)
print(color.mark2) # Reset color after printing

# Display code2
print(color.blue + f"code2 ", end='', flush=True)
sleep(1)
for s in code2:
    sleep(0.03)
    # Changed mark1 (background color) to green for better readability on default terminal
    print(color.green + s, end='', flush=True)
print(color.white) # Reset to white/default color

# Display code3
print(color.yellow + f"code3 ", end='', flush=True)
sleep(1)
for s in code3:
    sleep(0.03)
    print(color.mark + s, end='', flush=True)
print(color.mark2) # Reset color after printing

# Display code4 (corrected the label from code1 to code4)
print(color.green + f"code4 ", end='', flush=True) # Corrected label
sleep(1)
for s in code4:
    sleep(0.03)
    print(color.mark + s, end='', flush=True)
print(color.mark2) # Reset color after printing

# Wait for user input to return to the main menu
input(color.green + "Press Enter to return to the main menu >>> ")
print('Returning to menu...')
time.sleep(1) # Small delay before clearing and exiting

system("clear")
