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
