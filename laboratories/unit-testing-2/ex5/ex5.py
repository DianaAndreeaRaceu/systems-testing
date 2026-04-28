from faker import Faker

fake = Faker()


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"


# STUB: date fixe, hardcodate
class DatabaseStub:
    def __init__(self):
        self.data = {
            'ana@example.com': Person('Ana Popescu', 22, 'ana@example.com'),
            'ion@example.com': Person('Ion Ionescu', 35, 'ion@example.com'),
            'maria@example.com': Person('Maria Georgescu', 19, 'maria@example.com'),
        }

    def get(self, unique_key):
        return self.data.get(unique_key)


# FAKE: baza de date simplificata, dar functionala
class FakeDatabase:
    def __init__(self, n=500):
        self.data = {}
        while len(self.data) < n:
            person = Person(
                fake.name(),
                fake.random_int(min=18, max=80),
                fake.unique.email()
            )
            self.data[person.email] = person

    def get(self, unique_key):
        return self.data.get(unique_key)

    def get_youngest_person(self):
        return min(self.data.values(), key=lambda person: person.age)

    def get_new_person(self, name, age, email):
        if email in self.data:
            return None
        person = Person(name, age, email)
        self.data[email] = person
        return person


if __name__ == '__main__':
    print("=== TEST STUB ===")
    stub_db = DatabaseStub()
    print(stub_db.get('ana@example.com'))
    print(stub_db.get('ion@example.com'))
    print(stub_db.get('x@example.com'))

    print("\n=== TEST FAKE DATABASE ===")
    fake_db = FakeDatabase(500)
    print("Numar intrari:", len(fake_db.data))

    first_email = next(iter(fake_db.data))
    print("Primul email:", first_email)
    print("Persoana gasita:", fake_db.get(first_email))

    print("\nCea mai tanara persoana:")
    print(fake_db.get_youngest_person())

    print("\nAdaugare persoana noua:")
    print(fake_db.get_new_person("Test User", 25, "testuser@example.com"))

    print("\nCaut persoana nou adaugata:")
    print(fake_db.get("testuser@example.com"))