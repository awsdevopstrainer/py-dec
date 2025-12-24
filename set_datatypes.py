# myset = {1,2,4,5,6,6,5,4,3,3,2,5,6,7,7}

# print(myset)

# myset.add(55)
# myset.add(0)

# print(myset)

# myset.discard(5)

# print(myset)

# print(dir(myset))


# # myset.remove(655)

# # myset.discard(987)

# myset.remove(55)

# print(myset)

# # Update in set - updating the new list/tuples/set into the existing set

# newnames = ["santosh","Venkat"] # list of values

# myset.update(newnames)
# print(len(myset))

# for i in myset:
#     print(i)

# set operations


a = {1,2,3,4,5,6,2,3,1,2,4}
b = {4,5,6,7,8,9,6,43,4,23}

print("Union Operation")
# print(a|b)
print(a.union(b))

print("Intersection operation")
print(a.intersection(b))
# print(a & b)

print("Set Difference")

print(a-b)
print(a.difference(b))

print(a ^ b)
print(a.symmetric_difference(b))

if a == b:
    print("both set are equal")
else:
    print("Both are not equal")
    
c = {1,2}

print(c.issubset(a))
