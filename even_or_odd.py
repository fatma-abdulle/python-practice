
# This function checks if a number is even or odd.

def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Testing the function
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check_even_or_odd(num)
    print(f"The number {num} is {result}.")
