# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atliks nurodytas užduotis:
# 1. funkcija "get_user_average_age" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus vidurkį kaip skaičių.
# 2. funkcija "get_user_names" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]


def get_user_average_age(x):
    age_sum = 0
    for user in x:
        age_sum += user['age']
    print(f"Visų 'users' amžiaus vidurkis yra: {round((age_sum / len(x)), 2)} metai(-ų)")


def get_user_names(x):
    user_names_list = []
    for user in x:
        user_names_list.append(user['name'])
        user_names_list.sort()
    print(f"'Users vardai naujame list'e: {user_names_list}")


get_user_average_age(users)
get_user_names(users)
