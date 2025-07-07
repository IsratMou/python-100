# Python - Uppercase Half String
# For example, given the string "python", the output could be "PYThon" (uppercase first half) or "pytHON" (uppercase second half).

'''detailed type:
-----------------------------------
(for even length string)
===============================

txt="python"
half_length= len(txt)//2

# Uppercase first half
1st_upper=txt[:half_length].upper()+ txt[half_length:]
print(1st_upper)  # Output: PYTHON

# Uppercase second half
2nd_upper=txt[:half_length]+ txt[half_length:].upper()
print(2nd_upper)  # Output: pyTHON  


for odd length string
===============================
txt = "python3"
half_length = len(txt) // 2

# upper first half
result = txt[:half_length + 1].upper() + txt[half_length + 1:]
print(result)  # output:PYTHon3

# upper second half
result = txt[:half_length + 1] + txt[half_length + 1:].upper()
print(result)  # output:pythON3

-------------------------------------------------------------------


type-2: user input
=======================================

txt= input("Enter a string: ")
half_length = len(txt) // 2 

choice=input("uppercase which half (first/second): ").strip().lower()

if choice == "first":
    result = txt[:half_length].upper() + txt[half_length:]
elif choice == "second":
    result = txt[:half_length] + txt[half_length:].upper()
else:    
    print("Invalid choice")
print(result)


note: আমি ইউজার ইনপুটের উদাহরণে বিজোড় দৈর্ঘ্যের জন্য আলাদা কোড করিনি কারণ Python-এর ইন্টিজার ডিভিশন (//) অটোমেটিক্যালি বিজোড় সংখ্যার জন্য কাজ করে দেয়। আসুন বিস্তারিত বুঝি:

কীভাবে কাজ করে:
len(text) // 2 এর ম্যাথমেটিক্স:

জোড় দৈর্ঘ্য (যেমন 6): 6 // 2 = 3 → প্রথমার্ধ 0-3, শেষার্ধ 3-6

বিজোড় দৈর্ঘ্য (যেমন 5): 5 // 2 = 2 → প্রথমার্ধ 0-2, শেষার্ধ 2-5






'''
