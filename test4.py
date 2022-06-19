
# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title: str, director: str, budget: int):
        self.title = title
        self.director = director
        self.budget = budget

    def __repr__(self):
        return(f"{self.title}, {self.director}, {self.budget}")

    def was_expensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False

m1 = Movie('Pirates of the Caribbean: On Stranger Tides', 'Rob Marshall', 422000000)
m2 = Movie('Toy Story 4', 'Josh Cooley', 200000000)
m3 = Movie('Juno', 'Jennifer Garner', 7500000)

print(f"{m1}, {m1.was_expensive()}")
print(f"{m2}, {m2.was_expensive()}")
print(f"{m3}, {m3.was_expensive()}")
