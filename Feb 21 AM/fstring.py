name = input("Please enter your name: ")
age = input("Please enter your age: ")

# an f-string references other variables
output = f"{name} is {age} years old"

# a regular string will not
output = "{name} is {age} years old"

print(output)