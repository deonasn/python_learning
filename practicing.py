# just for practicing while reading
# mostly in-text examples

from json import JSONDecodeError
from pathlib import Path
import json

def entry_new_username(path):
    """Prompts the user to enter a new username."""
    username = input("Please enter your username: ").strip()
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def get_stored_username(path):
    """Extracts the stored username from the given JSON data file."""
    if path.exists():
        contents = path.read_text()
        try:
            username = json.loads(contents)
        except JSONDecodeError:
            print("The JSON data file is empty!\n")
            username = entry_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
            return username, True
        else:
            return username, False
    else:
        return None, None

def greet_user():
    """Greets the user."""
    path = Path('username.json')
    username, empty_file_status = get_stored_username(path)
    if username:
        if empty_file_status:
            pass
        else:
            print(f"Welcome back, {username}!")
    else:
        username = entry_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()