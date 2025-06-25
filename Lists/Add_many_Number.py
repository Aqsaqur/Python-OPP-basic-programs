# Write a function that takes a list of numbers
#  and returns the sum of those numbers.
# make it in gui
# program in 3 Examples 3

def add_many_numbers(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

def main() -> None:
    numbers = []
    user_input = input("Enter numbers separated by space: ")

    parts = user_input.split()
    numbers = [int(x) for x in parts]

    total_sum = add_many_numbers(numbers)
    print(f'Sum of Numbers: {total_sum}')

if __name__ == '__main__':
    main()

# Example 2 
# Very beginner an d not clean 
# class AddManyNumbers:
#     def __init__(self, numbers):
#         self.numbers = numbers

#     def get_sum(self):
#         return sum(self.numbers)
    

# def main():
#     user_input = input("Enter numbers separated by space: ")
#     parts = user_input.split()
#     numbers = [int(x) for x in parts]

#     obj = AddManyNumbers(numbers)
#     total_sum = obj.get_sum()
#     print(f"Sum of numbers: {total_sum}")

# while True:
#      main()
#      play_again = input("Play again? (y/n): ")
#      if play_again.lower() != "y":
#             print("Thanks for playing hope it helped,")
#             break
#      try:
          
#         numbers = [int(x) for x in parts]
#      except ValueError:
#         print("Please enter valid integers only.")
#         continue


# class AddNumberManager:
#     def __init__(self, numbers):
#         self.numbers = numbers

#     def get_sum(self):
#         return sum(self.numbers)
    
# def main():
#     while True: 
#         user_input = input("Enter Numbers Separated By Space: ")
#         parts = user_input.split()
#         try: 
#             numbers = [int(x) for x in parts]
#             break
#         except ValueError:
#             print(f"Please Enter Invalid integers.!!!")

#     obj = AddNumberManager(numbers)
#     total_sum = obj.get_sum()
#     print(f'The Sum of Numbers: {total_sum}')

# while True: 
#     main()
#     play_again = input("Play Again? (y/n): ")
#     if play_again.lower() != 'y':
#         break

class AddManyNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_sum(self):
        return sum(self.numbers)

def main():
    while True:
        user_input = input("Enter numbers separated by space: ")
        parts = user_input.split()

        try:
            numbers = [int(x) for x in parts]
            obj = AddManyNumbers(numbers)
            total_sum = obj.get_sum()
            print(f"Sum of numbers: {total_sum}")
            break  # Exit after successful calculation
        except ValueError:
            print("Please enter valid integers only.")

# Main loop to play again
while True:
    main()
    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Exiting program...")
        break

