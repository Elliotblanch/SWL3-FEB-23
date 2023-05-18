mylist = [1, 2, 5, 3, "Hello", True, 3.2]
fruits = ["apple", "banana", "cherry", "apple"]

for r in mylist:
    print(r)

b = 0
for x in mylist:
    b += 1
print(b)

print(50 * "=")

a = 0
for x in range(1,101):
    a += 1
    print(a)

for x in fruits:
    if x == "apple":
        fruits.remove(x)
print(fruits)
