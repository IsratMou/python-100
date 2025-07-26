# 8. Create list of squares
# ---------------------------------

squares = []
for num in range(1, 6):
    squares.append(num ** 2)  # Square: num**2
print(squares)  # Output: [1, 4, 9, 16, 25]

# Explanation: ** is the exponent operator.

# Alternative (list comprehension):
# ------------------------------------------------


squares = [num**2 for num in range(1, 6)]
