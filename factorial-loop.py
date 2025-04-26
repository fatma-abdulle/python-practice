
# This function calculates factorial using a loop.

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Testing the function
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial_loop(number)}")
