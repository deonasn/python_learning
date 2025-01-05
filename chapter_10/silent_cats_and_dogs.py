# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-9

from pathlib import Path

def read_n_print_file(filename):
    try:
        contents = filename.read_text()
    except FileNotFoundError:
        pass
    else:
        names = contents.split()
        print(f"\nThe names of {file.rstrip('.txt')} are:")
        for name in names:
            print(f"{names.index(name) + 1}. {name}")


if __name__ == "__main__":
    files = ['cats.txt', 'dogs.txt', 'cats_and_dogs.txt']
    for file in files:
        path = Path(file)
        read_n_print_file(path)