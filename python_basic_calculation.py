class Calculator():
    def _init_(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        return self.num1 + self.num2


    def sub(self):
        return self.num1 - self.num2


    def mul(self):
        return self.num1 * self.num2


    def div(self):
        return self.num1 / self.num2


    def mod(self):
            return self.num1 % self.num2


num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))


obj = Calculator(num1,num2)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Modulus")


    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    elif choice == 3:
        print("Result: ",obj.div())