# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# Example 1

def Square():
    num = float(input("Type a number to see its square: ")) # Make sure to cast the input to a float so we can do math with it!
    print(str(num) + " squared is " + str(num ** 2)) # num * num is equivalent to num ** 2. The ** operator raises something to a power!



if __name__ == '__main__':
    Square()


# Example 2 In OOP
class Square():
    def __init__(self, num):
        self.num = num

    def ouput(self):
        print(str(self.num) + " squared is " + str(self.num ** 2))
         # num * num is equivalent to num ** 2. The ** operator raises something to a power!

enter_power = float(input("Type a number to see its square: "))
display = Square(enter_power)
display.ouput()

# Example 3

def Squareing(num):
    print(str(num) + " squared is " + str(num ** 2))

if __name__ == '__main__':
    enter = float = float(input("Type a number to see its square: ")) # Make sure to cast the input to a float so we can do math with it!
    Squareing(enter)

