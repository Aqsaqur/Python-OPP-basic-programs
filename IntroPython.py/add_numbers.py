# Write a Python program that takes
# two integer inputs from the user 
# and calculates their sum.

class Calculate():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def output(self):
        print(f"The Total Sum: {self.num1 + self.num2}")

number1 = int(input("Enter Num 1: "))
number2 = int(input("Enter Num 2: "))

display = Calculate(number1, number2)
display.output()

# def Calculate_two_number():
#     num1 = int(input("Enter Number 1: "))
#     num2  = int(input("Enter Number 2: "))

#     print("The Total Sum:", num1 + num2)

# if __name__ == '__main__':
#     Calculate_two_number()


