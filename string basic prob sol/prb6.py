# Python program to print even length words in a string
'''
type-1: basic split(), loop
======================================
sentence="Python is pera for me"
wordlist=sentence.split()

for word in wordlist:
    if len(word) % 2 == 0:
        print(word)  # Output: Python is pera  me

====================================

type-2: list comprehension

sentence = "Python is pera for me"
evenwords=[word for word in sentence.split() if len(word) % 2 == 0]
print(evenwords)  # Output: ['Python', 'pera', 'me']



'''
