#a = None
#print(type(a)) #null is a builtin datatype


#if ():
# print
#else
# print 

'''mark = int(input("enter a number :"))
if mark >= 0:
    if mark == 0 :
        print("zero value")
    else :
        print("positive number")
else : 
    print("negative number")'''

#while loops
'''i=1
Ni = "i love u 💕💕💕"
while i<=101:
    print(Ni, end=',')
    i+=1'''

#while loop
'''mylist= [23,33,44,32,56,23]

i=0
sum=0
while i<len(mylist):
    sum+=mylist[i]
    i+=1
print(sum)'''


#printing patterns

'''n = 6 
i = 1
while i<=6:
    j=1
    while j<=i:
        print('*',end = ' ')
        j+=1
    print()
    i+=1'''


'''n = 6
i=1
while i<=n:
    j=1
    while j<=i:
        print('+',end=' ')
        j+=1
    print()
    i+=1'''


#printing reverse pattern
'''*****
    ****
     ***
      **
       *'''

'''n = 6
i=1
while i<=n:
    j=1
    while j<i:
        print(' ', end=' ')
        j+=1

    while j<=n:
        print("*",end=" ")
        j+=1 
    print()  #next line go
    i+=1'''



#for loops
'''syntax
for i in var'''

'''lang = ['py','react','java','php']

for i in lang:
    print(i)'''


'''string = ('python')
for i in string:#prints all char one by one
    print(i)'''


#doubling the elements in list
'''my_list = [1,2,3,4,5,6]

for i in my_list: #for doesnt req to incr like i+=1
    print(i*2)'''


#range 

'''for i in range(10,100,10):   #iterate from 1 to 10 incrementing ,last 10 is diffrence
    print(i,end=' ')'''


#printing multiplication table of 2

'''num= 2
for i in range(11):
    print(i,'x',num,'=',i*num)'''

#print multiplication table from 1 to 10 all(using of nested for)

'''for i in range(1,11):
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
    print()  #FOR SPACING'''



#num pattern usinf for loop nesting
'''
1
12
123
1234
12345'''

'''n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

'''n=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')  # i kal mathram print aavum repeat
    print()
'''

#reverse pattern
''''n=10
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()'''

'''n=10
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

#A
#A B
#A B C
#A B C D

'''n=5
for i in range(n):
    for j in range(i+1):
        print(chr(j+65),end = ' ')
    print()'''

##jump statments ; to control loop

#break
'''syntax'''

#condition :
#   break



'''eg

for i in range(10,100,10):
    if i == 50:
        break 
    print(i)
    


my_list = [23,23,45,65,4,22,54]
sum=0
for i in my_list:
    sum+=i
    if sum > 1000:
        break
    print(sum)
    

  #continue  

  #eg pgm to print num  skipping even numbers
for i in range(1,10):
    if i%2 == 0:
        continue   #to skip a particular condition completely
    print(i)
     
'''

'''
#jump sttmt : pass
for i in range(10):
    
    pass'''

'''a=100
b=20
if a>b :
    pass
else:
    print("hi")'''

#accessing dictionaries using loops
'''dictionary = {'git':'bash','set':'lone','step':'india'}
for i in dictionary :
    print(i)

dictionary = {'git':'bash','set':'lone','step':'india'}
for i in dictionary.keys() :
    print(i)


dictionary = {'git':'bash','set':'lone','step':'india'}
for i in dictionary.values() :
    print(i)    '''           #to get values

'''dictionary = {'git':'bash','set':'lone','step':'india'}
for i in dictionary :
    print(dictionary[i])   #another way to get values

dictionary = {'git':'bash','set':'lone','step':'india'}
for i,j in dictionary.items() :
    print(i,j)                 #to get both key value pair'''



#list comprehesion
'''lang = ['python','react','php','go']

new_list=[]

for i in lang:
    if 'p' in i:
        new_list.append(i)
print(new_list)              '''    #not using list comprehension\


#using comprehension method
'''lang = ['python','react','php','go']
new_list=[]

new_list = [i for i in lang if 'p' in i]
print(new_list)
'''

# another example for comprehension
'''
even=[i for i in range(1,101) if i%2==0]
print(even)

'''







