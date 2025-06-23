# Prompt the user to enter the lengths of each side of a 
# triangle and then calculate 
# and print the perimeter of the triangle 
# (the sum of all of the side lengths).

# In 3 Exapmple

def main():
    # Get the 3 side lengths of the triangle
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

# Exampe 2 In OOP

class Triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def output(self):
        print(f'The perimeter of the triangle is {self.side1 + self.side2 + self.side3}')

Enter_side1 = float(input("What is the length of side 1? "))
Enter_side2 = float(input("What is the length of side 2? "))
Enter_side3 = float(input("What is the length of side 3? "))

display = Triangle(Enter_side1, Enter_side2, Enter_side3)
display.output()

# Example 3
def triangle_perimeter_dict():
    sides = {}
    for i in range(1, 4):
        sides[f'side{i}'] = float(input(f"What is the lenght of the side {i}? "))

    perimeter = sum(sides.values())
    print(f'The perimeter of the triangle is {perimeter}')

if __name__ == '__main__':
    triangle_perimeter_dict()

