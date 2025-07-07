# Python program to capitalize the first and last character of each word in a string

'''আমাদের একটি বাক্য দেওয়া আছে, যেখানে প্রতিটি শব্দের প্রথম এবং শেষ অক্ষরকে বড় হাতের (capitalize) করতে হবে, বাকি অক্ষরগুলো ছোট হাতের রাখতে হবে। যেমন:

ইনপুট: "hello world"

আউটপুট: "HellO WorlD"
'''


''' # Type-1: Basic split(), loop
# =====================================================================


def capitalize_first_last(txt):
    wordlist = txt.split()
    result = []

    for word in wordlist:
        if len(word) == 0:
            continue
        elif len(word) == 1:
            new_word = word[0].upper()
        else:
            new_word = word[0].upper() + word[1:-1].lower() + word[-1].upper()
        result.append(new_word)

    return ' '.join(result)


txt = "hello world python programming language"
# Output: "HellO WorlD PythoN ProgramminG LanguagE"
print(capitalize_first_last(txt))
'''

# Type-2: List comprehension
# =====================================================================


def capitalize_first_last(txt):
    return ' '.join(
        [word[0].upper() + word[1:-1].lower() + word[-1].upper()
         if len(word) > 1
         else word[0].upper()
         for word in txt.split()]
    )


txt = "hello world python programming language"
# Output: "HellO WorlD PythoN ProgramminG LanguagE"
print(capitalize_first_last(txt))
