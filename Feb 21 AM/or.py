a = int(input("Input whole number A: "))
b = int(input("Input whole number B: "))
c = int(input("Input whole number C: "))
if a > b or a > c:
    print("A is not the smallest number")
if b > a or b > c:
    print("B is not the smallest number")
if c > a or c > b:
    print("C is not the smallest number")
else:
    print("All numbers are equal")
