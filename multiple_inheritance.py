class First:
    def display_first(self):
        print("First")


class Second:
    def display_second(self):
        print("Second")


class Third(First, Second):
    def display_third(self):
        print("Third")


x = Third()
x.display_third()
x.display_second()
