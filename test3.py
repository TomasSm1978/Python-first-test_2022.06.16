# Turimas "audi" dict.

# Parašykite funkciją "show_object_values", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.
import json

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}

def show_object_values(x):
    # print(list(x.values()))
    new_list = []
    for key, value in x.items():
        new_list.append(value)
    print(new_list)

show_object_values(audi)
