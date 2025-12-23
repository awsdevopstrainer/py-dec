# print(nums[2])
# print(nums[-3])
# sub_nums = []
# for i in range(2,6):
#     sub_nums.append(nums[i])
# print(nums[2:6])    

# sub_nums = nums[-6:-1]
# print(sub_nums)

# print(nums[4:])


# print(nums[6])

# print(nums[:])
# print(nums)

# print(nums[:9])

# print(nums)

# rev_list = []

# n = len(nums)

# while n > 0:
#     rev_list.append(nums[n-1])
#     n -= 1
# print(rev_list)
# nums[::-1]

nums = [1,2,3,4,5,2,3,4,5,6]

print(len(nums))

# append() -add more items in to the list
# extend()
# insert()
# remove()
# count()
# index()
# sort()
# pop()
print(nums)

nums.append(123)
print(nums)

nums.insert(2,123)
print(nums)

nums[3] = 567

print(nums)

new_nums = [43,534,534,534,534]

nums.extend(new_nums)

print(nums)

nums.remove(567)

print(nums)

nums.remove(534)
print(nums)

nums.remove(nums[5])
print(nums)

del nums[2]

print(nums)

del nums[2:5]

print(nums)

new_values = [6456,3453245]
nums[2:2] = new_values

print(nums)

print(nums.count(534))

print(nums.index(534))

nums.sort()

print(nums)

nums.pop()

print(nums)

print(dir(nums))

newnums = nums.copy()
print(newnums)

nums[0] = "santhosh"

print(nums)

print(newnums)

# newnums.reverse()
newnums = newnums[::-1]

print(newnums)


newnums.clear()

print(newnums)
