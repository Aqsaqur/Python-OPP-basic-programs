# Write a function that takes a list of numbers
#  and returns the sum of those numbers.
# program Example 3

# def add_many_numbers(numbers: list[int]) -> int:
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# def main() -> None:
#     numbers = []
#     user_input = input("Enter numbers separated by space: ")

#     parts = user_input.split()
#     numbers = [int(x) for x in parts]

#     total_sum = add_many_numbers(numbers)
#     print(f'Sum of Numbers: {total_sum}')

# if __name__ == '__main__':
#     main()

# Example 2 
class add_many_numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_sum(self):
        return sum(self.numbers)
    

def main():
    user_input = input("Enter numbers separated by space: ")
    parts = user_input.split()
    numbers = [int(x) for x in parts]

    obj = add_many_numbers(numbers)
    total_sum = obj.get_sum()
    print(f"Sum of numbers: {total_sum}")

while True:
     main()
     play_again = input("Play again? (y/n): ")
     if play_again.lower() != "y":
            print("Thanks for playing hope it helped,")
            break
