# This function calculates the sum of the digits of a number.

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

# Testing the function
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Sum of digits of {number} is {sum_of_digits(number)}")
