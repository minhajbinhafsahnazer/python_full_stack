#9.Write a Python function that takes a tuple and an element as input and counts how many times that element appears in the tuple.
'''def fun():
    tup1 = tuple(input("Enter the whole tuple : "))
    tup2 = tuple(input("Enter the specific tuple element : "))

    count = 0
    for i in tup1:
        if i in tup2:
            count+=1
    print("Number of occurences :",count)
fun()'''


#10.Write a Python program that takes a list of person tuples (name, age) and calculates and prints the  average age of the group

n = int(input("Enter the number of peoples : "))
people = []
sum_age = 0

for i in range(n):
    name = input("Enter the name : ")
    age = int(input("Enter the age : "))
    people.append((name,age))
    sum_age+=age
print(people)

avg_age = sum_age/n

print("average age :",avg_age)
