l1 = ['apple', 'banane', 'kiwi', 'orange', 'cerise', 'apple']

l2 = ['Tomato', 'Bringley', 'Potato', 'Carrot']
print(l1.count('apple'))  # Count the number of occurrences of 'apple' in the list


l1.extend(l2) 

print(l1)# Extend l1 with l2 



# a,b,c,d= [1,2,3,4]

# print(a,b,c,d) # Unpacking the values of a,b,c into the variables a,b,c

*a,b,c = l1

print(a)
print(b)
print(c) # Unpacking the values of a,b,c into the variables a,b,c


# for index, value in enumerate(l1):
#     print(index, value)  # Enumerate the list l1 and print the index and value of each element  
    
    
    
    
l3 = [1,2,3,4,5,6,7,8,9,10]



for num, fruit in zip(l3, l1):
    print(num, fruit)  # Zip the two lists l1 and l3 and print the elements of both lists together
    
    
l4=[[1,2],[3,4]]
                #[sub1][sub2]    [1,2][3,4]
flat = [item for sub in l4 for item in sub]


print(flat)