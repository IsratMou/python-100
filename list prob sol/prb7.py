'''
7. Access a sublist using slicing
python
------------------------------------------
my_list = [10, 20, 30, 40, 50, 60]
sublist = my_list[1:3]  # Elements from index 1 to 2 (end index excluded)
print(sublist)  # Output: [20, 30]
Explanation: Slicing syntax [start:stop:step] extracts a portion.
by Default start=0, stop=len(list), step=1.
'''

'''
Alternative: Get every other element:

my_list = [10, 20, 30, 40, 50, 60]
print(my_list[::2])  # Output: [10, 30, 50]

'''
