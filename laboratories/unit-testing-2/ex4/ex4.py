#TODO Creati o baza de date fake ce contine minim 500 de intrari. 
# O intrare este reprezentata de o instanta a clasei Person (pe care trebuie sa o creati) 
# care are minim 3 atribute (nume, varsta, email). Cheia unica este representata de adresa de mail. 
from faker import Faker

fake = Faker()

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"


def create_fake_database(n=500):
    database = {}

    while len(database) < n:
        name = fake.name()
        age = fake.random_int(min=18, max=80)
        email = fake.unique.email()

        person = Person(name, age, email)
        database[email] = person

    return database


if __name__ == '__main__':
    db = create_fake_database()
    print(f"Numar intrari: {len(db)}")

    first_key = next(iter(db))
    print("Exemplu intrare:")
    print(first_key, "->", db[first_key])