#lambda argument: expression


lambda x: x + 1

print((lambda x: x + 1)(5))  # Output: 6


def add(x,y):
    return x + y


lambda x,y: x+y


names = ['tom','Jerry','Mickey','Donald']


sorted_names = sorted(names, key=lambda x: x.lower())  


print(sorted_names)  # Output: ['Donald', 'Jerry', 'Mickey', 'tom']



max_func = lambda x, y: x if x > y else y