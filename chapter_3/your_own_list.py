# Deon Anoth
# 05-22-2024
# Python Crash Course: Try it yourself: 3-3

favorite_transportation = ["car",'motorcycle','airplane']           # list containing my favorite transpotation
print(f"I would like to own a BMW {favorite_transportation[1]}")
print(f'Tesla has the best {favorite_transportation[0]} with the best techonological features')
print(f'Riding an {favorite_transportation[2]} feels like riding a cloud')

print('\n')
motorcycles = []
while True:                                     # While loop for input and append it to the list
    m_inp = input('Enter the name of the motorcycle (enter "-q" to quit): ')
    if m_inp == '-q':
        break
    motorcycles.append(m_inp)                   # list append
print(motorcycles)                              # Printing list