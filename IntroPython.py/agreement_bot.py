# Write a program which asks the user what their favorite animal is,
#  and then always responds with "My favorite animal 
# is also ___!" 
# (the blank should be filled in with 
# the user-inputted animal, of course).

# In three ways 

# Example 1

Enter_fav_animal = str(input("Enter Your Fav Animal: "))

def fav_animal():
    print(f"My favorite animal is also {Enter_fav_animal}")

if __name__ == '__main__':
    fav_animal()

# Example 2

def Your_fav_animal(animal):
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    user_input = str(input("Enter your fav animal: "))
    Your_fav_animal(user_input)

# Example 3 In OOP

class Animal():
    def __init__(self, animal):
        self.animal = animal

    def Output(self):
        print(f"My favorite animal is also {self.animal}")

Enter_animal = str(input("Enter Your Fav Animal: "))
Display = Animal(Enter_animal)
Display.Output()

