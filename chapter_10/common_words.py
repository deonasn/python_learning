# Deon Anoth
# 01-01-2025
# Python Crash Course: Try it yourself: 10-10

from pathlib import Path

def count_common_words(file):
    try:
        contents = Path(file).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\nFile '{file}' not found, please check your directory!")
    else:
        word_1 = 'the'
        word_2 = 'the '
        common_word_1_count = contents.lower().count(word_1)
        common_word_2_count = contents.lower().count(word_2)
        book_name = filename.replace('_',' ').rstrip(".txt").title()
        print(f"\nThe text file '{book_name}' contains the word '{word_1}' {common_word_1_count} times!")
        print(f"The text file '{book_name}' contains the word '{word_2}' {common_word_2_count} times!")
        print(f"-> Which is a difference of {common_word_1_count - common_word_2_count} words...")

if __name__ == "__main__":
    filename = "myths_of_china_and_japan.txt"
    path = Path(filename)
    count_common_words(path)