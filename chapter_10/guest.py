# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-4

from pathlib import Path

user = input("Enter your name: ")       # prompt user to enter their name
path = Path("guest.txt")                # create a Path object to store the file name
path.write_text(user)                   # write the user's name to guest.txt