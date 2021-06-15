class sample:
    def set_name(self, name):
        self.name = name

    def __add__(self, other):
        name = self.name +" "+ other.name
        return name


first_name = sample()
second_name = sample()

first_name.set_name("Vishnu")
second_name.set_name("Krishna")

full_name = first_name + second_name
print(full_name)
