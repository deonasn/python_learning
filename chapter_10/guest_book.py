# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-5

from pathlib import Path

user = ""                                       # initialize an empty string to store the user's name

prompt_status = True
while prompt_status:
    user += input("Enter your name: ")          # prompt user to enter their name
    repeat_prompt = input("Do you want to continue? (y/n): ")  # prompt user to continue or not
    if repeat_prompt.lower() == "n":
        prompt_status = False
    if repeat_prompt.lower() == "y":
        user += "\n"                            # add a newline character to separate the names
    while repeat_prompt.lower() not in ["y", "n"]:
        repeat_prompt = input("Invalid input. Please enter 'y' or 'n': ")  # prompt user to enter 'y' or 'n'

path = Path("guest_book.txt")                   # create a Path object to store the file name
path.write_text(user)                           # write the user's name to guest.txt