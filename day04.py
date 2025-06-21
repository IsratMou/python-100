# BRO CODE PYTHON COURSE
# ---------------------------


# #this is my first python program

# print("I like pizza!")
# print("Its really good")

# #strings
# first_name="Israt"
# food='pizza'
# email="israt@gmail.com"

# print(first_name)
# print(f"Hello , {first_name}")
# print(f'You like {food}')
# print(f"Your name is {email}")


# #integer
# age=25
# quantity=3
# num_of_students=30

# print(f"You are {age} years old.")
# print(f"You are buying {quantity} items.")
# print(f"Your class has {num_of_students} students.")

# #float
# price=10.99
# gpa=3.2
# distance=5.5

# print(f"The price is ${price}")
# print(f"Your gpa is {gpa} .")
# print(f"You ran {distance} km")

# #boolean
# is_student = True
# for_sale= False
# is_online= True

# print(f"Are you a student?: {is_student}")

# if is_student:
#     print("You are a student")

# else:
#     print("You are not a student")

# if for_sale:
#     print("that item is for sale")

# else:
#     print("that item is not available")


# if is_online:
#     print("You are a online")

# else:
#     print("You are offline ")


# #homework

# user_name="Mou"
# year=2024
# pi=3.14
# is_admin=True

# print(f"hi, Your name is {user_name}")
# print(f"You are in {year}")
# print(f"pi is ={pi}")

# if is_admin:
#     print("Admin is active")

# else:
#     print("Admin is offline")


# #typecasting

# name="Istat Mou"
# age=25
# gpa=3.2
# is_student= True

# gpa=int(gpa)   #float to int
# age=float(age)

# print(type(name))

# print(gpa)
# print(age)


# input

# name = input("what is your name? ")
# age = int(input("How old are you? "))

# age = age+1

# print(f"Hello,{name}!")
# print("Happy Birthday!")
# print(f"You are {age} years old.")


# exercise-1
# ------------------------
# Calculate the area of a rectangle

# length = float(input("Enter the length of the rectangle: "))

# width = float(input("Enter the width of the rectangle: "))

# area = length * width

# print(f"the area of the rectangle = {area} cm²")  # alt+0178= ²

# exercise-2
# ------------------------

# shopping cart program
# --------------------------------

item = input("Enter the item name: ")
price = float(input("Enter the item price: "))
quantity = float(input("Enter the item quantity: "))

total_price = price * quantity
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Price: ${total_price:.2f}")
