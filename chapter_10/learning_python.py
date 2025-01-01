# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-1

from pathlib import Path
def open_file(file_name):
    """function to open a file"""
    path = Path(file_name)
    return path

def print_by_read_entire_file(file_name):
    """function to read the entire file and print the contents"""
    contents = file_name.read_text()
    print(contents)

def print_by_store_loop(file_name):
    """function to store the contents in a list and print the contents"""
    lines = file_name.read_text().splitlines()
    for line in lines:
        print(line)

if __name__ == "__main__":
    file_name = "learning_python.txt"
    file = open_file(file_name)
    print_by_read_entire_file(file)
    print("\n")
    print_by_store_loop(file)