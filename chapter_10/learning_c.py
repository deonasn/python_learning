# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-2

from pathlib import Path
def open_file(file_name):
    """function to open a file"""
    path = Path(file_name)
    return path

def replace_and_print(file_name):
    """function to store the contents in a list and print the contents while replacing Python with C"""
    lines = file_name.read_text().splitlines()
    for line in lines:
        line = line.replace('Python', 'C')
        print(line)

if __name__ == "__main__":
    file_name = "learning_python.txt"
    file = open_file(file_name)
    replace_and_print(file)