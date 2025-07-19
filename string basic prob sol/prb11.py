# Python-এ দুটি স্ট্রিং-এর মধ্যে মিলে যাওয়া ক্যারেক্টার কাউন্ট করার পদ্ধতি
# সমস্যা বোঝা:
# আমাদের দুটি স্ট্রিং দেওয়া হবে, আমাদের বের করতে হবে এই দুটি স্ট্রিং-এ কতগুলো কমন ক্যারেক্টার আছে। ক্যারেক্টারগুলোর পজিশন আলাদা হতে পারে, শুধু ক্যারেক্টার ম্যাচ করলেই হবে।

# উদাহরণ:

# স্ট্রিং 1: "apple"

# স্ট্রিং 2: "pear"

# কমন ক্যারেক্টার: 'p', 'e', 'a'

# টোটাল ম্যাচ: 3
# -------------------------------------------------------------------------

'''
type-1: set intersection
---------------------------------------------------

def count_common_characters(str1, str2):
    set1= set(str1.lower())
    set2= set(str2.lower())
    
    return len( set1 & set2 )
    
print(count_common_characters("apple", "pear"))  # Output: 3
    
    
-------------------------------------------------------------

type-2: counter use kore:
-----------------------------------------------

from collections import Counter

def count_common_chars(str1, str2):
    counter1 = Counter(str1.lower())
    counter2 = Counter(str2.lower())
    common_chars = counter1 & counter2  # Intersection of two counters
    
    return sum(common_chars.values())
print(count_common_chars("apple", "pear"))  # Output: 3 
print(count_common_chars("hello", "world"))  # Output: 2

# -------------------------------------------------------------------------

type-3: list comprehension use kore:
---------------------------------------------------

def count_matching_chars(str1, str2):
    return len([ch for ch in set(str1) if ch in set(str2)])

print(count_matching_chars("hello", "world"))  # Output: 3 ('l', 'o')






'''
