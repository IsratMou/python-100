print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Looping Through a String

for x in "babababababa":
    print(x)

# To check if a certain phrase or character is present in a string, we can use the keyword in.

text = "The rain in Spain stays mainly in the plain"

print("plain" in text)

#  way-2:
if "stays" in text:
    print("yes it does")
else:
    print("no it does not")


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
a = "Hello, World!"
print(a.upper())

# The strip() method removes any whitespace from the beginning or the end:

p = " Hello, World! "
print(p.strip())  # returns "Hello, World!"

q = "Hello, World!"
print(q.replace("H", "J"))  # returns "Jello, World!"

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# string concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# string formatting
# --------------------------

# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt2 = f"The price is {20 * 59} dollars"
print(txt2)


# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# Note: All string methods return new values. They do not change the original string.

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

str1 = "this is a string .\nwe are creating with python"
str2 = 'this is also a string'
str3 = """this is a string"""
print(str1)
print(str2)
print(str3)
