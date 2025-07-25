# Remove an element from a list by value.
# --------------------------------------------


'''type-1: remove()
fruits = ['apple', 'banana', 'orange', 'banana']

# Remove first occurrence of 'banana'
fruits.remove('banana')

print(fruits)  # Output: ['apple', 'orange', 'banana']

*********************************************************

error handling:
+++++++++++++++++++++++++++

fruits = ['apple', 'orange']

try:
    fruits.remove('banana')
except ValueError:
    print("Value not found in list")



------------------------------------------------------------

type-2:list comprehension
-------------------------------------------------------------

numbers = [1, 2, 3, 4, 2, 6, 2, 2, 9] # Remove all occurrences of 2
value_to_remove = 2
numbers = [num for num in numbers if num != value_to_remove]
print(numbers)


----------------------------------------------------------


type-3: filter() function
----------------------------------------------------------

numbers = [1, 2, 3, 4, 2, 6, 2, 2, 9]  # Remove all occurrences of 2
value_to_remove = 2
numbers = list(filter(lambda x: x != value_to_remove, numbers))
print(numbers)

explanation:
lambda x: x != 2 একটি ছোট ফাংশন তৈরি করে যা:

ইনপুট x নেয়

চেক করে x কি ২ এর সমান নয় কিনা

যদি না হয় True রিটার্ন করে

filter() ফাংশন:

numbers লিস্টের প্রতিটি এলিমেন্টের জন্য lambda ফাংশন কল করে

শুধু True রিটার্ন করা এলিমেন্টগুলো রাখে

[1, 3, 4] এই নতুন লিস্ট তৈরি করে

list() কনভার্শন:

ফিল্টার অবজেক্টকে আবার লিস্টে পরিণত করে


type-4: Using pop() with index() (When You Need the Removed Value)
python
----------------------------------------------------------


fruits = ['apple', 'banana', 'orange']
value = 'banana'
if value in fruits:
    index = fruits.index(value)
    removed = fruits.pop(index)
    print(f"Removed {removed}")


----------------------------------

my_list = [x for x in my_list if x != 30]# Remove an element from a list by value.

'''