'''
10. Count vowels in a string
---------------------------------

text = "Hello"
vowels = "aeiou"
count = 0
for char in text:
    if char.lower() in vowels:  # Convert to lowercase
        count += 1
print(count)  # Output: 2 (e, o)
Explanation:

char.lower() ensures case-insensitive comparison.

Check if character exists in the vowels string.


'''
