# Python program to store frequency of a number in a Dictionary
num=[1,3,5,7,8,99,7,5,3,4,4,34,34,23,56,77]
freq_map={}

for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1
print(freq_map)

# print (freq_map[3])

## Time Complexity of the above problem is --> O(n)

## Space Complexity of the above problem is --> O(n)

# Problem --02 

nums=[1,3,5,7,8,99,7,5,3,4,4,34,34,23,56,77]

Hash_map={}

for i in range(0, len(nums)):
    Hash_map [nums[i]]=Hash_map.get(nums[i],0)+1
print(Hash_map)
