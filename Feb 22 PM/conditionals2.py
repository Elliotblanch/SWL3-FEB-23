a = int(input("Please enter value for A: "))
b = int(input("Please enter value for B: "))
c = int(input("Please enter value for C: "))

if a > b and a > c:
    print("A is the largest number")
    if b > c:
        print("and C is the smallest")
    elif c > b:
        print("and B is the smallest")
    else:
        print("and B & C are equal")
    
elif b > a and b > c:
    print("B is the largest number")
    if a > c:
        print("and C is the smallest")
    elif c > a:
        print("and A is the smallest")
    else:
        print("and A & C are equal")
elif c > a and c > b:
    print("C is the largest number")
    if a > b:
        print("and B is the smallest")
    if b > a:
        print("and A is the smallest")
    else:
        print("and A & B are equal")

