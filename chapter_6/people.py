# Deon Anoth
# 06-11-2024
# Python Crash Course: Try it yourself: 6-7

# did - contains information about specific individuals - name, age, and city
people = {'person_0' : {'first_name': 'Zyer', 'last_name': 'Anoth', 'age': '23', 'city': 'Urbana'},
          'person_1' : {'first_name': 'Deon', 'last_name': 'Anoth', 'age': '28', 'city': 'Pontoon Beach'},
          'person_2' : {'first_name': 'Shahana', 'last_name': 'Bashir', 'age': '56', 'city': 'Veliancode'},
          }

# for loop to print know information about the specific individuals stored in the dictionary above
for person, info in people.items():
    print(f'{info["first_name"]} {info["last_name"]} is {info["age"]} years old and lives in {info["city"]}')