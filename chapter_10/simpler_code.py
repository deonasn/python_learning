# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-3

from pathlib import Path
def open_file(file_name):
    """function to open a file"""
    path = Path(file_name)
    return path

def print_simpler(file_name):
    """function to store the contents in a list much simpler and print the contents."""
    contents = file_name.read_text()
    for line in contents.splitlines():
        print(line)

if __name__ == "__main__":
    file_name = "learning_python.txt"
    file = open_file(file_name)
    print_simpler(file)