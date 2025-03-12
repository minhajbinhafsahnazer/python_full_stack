#29. Create a simple calculator operations  using function.
'''
num1 = int(input("Enter the Number 1 : "))
operator = input("select calculation (+,-,*,/) : ")
num2 = int(input("Enter the Number 2 : "))
if operator == '+':
    print(num1+num2)
if operator == '-':
    print(num1-num2)
if operator == '*':
    print(num1*num2)
if operator == '/':
    print(num1/num2)


'''


#30. Create a Python function that takes a string as input and counts the number of vowels and consonants in the string.
vowels = 0
consonents = 0
string1 = input("Enter the string : ")
vow = ("A","E","I","O","U","a","e","i","o","u")
for i in string1:
    if i.isalpha():
        if i in vow:
            vowels+=1
        else:
            consonents+=1
print("Num of vowels =",vowels)
print("Num of consonents =",consonents)


