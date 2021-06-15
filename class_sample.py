class mysampleClass:
    def hello(self, n):
        self.name = n

    def print_name(self):
        print(self.name)


x = mysampleClass()
y = mysampleClass()
name = "Vishnu"
x.hello(name)
y.hello("Jishnu")

x.print_name()
y.print_name()
