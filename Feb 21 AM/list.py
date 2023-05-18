list = [1, 2, 5, 3, "Hello", 2.2, True]

print(list)

list[1] = "orange"
print(list)

list.append("Good morning!")
print(list)

list.insert(2, "Point 2 is here!")
print(list)

list.remove("Hello")
print(list)

fruits = ["apple", "banana", "cherry", "apple"]

for x in fruits:
    if x == "apple":
        fruits.remove(x)
        
print(fruits)