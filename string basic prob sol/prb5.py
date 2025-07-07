# string theke space remove kora + len ber ber kora
# ------------------------------------------

'''type-1: replace() use kora:
# ------------------------------------------------------------


txt= "Hello World!"
len_txt = len(txt.replace(" ",''))
print(len_txt)  # Output: 11


# ------------------------------------------------------------



type-2: count () , loop use kora:
---------------------------------------------------------


txt = "Hello World!"
count = 0
for char in txt:    
    if cha != " ":
        count += 1
print(count)    # Output: 11

# ------------------------------------------------------------




type-3: list comprehension use kora:
# ------------------------------------------------------------

txt = "Hello World!"
length= len(''.join([char for char in txt if char!= ' ']))
# print(length)  # Output: 11

--------------------------------------------------------------

type-4: BEST PRACTICE ===fastest and most efficient way:
# ------------------------------------------------------------
txt= "Hello World!"
result= len(txt)-txt.count(" ")
print(result)  # Output: 11

'''
