# Write a program 
# that doubles each element in a list of numbers. 
# For example, if you start with this list:
# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]
# In 3 Ways

def Double_list():
    numbers: list[int] = [1, 2, 3, 4]

    for i in range(len(numbers)):
        elemt_at_index = numbers[i]
        numbers[i] = elemt_at_index * 2

    print(numbers)


if __name__ == '__main__':
    Double_list()


def Double_list():
    user_input = input("Enter Numbers: ")
    parts = user_input.split()
    numbers: list[int] = parts

    for i in range(len(numbers)):
        elemt_at_index = numbers[i]
        numbers[i] = elemt_at_index * 2

    print(numbers)


if __name__ == '__main__':
    Double_list()

