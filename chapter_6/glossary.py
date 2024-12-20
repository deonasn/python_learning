# Deon Anoth
# 06-07-2024
# Python Crash Course: Try it yourself: 6-3

# creating a dictionary of terms in the book 'Python Crash Course'
glossary = {'traceback': 'a record of where the interpreter ran into trouble when trying to execute your code.',
            'string': 'a series of characters.', 'method': 'an action that Python can perform on a piece of data. '
                                                           'Every method is followed by a parantheses',
            'whitespace': 'any nonprinting characters, such as spaces, tabs, and end-of-line symbols',
            'syntax error': "error occured when Python doesn't recognize a section of your program as valid Python code.", }

# print each terms in glossary dictionary one by one and their meaning indented on a second line
print(f'traceback:\n\t{glossary["traceback"]}')
print(f'string:\n\t{glossary["string"]}')
print(f'method:\n\t{glossary["method"]}')
print(f'whitespace:\n\t{glossary["whitespace"]}')
print(f'syntax error:\n\t{glossary["syntax error"]}')