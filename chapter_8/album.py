# Deon Anoth
# 06-19-2024
# Python Crash Course: Try it yourself: 8-7

# defining function 'make_album' to store album information, and returns the information when it is called
def make_album(artist, title, no_songs=None):
    album_info = {'artist': artist.title(), 'title': title.title()}
    if no_songs:
        album_info['number of songs'] = no_songs
    return album_info

# calls and stores 'make_album' function while giving it specific arguments
album_1 = make_album('Zhao Lusi', 'I just wanna hide you')
album_2 = make_album('Ma Boqian', 'Be your light')
album_3 = make_album('Zhang Yi Hou', 'Forever star')
album_4 = make_album('Imran Khan', 'Unforgettable', 13)

# prints the above stored information
print(album_1)
print(album_2)
print(album_3)
print(album_4)