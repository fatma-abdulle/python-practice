
# This function reverses a string without using [::-1] or built-in methods.

def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Testing the function
if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"The reversed string is: {reverse_string(text)}")
