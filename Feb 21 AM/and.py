a = int(input("Input whole number A: "))
b = int(input("Input whole number B: "))
c = int(input("Input whole number C: "))

if a > b and a > c:
    print("A is the largest number")
    if a == 0:
        print("A is equal to 0")
    if b > c:
        print("and C is the smallest number")
    elif c > b:
        print("and B is the smallest")
    else:
        print("and B & C are equal")   
elif b > a and b > c:
    print("B is the largest number")
    if b == 0:
        print("B is equal to 0")
    if a > c:
        print("and C is the smallest")
    elif c > a:
        print("and A is the smallest")
    else:
        print("and A & C are equal")
elif c > a and c > b:
    print("C is the largest number")
    if c == 0:
        print("C is equal to 0")
    if c == 5:
        pass
    if a > b and d > b:
        print("and B is the smallest")
    elif b > a and d > a:
        print("and A is the smallest")
    else:
        print("and A & B are equal")