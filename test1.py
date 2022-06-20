# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filter_dog_owners" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filter_adults" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
    {"id": '1', "name": 'John Smith', "age": 20, "hasDog": True},
    {"id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False},
    {"id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True},
    {"id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False},
    {"id": '5', "name": 'Alex John', "age": 25, "hasDog": True},
    {"id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True},
    {"id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True},
    {"id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False},
    {"id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True},
]


def filter_dog_owners(x):
    print(f"'users', kurie turi augintinį, sąrašas:")
    users_has_dog_list = []
    users_filtered = list(filter(lambda d: d['hasDog'] is True, x))
    for user in users_filtered:
        users_has_dog_list.append(user['name'])
        print(user['name'])
    print(f"'users', kurie turi augintinį, sąrašas masyve: {users_has_dog_list}")


def filter_adults(x):
    print(f"'Suaugusiųjų 'users' sąrašas:")
    users_adult = []
    users_filtered = list(filter(lambda d: d['age'] >= 18, x))
    for user in users_filtered:
        users_adult.append(user['name'])
        print(user['name'])
    print(f"Suaugę 'users', pateikiami masyve: {users_adult}")


filter_dog_owners(users)
filter_adults(users)
