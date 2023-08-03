string = input("Please enter string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string
print(f"The reverse string is: {reversed_string} ")