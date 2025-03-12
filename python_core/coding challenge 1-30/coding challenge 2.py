
#coding challenge 1.4 
#Write a Python program that takes a list of numbers as input and calculates and
# prints the sum and  average of those numbers.''

'''
my_list = list(map(int, input("Enter Number by space : ").split()))

total = sum(my_list)
avg = total/len(my_list)
print("sum = ",total)
print("avg = ",avg)

'''

#5. Reverse a List
# Write a Python function that takes a list and returns a new list with the elements 
#reversed. Do this without using the built-in reverse method.
'''
my_list = list(input("Enter string With space : ").split())
def fun():
    new_list = my_list[::-1]
    print(new_list)
    
fun()
'''

#6. Create a Python function that takes a list as input and removes duplicate elements, preserving the order of the elements. Return the new list.
''''
unique_one = []
store = ""
def fun():
    global unique_one,store
    my_list = input("Enter the list uin spaces :").split()

    for i in my_list:
        if i not in unique_one:
          unique_one.append(i)
          store+=i
    print(store) 
fun()
'''

#7 .create a Python program that takes two lists and returns a new list containing elements that are common in both input lists.
'''new_list = []
list1 = list(input("Enter List1 : ").split())   #space makes it help to add space seperated word like apple
list2 = list(input("Enter List2 : ").split())
for i in list1:
    if i in list2:
        new_list.append(i)

print(new_list)
'''

#8.  Write a Python function that takes a list and an element as input and counts how many times that element appears in the list.
times = 0
def fun():
    global times
    list1 = list(input("Enter the whole list :").split())
    element = list(input("Enter the single element to check occurence : ").split()) 
    for i in list1:
        if i in element:
            times+=1
    print("Number of occurences :",times)
fun()