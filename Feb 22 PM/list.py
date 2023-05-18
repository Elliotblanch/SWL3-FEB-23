mylist = [1, 2, 5, 3, "Hello", True, 3.2]

print(mylist)
print(mylist[4])

mylist[1] = "I'm here now"
print(mylist)

mylist.append("And so am I!")
print(mylist)

mylist.insert(4, False)
print(mylist)

mylist.remove("Hello")
print(mylist)

fruits = ["apple", "banana", "cherry", "apple"]

fruits.remove("apple")
print(fruits)