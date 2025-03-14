class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def display(self):
        return f'{self.name} is {self.age} years old'

    @classmethod
    def from_birth_year(cls, name, birth_year):
        name = name
        age = birth_year
        return cls(name, age)

    @classmethod
    def is_adult(cls, age):
        if age > 18:
            return True
        return False



# код для проверки
person1 = Person("John", 28)
print(person1.display) # John is 28 years old

person2 = Person.from_birth_year("Mike", 1995)
print(person2.display)  # Mike is 26 years old

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
