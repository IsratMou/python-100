'''
7. Print list in reverse order
---------------------------------

numbers = [10, 20, 30]
for num in reversed(numbers):  # Built-in reversed()
    print(num)
Output: 30, 20, 10


Alternative (negative indexing): 

---------------------------------

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])  # Start from last index, go backwards
    
    
'''
