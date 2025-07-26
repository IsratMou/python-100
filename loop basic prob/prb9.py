'''

9. Loop through dictionary
----------------------------------


person = {"name": "Alice", "age": 30}
for key, value in person.items():  # Get key-value pairs
    print(f"{key}: {value}")
    
    
Output:
name: Alice
age: 30

Alternative (keys only):
-----------------------------------


for key in person:
    print(key, "->", person[key])  # Access value by key

'''
