s1 ={1,2,"hello",True, False,0}


print(len(s1))


s1.add(3)
print(s1)

s1.update([1,2])
print(s1)


# s1.remove(5)
s1.discard(5)


print(s1.pop())   
s1.clear()
print(s1)



# Method	Description
# add(x)	Adds x to the set
# remove(x)	Removes x (error if not present)
# discard(x)	Removes x if present
# pop()	Removes and returns a random element
# clear()	Empties the set
# union(set)	Returns union
# intersection(set)	Returns intersection
# difference(set)	Returns difference
# symmetric_difference()	Elements in either, not both
# issubset(set)	Checks if one set is subset of another
# issuperset(set)	Checks if one set is superset
# isdisjoint(set)	True if no common elements