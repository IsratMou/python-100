# Python Booleans

a = 200
b = 30

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.


# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.


# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


def myfuction():
    return False


x = myfuction()
print(x)


def myfunction1():
    return True


if myfunction1():
    print("yes")
else:
    print("no")

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))


# Python Operators--------------------------------

# Arithmetic operators---- **	Exponentiation->	x ** y	, //	Floor division->	x // y

# Assignment operators---- +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=
# Comparison operators---- ==, !=, >, <, >=, <=
# Logical operators---- and, or, not
# Identity operators---- is, is not
# Membership operators---- in, not in
# # Bitwise operators---- & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)


# Python Operators Precedence
# If two operators have the same precedence, the expression is evaluated from left to right.
# Operator	Description
# ()	Parentheses
# **	Exponentiation
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# not	Logical NOT
# and	AND
# or	OR

''' conditional statements:
# ------------------------------------------
if (condition):
    statement 1
elif (condition):
    statement 2
else:
    statement 3 '''

age = 21
if age < 18:
    print("You are a minor.")
    print("You are not allowed to vote.")
else:
    print("You are an adult.")
    print("You are allowed to vote.")


light = "green"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready")
else:
    print("Go")


num = 5

if num > 2:
    print("Greater than 2")
elif (num > 3):
    print("Greater than 3")
else:
    print("Less than or equal to 2")


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
elif marks >= 50 and marks < 60:
    print("Grade E")
else:
    print("Grade F")


"""nested if statements:
# ------------------------------------------
# if (condition):
#     if (condition):    
#         statement 1    
#     else:
#         statement 2
# else:
#     statement 3  """

age = 34
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can drink alcohol.")
    else:
        print("You cannot drink alcohol.")
else:
    print("You are a minor.")
    if age >= 16:
        print("You can drive a car.")
    else:
        print("You cannot drive a car.")


# practice of if-else statements
# number = int(input("Enter a number: "))

# if number//2==0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")

# divided by 7 or not

num = 24

if (num % 7 == 0):
    print(f"{num} is divisible by 7.")
else:
    print(f"{num} is not divisible by 7.")
