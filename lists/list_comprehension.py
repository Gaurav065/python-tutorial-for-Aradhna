



# # it is consise way to create a list using a single line of code . it replaces the need for a loop to create a list
# [exprssion/variable for item in iterable]

# # [expression for item in iterable followed by a condition or not]

# # expression is the result of the operation performed on each item in the iterable. The expression can be a variable, a function call, or any other valid Python expression.


# squares = [x**2 for x in range(11)]  # List comprehension to create a list of squares




# even = [x for x in squares if x % 2 == 0]  # List comprehension to filter even squares
# print(even)  # Output: [0, 4, 16, 36, 64, 100]


# print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# # [true expression if condition else false for item in iterable ] 

# pair = [(x,y)for x in range(5) for y in range(5) if x != y]  # List comprehension to create pairs of numbers

# print(pair)



text = 'Hello World! Welcome to python Programming'
result = text.split()
value = [char for char in result if char.isupper()]
print(value)