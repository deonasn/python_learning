# just for practicing while reading
# mostly in-text examples

from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += str(8)

path = Path("programming.txt")
path.write_text(contents)
print(len(contents))
# path.write_text("I love programming.")
# path.write_text("I love creating new games.")