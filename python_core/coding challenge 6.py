#15. Write a program to check Armstrong number.
'''
num = int(input("Enter the number : "))

num_str = str(num)
num_digits = len(num_str)

sum_of_pwr = sum(int(i)**num_digits for i in num_str)

if sum_of_pwr == num:
    print("it is amstrong.")

else:
    print("not amstrong.")

'''

#16. Write a program to check palindrome number.
'''
n = input("enter the number :")

if n == n[::-1]:
    print("palindrome")
else:
    print("not palindrome")




'''

#17. Write a program to print sum of digits.
'''
n1 = int(input("enter the num1 : "))
n2 = int(input("enter the num2 : "))

sum_num = n1 + n2
print(sum_num)



'''

#18.  Print the Fibonacci series for first 12 numbers.

'''
n = int(input("Enter the number : "))
a=0
b=1
for i in range(n):
    print(a,end = " ")
    a, b = b , a+b'''

#19.pattern (1.1)
#*
#**
#***
#****
#*****
#*****
#****
#***
#**
#*
'''
n = 6
for i in range(n):
    for j in range(i):
        print("*",end="")

    print()

for i in range(n):
    for j in range(i,n):
        print("*",end ="")

    print()'''
     
#PATTERN (1.2)
#1
#2 3
#4 5 6
#7 8 9 10
'''
n = 5
num = 1
for i in range(n):
    for j in range(i):
        print(num,end = " ")
        num+=1
    print()

'''

#PATTERN(1.3)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
'''
n = 5
for i in range(n):
    for j in range(n - i - 1):  # Print spaces to align the stars
        print(" ", end="")

    for k in range(i + 1):  # Print left-side stars
        print("*", end=" ")

    print() '''

#PATTERN (1.4)
# 6
# 56
# 456
# 3456
# 23456
# 123456
'''
n=7
for i in range(n):
    num = 6 - 1 * i
    for j in range(i):
        num+=1
        print(num,end="")
    print()
        '''

#20.Write a Program to print the multiplication table.
'''
n = int(input("Enter the multiplication table level : "))
for i in range(n):
    print("Multiplication table of ",i)
    for j in range(0,10):
        print(j ,"x", i , "=" ,i*j)
        j+=1
    print()
    '''

#21. How to find the factorial of number 5.
 
 #iteration method
'''
n = int(input("Enter the number to find the factorial : "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(f"Factorial of {n} :{fact}")

'''
#22. Write a Program to Check Whether a Number is Prime or Not.
'''
n = int(input("Enter the number to check if prime : "))
flag = 0
if n==0 or n==1:
        print("not prime")
if n>0:
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0:
            flag = 1
    if flag == 1:
        print("not prime")
    else :
        print("prime")

'''



#23. pattern
# 13579
# 3579
# 579
# 79
# 9
n = 5
for i in range(n):
    num = 1 + 2 * i
    for j in range(i,n):
        print(num,end = "")
        num+=2
    print()
    
