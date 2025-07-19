# Python-এ সব স্বরবর্ণ (vowels) আছে এমন স্ট্রিং চেক করার পদ্ধতি
# সমস্যা বোঝা:
# আমাদের এমন একটি প্রোগ্রাম তৈরি করতে হবে যা একটি স্ট্রিং-এ ইংরেজির সবগুলো স্বরবর্ণ (a, e, i, o, u) আছে কিনা তা চেক করবে। স্বরবর্ণগুলো ছোট হাতের বা বড় হাতের যেকোনো ফরম্যাটে থাকতে পারে।

'''typre-1: set comparison
--------------------------------------------

# ধাপ ১: প্রথমে একটি সেট তৈরি করব যা সব স্বরবর্ণ ধারণ করবে।
# ধাপ ২: তারপর ইনপুট স্ট্রিং থেকে স্বরবর্ণগুলো বের করব এবং সেটে রূপান্তর করব।
# ধাপ ৩: চেক করব যে ইনপুট স্ট্রিং-এর স্বরবর্ণের সেটটি আমাদের স্বরবর্ণের সেটের সমান কিনা।

def contains_all_vowels(txt):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    return vowels.issubset(txt.lower())
    
print(contains_all_vowels("Educations"))  #output: True
print(contains_all_vowels("Hello World")) #output: False


----------------------------------------------------------

type-2:   list comprehension
---------------------------------------------
def contains_all_vowels(txt):
    vowelslist = ['a', 'e', 'i', 'o', 'u']
    txt_lower = txt.lower()
    
    return all(vowel in txt_lower for vowel in vowelslist)
    
print(contains_all_vowels("Educations"))  #output: True
print(contains_all_vowels("Hello World")) #output: False
    
    
----------------------------------------------------------


type-3: using user input:
------------------------------

def check_all_vowels():
    text = input("Enter a string to check for all vowels: ")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    if vowels.issubset(text.lower()):
        print("The string contains ALL vowels (a, e, i, o, u)")
    else:
        missing = vowels - set(text.lower())
        print(f"The string is MISSING these vowels: {', '.join(sorted(missing))}")

check_all_vowels()
    


'''
