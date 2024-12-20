# Deon Anoth
# 06-24-2024
# Python Crash Course: Try it yourself: 8-13

# defining function 'build_profile' using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we kow about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# function call and prints the dictionary
user_profile = build_profile('Deon', 'Anoth', location = 'Pontoon Beach', field = 'Computer Science',
                             religion = 'ISLAM')
print(user_profile)