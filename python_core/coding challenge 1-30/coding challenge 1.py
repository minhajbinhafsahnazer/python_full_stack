#coding challenge 1.1

#Number of Vowels and consonants in a string
'''
vowels = {'A','E','I','O','U','a','e','i','o','u'}
v = 0
c = 0

lang=input("Enter the String : ")
for i in lang:
    if i in vowels:
        v+=1
    else:
        c+=1
print("No of vowels :", v)
print("No of consonants :",c)
'''

#coding challenge 1.2

# Write Program to given string is a palindrome (reads the same forwards and backwards).
'''
lang = input("Enter the string to check palindrome : ")
lang_rev = lang[::-1]
if lang == lang_rev:
    print("The given string is palindrome")
else:
     print("Not palindrome")
'''

#coding challenge 1.3
# Write a program to remove duplicate values in the given string.

string = input("Enter The String : ")

unique_char = set()  #to store uniq
read = ""   #to store loaded string

for i in string :
    if i not in unique_char:
        unique_char.add(i)
        read+=i
print("string after removing duplicates : ",read)

