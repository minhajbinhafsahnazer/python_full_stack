#24.Write a Python program that uses list comprehension to create a new list containing the squares of the numbers from 1 to 10.
'''
squares = [x**2 for x in range(1, 11)]
print(squares)



#25.Write a Python program that uses a "for" loop to iterate over a string and prints out each character along with its count.

n=1
text = "HELLO WORLD"
for i in text:
    print("character no ",n,":",i)
    n+=1
print()

'''
#26.Write a Python program that uses a list comprehension to create a new list that contains only the uppercase letters in an existing list of strings.
'''
word = ["HELLO","WOrld","PYtHAgOraS","ThREE"]
upper = [char for i in word for char in i if char.isupper()]
print(upper)

'''

#27.To write a program in python find the  second smallest and  third largest number in a  list.
'''
num = [11,22,33,45,34,35,77,88,99]
sorted_list = sorted(num)
print("second smallest no :",sorted_list[1])
print("third largest no :",sorted_list[-3])

'''


#28.Write a Python program to remove duplicates from a list while preserving the order of elements.

list1 = [2,3,2,3,4,5,3,2,1,4,6,7,5,3]
unique = set()
for i in list1:
        unique.add(i)
print(unique)
'''
#ANOTHER METHOD
'''
list1=[2,3,2,3,4,5,3,2,1,4,6,7,5,3]
unique = set(list1)
print(unique)
