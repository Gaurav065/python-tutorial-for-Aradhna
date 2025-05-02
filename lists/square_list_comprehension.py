squares =[1-x**2 for x in range(11)]

print(squares)

matrix = [[1,2],[3,4]]


copy = squares.copy()
print(copy)

print(matrix[1][0])

if -15 in squares:
    print("yes")
    
    
a = [4,3,1,5,2]

a.sort(reverse=True)# desc to asc
print(a)
# squares.reverse()
# print(squares)

# max().min().sum()