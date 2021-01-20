# List

"""
#Creating a list
jon_snow = ["Jon snow", "winterfell", 30]
print(jon_snow)

#indexing
print(jon_snow[1])

#length
print (len(jon_snow))
"""
"""
#list-ception
Birthmonths = [["Adi", "Feb"], ["Bhai", "Jan"], ["Moni", "July"]]
print(Birthmonths)
"""
"""
# Merging list
x = [1,2,3,4,5]
y = [6,7,8,9,10]
merged_list = x + y
print(merged_list)
"""
"""
# Adding Elements (append.)
#Empty list
num_list = [1, 2, 3, 4, 5, 6, 8]
num_list.append(9)
num_list.append(7)
print(num_list)
"""
"""
# Removing Elements
House = ["Mumma", " Aunt", "Uncle", "Siblings"]
last_House= House.pop()
print(last_House)
print(House)
"""
"""
#list sort
num = [20, 1, 8, 19, 16]
num.sort()
print(num)
"""
#Creating a list comprehension
nums = [10,20,30,40,50]
nums_triple = []
for n in nums :
       nums_triple.append(n*3)
print(nums)
print(nums_triple)
