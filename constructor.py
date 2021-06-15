class constructor:
    year = 2021

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year: " + str(constructor.year))
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Place: " + self.place)

    @classmethod
    def add_year(cls):
        constructor.year = constructor.year + 1

    @staticmethod
    def display_welcome():
        print("Welcome")

constructor.display_welcome()

x = constructor("Vishnu K", 22, "Palakkad")
y = constructor("Jishnu K", 20, "Palakkad")

x.display()
y.display()

print("---------------------")
constructor.year = constructor.year + 1
x.add_age()
y.add_age()

x.relocate("Delhi")
y.relocate("Mumbai")

x.display()
y.display()

print("---------------------")
constructor.add_year()

x.add_age()
y.add_age()

x.display()
y.display()