
# This function sums all elements in a list without using the built-in sum() function.

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num  # Add each number to the total
    return total

# Testing the function
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    result = sum_list(sample_list)
    print(f"The sum of {sample_list} is {result}")