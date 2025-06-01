# just for practicing while reading
# mostly in-text examples

def get_formatted_name(first, last, middle=None):
    """Generate a neatly formatted full name."""
    if middle == None:
        full_name = f"{first} {last}"
    else:
        full_name = f"{first} {middle} {last}"
    return full_name.title()