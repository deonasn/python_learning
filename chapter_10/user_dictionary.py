# Deon Anoth
# 01-10-2025
# Python Crash Course: Try it yourself: 10-13

from pathlib import Path
import json
from json import JSONDecodeError

def entry_new_user_info(path):
    """Prompts the user to enter a new user information."""
    print("New user data Entry:-")
    username = input("\t-> Please enter your name: ").strip().title()
    while True:
        gender = input("\t-> Please enter your gender (Male/Female): ").strip().lower()
        if gender.lower() not in ["male", "female"]:
            print("\t\t!-> Please enter either male or female.")
        else:
            break
    while True:
        try:
            age = int(input("\t-> Please enter your age: ").strip())
        except ValueError:
            print(f"\t\t!-> Invalid Entry for 'Age'! Please enter an integer.")
        else:
            break
    user_info = {'username': username, 'gender': gender, 'age': age}
    contents = json.dumps(user_info)
    path.write_text(contents)
    print("\t\t<- User info saved successfully! ->")
    return user_info

def get_stored_user_info(path):
    """Extracts the stored user information from the given JSON data file."""
    if path.exists():
        contents = path.read_text()
        try:
            user_info = json.loads(contents)
        except JSONDecodeError:
            print("There is no user information stored in the data file!\n")
            user_info = entry_new_user_info(path)
            return user_info, True, True
        else:
            return user_info, True, False
    else:
        return None, False, True

def proc_stored_info(user_info):
    """Processes the user information from the extracted user data."""
    username = user_info['username']
    gender = user_info['gender']
    age = user_info['age']
    return username, gender, age

def greet_user():
    """Greets the user."""
    user_info, file_status, empty_file_status = get_stored_user_info(path)
    if file_status and not empty_file_status:
        username, gender, age = proc_stored_info(user_info)
        print(f"\nSaved Data:-")
        print(f"\t-> Name: {username}")
        print(f"\t-> Gender: {gender.title()}")
        print(f"\t-> Age: {age}")
    elif not file_status:
        user_info = entry_new_user_info(path)


if __name__ == "__main__":
    path = Path('user_dictionary.json')
    user_info = {}
    greet_user()