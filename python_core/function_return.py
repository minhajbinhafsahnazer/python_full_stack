#function

#synx
#fuction define 
'''def function_name():    
    print/return stttm '''

 #fuction call
'''function_name()''' 


#eg 
'''
def my_function():
    print('this is my first fuction')
my_function()


def my_function(a,b):   #parameter(the variables listed inside the fuction defenition)
    print(a+b)
my_function(5,7)   #argument pased(sent when call)

'''
'''
def my_function(a,b,c):   #parameter(the variables listed inside the fuction defenition)
    print(a+b+c)
my_function(5,7,5)   #argument pased(sent when call)
my_function(5,5,5)
my_function(7,7,7)
'''

'''
def my_function(a,b,c=None):  #parameter(the variables listed inside the fuction defenition)
   if c is not None:
       print(a+b+c)
   else:
       print(a+b)                     
my_function(5,7)   #argument pased(sent when call)
my_function(5,5,5)
my_function(7,7,7)


'''
#arbitary argument
'''

def fun(*sum):
    total = 0
    for i in sum:
        total+=i
    print(total)
fun(3,4,5,6,8)
fun(32,45,52,64,83)'''

#return
'''
def my_function():
   print('hello worldddd')

   return 5,7  #statically prints that
print(my_function())   
'''
#sqr of a number
'''
def square(num):
   return num*num
x=int(input('enter a number'))
print(square(x))
'''

#integeneous methodd
'''
def square(num):
   s=num*num
   return s
x=int(input('enter a number'))
print(square(x)) '''


#lists into a function
def fun(lang):
    for i in lang:
        print(i)

lang = ['react','java']
fun(lang)