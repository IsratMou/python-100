mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))
# List items are ordered, changeable, and allow duplicate values.
''' When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.'''


list1 = ["abc", 34, True, 40, "male"]
print(type(list1))  # Output: <class 'list'>


# Using the list() constructor to make a List:

# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)


# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])


if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
# Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
print(thislist)


# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']

'''If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:'''

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # Output: ['apple', 'watermelon']


'''The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  # Output: ['apple', 'banana', 'watermelon', 'cherry']


# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
# Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
print(thislist)

'''The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:
'''

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']


'''The remove() method removes the specified item.

    ** If there are more than one item with the specified value, the remove() method removes the first occurrence: **
    
Example
Remove "banana":'''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry']


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry', 'banana', 'kiwi']


'''The pop() method removes the specified index.

Example
Remove the second item:'''

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Output: ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Output: ['banana', 'cherry']

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)  # This will raise an error because the list no longer exists


'''The clear() method empties the list.

The list still remains, but it has no content.'''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output: []


# Python - Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


# using while loop
thislist = ["cat", "dog", "rabbit"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1


'''Python - List Comprehension'''
list2 = ["bangladesh", "india", "pakistan", "nepal"]

[print(x) for x in list2]


for x in ['apple', 'banana', 'cherry']:
    print(x)


# Python - List Comprehension

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)  # Output: ['apple', 'banana', 'mango']

'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']
# The syntax is easy to understand, and the result is a new list, which is exactly what you want.

newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

# using range
newlist3 = [x for x in range(5)]
print(newlist3)  # Output: [0, 1, 2, 3, 4]

# Using range with a condition
list4 = [x for x in range(10) if x < 6]
print(list4)  # Output: [0, 1, 2, 3, 4, 5]

# expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
'''
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)
# Output: ['hello', 'hello', 'hello', 'hello', 'hello']

'''

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']


# Python - Sort Lists

''' Sort List Alphanumerically: by default choto theke boro jabe
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:'''

thislist = ["banana", "cherry", "apple", "kiwi", "mango", "orange"]
thislist.sort()
print(thislist)
# Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # Output: [23, 50, 65, 82, 100]

# Sort Descending- boro theke choto
thislist = ["banana", "cherry", "apple", "kiwi", "mango", "orange"]
thislist.sort(reverse=True)
# Output: ['orange', 'mango', 'kiwi', 'cherry', 'banana', 'apple']
print(thislist)


# Python - Copy Lists

# You can use the built-in List method copy() to copy a list.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# Use the slice Operator
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist = thislist[:]
# Output: ['apple', 'banana', 'cherry' 'orange', 'kiwi', 'melon', 'mango']
print(mylist)


# Python - Join Lists

# ----------------------------------------------------
'''There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

# Python-এ আপনি একটি লিস্টের (list1) মধ্যে আরেকটি লিস্টের (list2) সব আইটেম একে একে যোগ করতে পারেন। এটাকে বলা হয় "Appending Items One by One"।

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]


# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]




'''# Python - List Methods:
-----------------------------------
List Methods:
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list '''
