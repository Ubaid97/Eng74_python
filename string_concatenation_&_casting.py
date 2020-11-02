# What is concatenation

first_name = 'Ubaid'
last_name = 'Muhammad'
age = 22
print(first_name + " " + last_name, age)

# Casting - used to change variable from one data type to another
# str(), int(), float()

x = "5"
result = age + int(x)
print(str(result))

name = input("Please enter your full name: ")
DOB = input("please enter your date of birth in the format dd/mm/yyyy: ")
age = input("please enter your age: ")
house_number = input("Please enter your house number: ")
address = input("Please enter the first line of your address: ")
postcode = input("Please enter your postcode: ")

print("Full name:", name)
print("Age:", age)
print("DOB:", DOB)
print("Address:", str(house_number), address)
print("Postcode:", postcode)