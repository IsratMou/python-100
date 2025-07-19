'''
Python-এ সেট ব্যবহার করে স্ট্রিং-এর স্বরবর্ণ গণনা
সমস্যা বোঝা:
আমাদের একটি স্ট্রিং দেওয়া হবে এবং আমাদের সেট ব্যবহার করে স্ট্রিং-এ কতগুলো স্বরবর্ণ (vowel) আছে তা গণনা করতে হবে। ইংরেজিতে স্বরবর্ণ হলো: a, e, i, o, u (ছোট হাতের এবং বড় হাতের উভয়ই)।

উদাহরণ:

ইনপুট: "Beautiful Day"

আউটপুট: 6 (e, a, u, i, a, y নয় - কারণ 'y' স্বরবর্ণ নয়)

'''

'''
def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

print(count_vowels("Beautiful Day"))  # Output: 6


'''
# ২. লিস্ট কম্প্রিহেনশন ব্যবহার করে:


def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([char for char in text.lower() if char in vowels])


print(count_vowels("Hello World"))  # Output: 3


'''
type-3: user input use kore:
---------------------------------------------------

def main():
    text = input("Enter a string: ")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = sum(1 for char in text.lower() if char in vowels)
    
    print(f"Number of vowels: {count}")
    print(f"Vowels found: {', '.join(set(text.lower()) & vowels)}")

if __name__ == "__main__":
    main()
    
'''