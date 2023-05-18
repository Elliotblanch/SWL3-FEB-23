firstname = input("Please enter first name: ")
lastname = input("Please enter last name: ")
birthmonth = input("Please enter the month you were born in: ")
Birthyear = int(input("Please enter the year you were born in: "))

fullname = firstname + " " + lastname
birthstring = str(Birthyear)

output = fullname + " was born in " + birthmonth + ", " + birthstring

print(output)