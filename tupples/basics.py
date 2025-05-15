

## what is a tuple?
# A tuple is a collection of ordered elements, similar to a list, but it is immutable (cannot be changed).
# Tuples are defined using parentheses () and can contain elements of different data types.

t1 = (1,2,3,4,5)

t3 = ('a', 'b', 'c', 'd', 'e')
l1 = list(t1)

print(type(l1), l1)

l1 = tuple(l1)
print(type(l1), l1)

# int
# float
# str
# list
# dict
# set
# tuple
# bool
t2 = (1, 2.5, 'hello', [1, 2, 3], {'key': 'value'}, {1, 2, 3}, (4, 5), True)


print(t1[-1])


print(t1+t3)

print(t1*2)


t1.count(1)
print(t1.index(5))