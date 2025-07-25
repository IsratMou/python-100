# Remove an element from a list by index.
# --------------------------------------------

'''
type1: remove by index
-------------------------------------------------------------

fruits = ['apple', 'banana', 'orange', 'banana']

# Remove the second element (index 1)
fruits.pop(1)

print(fruits)  # Output: ['apple', 'orange', 'banana']

-------------------------------------------------------------

type2: del statement
-------------------------------------------------------------

fruits = ['apple', 'banana', 'orange', 'banana']

# Remove the second element (index 1)
del fruits[1]

print(fruits)  # Output: ['apple', 'orange', 'banana']  


-------------------------------------------------------------


type3: slice assignment
-------------------------------------------------------------
colors = ['red', 'green', 'blue', 'yellow']

# ইনডেক্স 1-এর এলিমেন্ট রিমুভ
colors = colors[:1] + colors[2:]

print(colors)  # Output: ['red', 'blue', 'yellow']


শুধু রিমুভ করতে চাইলে → del

রিমুভ করা এলিমেন্টও লাগলে → pop()

একাধিক এলিমেন্ট রিমুভ করতে → স্লাইসিং বা del with slice

'''
