# Deon Anoth
# 06-19-2024
# Python Crash Course: Try it yourself: 8-8

# defining function 'make_album' to store album information, and returns the information when it is called
def make_album(artist, title, no_songs=None):
    album_info = {'artist': artist.title(), 'title': title.title()}
    if no_songs:
        album_info['number of songs'] = no_songs
    return album_info

# artist names and thier album titles:
"""Zhao Lusi - I just wanna hide you"""
"""Ma Boqian - Be your light"""
"""Zhang Yi Hou - Forever star"""

# Welcome message
print("Hi, Please enter the album artist and the respective title!\n"
      "(enter 'q' at any time to quit)")

# while loop to enter user inputs infinitely until the user chooses to quit
while True:
    album_artist = input('\nEnter artist: ')
    if album_artist == 'q':
        break

    album_title = input('Enter title: ')
    if album_title == 'q':
        break

    # calls 'make_album' function with user inputs as arguments
    album = make_album(album_artist, album_title)
    print(album)