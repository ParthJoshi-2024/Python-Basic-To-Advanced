# Higher Order Functions in Python

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map Higher Order Function
def is_greater_than_five(num):
    if num>5:
        return True
    else:
        return False


b = list(map(is_greater_than_five, a))
# Filter Higher Order Function
def is_even(num):
    return num % 2 == 0
c = list(filter(is_even, a))

# Lamda Function expression for map and filter
d = list(map(lambda x: x > 5, a))
e = list(filter(lambda x: x % 2 == 0, a))

# Reduce Higher Order Function
from functools import reduce
def add(x, y):
    return x + y
result = reduce(add, a)
# Output results
print("Original List:", a)
print("Map Result (is greater than 5):", b)
print("Filter Result (is even):", c)
print("Map Result (lambda > 5):", d)
print("Filter Result (lambda even):", e)
print("Reduce Result (sum of all elements):", result)
# Output:
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Map Result (is greater than 5): [False, False, False, False, False, True, True, True, True, True, True]
# Filter Result (is even): [2, 4, 6, 8, 10]
# Map Result (lambda > 5): [False, False, False, False, False, True, True, True, True, True]
# Filter Result (lambda even): [2, 4, 6, 8, 10]
# Reduce Result (sum of all elements): 55
