'''
15. Reverse a string manually
python
text = "Python"
reversed_str = ""
for char in text:
    reversed_str = char + reversed_str  # Prepend character
print(reversed_str)  # Output: "nohtyP"
Explanation:

Start with empty string.

Add each new character to the front.

Alternative (slicing):

python
reversed_str = text[::-1]


'''
