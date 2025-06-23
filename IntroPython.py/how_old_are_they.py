# Write a program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

# In 3 Examples

# Example 1

def age_riddle():
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

   # This shows all the ages
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

if __name__ == '__main__':
    age_riddle()

# Example 2

def age_guessing(anton, beth, chen, drew, ethan):
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is- " + str(ethan))

if __name__ == '__main__':
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen
    age_guessing(anton, beth, chen, drew, ethan)

# Example 3 IN OOP

class AgeGuessingRiddle():  # Using PascalCase for class names (Python convention)
    def __init__(self):
        # Calculate ages in __init__ instead of taking them as parameters
        self.anton = 21
        self.beth = self.anton + 6
        self.chen = self.beth + 20
        self.drew = self.chen + self.anton
        self.ethan = self.chen

    def output(self):
        print("Anton is " + str(self.anton))
        print("Beth is " + str(self.beth))
        print("Chen is " + str(self.chen))
        print("Drew is " + str(self.drew))
        print("Ethan is " + str(self.ethan))  # Fixed typo in "is-"

if __name__ == '__main__':
    # Create an instance of the riddle
    riddle = AgeGuessingRiddle()
    # Call the output method
    riddle.output()

# Example 4 using loop 
def age_riddle_dict():
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    ages = {
        "Anton": anton,
        "Beth": beth,
        "Chen": chen,
        "Drew": drew,
        "Ethan": ethan
    }

    for name, age in ages.items():
        print(f'{name} is {age}')

if __name__ == '__main__':
    age_riddle_dict()






