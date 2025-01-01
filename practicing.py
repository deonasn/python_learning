# just for practicing while reading
# mostly in-text examples

from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# print(pi_string)
# print(len(pi_string))
# print(f"{pi_string[:52]}...")
# print(contents)