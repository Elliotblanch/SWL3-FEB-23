fruits = ["apple", "banana", "cherry", "apple"]

for x in fruits:
    print(x)

print(50 * "=")

a = 0
for x in fruits:
    a +=1
print(a)

for x in fruits:
    if x == "apple":
        fruits.remove(x)
        
print(fruits)