# Python program to check whether the string is Symmetrical or Palindrome
# -----------------------------------------------------------------------------

'''
স্ট্রিং সিমেট্রিক্যাল কি? (What is Symmetrical String?)
বাংলা: একটি স্ট্রিং সিমেট্রিক্যাল হবে যদি এটিকে মাঝখান থেকে ভাগ করলে দুই ভাগ একই দেখায়।
English: A string is symmetrical if its left half looks exactly like its right half when split in the middle.

উদাহরণ (Example):
"abab" → "ab" | "ab" → সিমেট্রিক্যাল (Symmetrical)

"abcabc" → "abc" | "abc" → সিমেট্রিক্যাল (Symmetrical)

"hello" → "he" | "lo" → সিমেট্রিক্যাল নয় (Not symmetrical)
------------------------------------------------------------

প্যালিনড্রোম স্ট্রিং কি? (What is Palindrome String?)
বাংলা: একটি স্ট্রিং প্যালিনড্রোম হবে যদি এটিকে উল্টে লিখলেও একই থাকে।
English: A string is palindrome if it reads the same backward as forward.

উদাহরণ (Example):
"madam" → উল্টালেও "madam" → প্যালিনড্রোম (Palindrome)

"racecar" → উল্টালেও "racecar" → প্যালিনড্রোম (Palindrome)

"python" → উল্টালে "nohtyp" → প্যালিনড্রোম নয় (Not palindrome)
'''


# Using string slicing
# ===========================================

s = "abab"
# Check if symmetrical (সিমেট্রিক্যাল কি না চেক করা)
half = len(s) // 2

if len(s) % 2 == 0:  # Even length
    left_half = s[:half]
    right_half = s[half:]
else:  # Odd length
    # For odd-length strings, we ignore the middle character when checking symmetry
    left_half = s[:half]
    right_half = s[half+1:]

symmetrical = left_half == right_half
pallindrome = s == s[::-1]

print('symmetrical' if symmetrical else "Not Symmetrical")
print('pallindrome' if pallindrome else "Not Palindrome")


'''
method=2:
    Using reversed iteration

s = "amaama"

# Check palindrome using reversed()
pal = list(s) == list(reversed(s))

# Check symmetry
half = len(s) // 2
sym = s[:half] == s[half:] if len(s) % 2 == 0 else s[:half] == s[half+1:]

print("Symmetrical" if sym else "Not Symmetrical")
print("Palindrome" if pal else "Not Palindrome")

'''
