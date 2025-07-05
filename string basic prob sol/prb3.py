# # Reverse Words in a Given String in Python

'''
type-1:
    
sentence=input("Enter a sentence: ")
words=sentence.split()
reversed_words=words[::-1]
reversed_sentence=' '.join(reversed_words)
print("Reversed sentence:",reversed_sentence)

-----------------------------------------------------------

type-2
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = words.reversed()
reversed_sentence = ' '.join(reversed_words)
print("Reversed sentence:", reversed_sentence)


# ------------------------------------------------------
type-3:
    
sentence = input("Enter a sentence: ")
reversed_sentence = ' '.join(reversed(sentence.strip().split()))
print("Reversed sentence:", reversed_sentence)


'''
