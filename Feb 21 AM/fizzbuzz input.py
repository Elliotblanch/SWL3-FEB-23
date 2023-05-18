fizz = int(input("What number is fizz? "))
buzz = int(input("What number is buzz? "))

for num in range(1, 101):
    if num % fizz == 0 and num % buzz == 0:
        print("FizzBuzz")
    elif num % fizz == 0:
        print("Fizz")
    elif num % buzz == 0:
        print("Buzz")
    else:
        print(num)