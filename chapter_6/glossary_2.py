# Deon Anoth
# 06-08-2024
# Python Crash Course: Try it yourself: 6-4

# creating a dictionary of terms in the book 'Python Crash Course'
glossary = {'traceback': 'a record of where the interpreter ran into trouble when trying to execute your code.',
            'string': 'a series of characters.', 'method': 'an action that Python can perform on a piece of data. '
                                                           'Every method is followed by a parantheses',
            'whitespace': 'any nonprinting characters, such as spaces, tabs, and end-of-line symbols',
            'syntax error': "error occured when Python doesn't recognize a section of your program as valid Python code.",
            'float': 'numbers with a decimal point.', 'constant': 'a variable whose value stays the same.',
            'comments': 'allows you to write notes in your spoken language, within your programs. '
                        'Python uses (#) symbol to start the comment section and it only applies to that line.',
            'list': 'a collection of items in a particular order.', 'index': 'the position of an item in a list. '
                                                                             "Starts from '0' to 'n-1'.",
            'index error': 'error occured when Python cannot find an item at the index you requested.',
            'indentatin error': 'error occured due to unnecessary or forgotten indentation.',
            'list comprehension': 'allows you to generate the same list in just one line of code. '
                                  'It combines the for loop and the creation of new elements into one line, and '
                                  'automatically appends each new element.',
            'slice': 'a specific group of items in a list of items.',
            'tuple': 'list with values that cannot be changed (immutable)',
            'conditional test': 'an expression that can be evaluated as True or False in an if-statement',
            'boolean value': 'either True or False.', 'else block': 'a catchcall statement in an if-else/if-elif-else chain',
            'dictinary': 'a collection of key-value pairs.', 'key-value pair': 'a set of values associated with each other', }

# for loop to print each word and their meaning indented on a second line
for key, value in glossary.items():
    print(f'{key}:\n    {value}')