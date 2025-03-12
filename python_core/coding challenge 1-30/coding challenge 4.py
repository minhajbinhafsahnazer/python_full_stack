#11. create a Python program that takes two sets
#  and returns a new set containing elements that are common in both input sets.
'''
set1 = set(input("Enter the first set : ").split())
set2 = set(input("Enter the second set : ").split())
common = set()
for i in set1:
    if i in set2:
        common.add(i)
print(common)

'''
#12.Create a Python program that 
# takes a string as input and 
# checks if all the characters in the string are unique (i.e., no character repeats). 
# Return True if all characters are unique, and False otherwise.
unique = set()
common = 0
lang = input("Enter the string : ")
for i in lang :                    
    if i not in unique:
        unique.add(i)
    else:
        common+=1
if common == 0:
    print("True ,all characters are unique")
else:
    print("False , all characters are not unique")


