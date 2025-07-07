# Python program to check if a string has at least one letter and one number

'''type-1:
# ==========================================================

txt = "Python3"
has_letter = any(char.isalpha() for char in txt)
has_number = any(char.isdigit() for char in txt)
if has_letter and has_number:
    print("The string has at least one letter and one number.")
else:
    print("The string does not have at least one letter and one number.")
    

==============================================================================

type-2: using regex (Regular expressions (regex))=(for expert users)
# ==========================================================

import re
s = "Python123"

# checks for lettors
l = bool(re.search(r'[a-zA-Z]', s))  
# checks for digits 
n = bool(re.search(r'\d', s))  

if l and n:
    print(True)
else:
    print(False)


# ==========================================================


type-3: manual check
# ==========================================================

txt = "Python3"
has_letter = False
has_number = False

for char in txt:
    if char.isalpha():  
        has_letter = True
    elif char.isdigit():  
        has_number = True

if has_letter and has_number:
    print("The string has at least one letter and one number.")
else:
    print("The string does not have at least one letter and one number")                           

    '''
