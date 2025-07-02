mytuple = ("apple", "banana", "cherry")
print(mytuple)  # Output: ('apple', 'banana', 'cherry')

# A tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.
# Tuples are written with round brackets.

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


'''Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.'''

thistuple = ("apple",)
print(type(thistuple))  # Output: <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # Output: <class 'str'>


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry"))
print(type(thistuple))  # Output: <class 'tuple'>


# Access Tuple Items
# -------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Output: banana

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # Output: cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Output: ('cherry', 'orange', 'kiwi')
print(thistuple[:4])  # Output: ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:])  # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')
# Range of Negative Indexes
print(thistuple[-4:-1])  # Output: ('orange', 'kiwi', 'melon')


# check if an item exists in a tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    # Output: Yes, 'apple' is in the fruits tuple
    print("Yes, 'apple' is in the fruits tuple")


'''Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''

# tuple methods
tup = (1, 2, 3, 4, 5, 2, 2, 4)
# Output: 3 (counts how many times 2 appears in the tuple)
print(tup.count(2))
print(tup.index(2))  # Output: 1
# Output: 1 (returns the index of the first occurrence of 2 in the tuple)

# tuple e amra list & string er moto slicing korte pari
