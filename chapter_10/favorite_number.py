# Deon Anoth
# 01-09-2025
# Python Crash Course: Try it yourself: 10-11 & 10-12

from json import JSONDecodeError
from pathlib import Path
import json

def enter_favorite_number(path):
    """Prompts the user to enter a favorite number."""
    while True:
        try:
            fav_num = int(input("Please enter your favorite number: ").strip())
        except ValueError:
            print(f"Invalid Entry! Please enter an integer.")
        else:
            contents = json.dumps(fav_num)
            path.write_text(contents)
            return fav_num

def get_stored_favorite_number(path):
    """Extracts the stored favorite number from the given JSON data file."""
    if path.exists():
        contents = path.read_text()
        try:
            fav_num = json.loads(contents)
        except JSONDecodeError:
            print("There are no stored number!\n")
            fav_num = enter_favorite_number(path)
            print(f"Your favorite number '{fav_num}' have been stored!")
            return fav_num, True
        else:
            return fav_num, False
    else:
        return None, None


if __name__ == "__main__":
    filename = 'favorite_number.json'
    path = Path(filename)
    fav_num, empty_file_status = get_stored_favorite_number(path)
    if fav_num:
        if empty_file_status:
            pass
        else:
            print(f"I know your favorite number! It's {fav_num}.")
    else:
        fav_num = enter_favorite_number(path)
        print(f"Your favorite number '{fav_num}' have been stored!")