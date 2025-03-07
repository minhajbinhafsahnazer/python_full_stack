#13.Write a Python function that takes a dictionary of items and their prices as input and 
# finds and prints the keys (items) with the highest prices
'''
def fun():
     items = {}
     n=int(input("Enter the num of items : "))
     for i in range(n):
        item =input("enter name : ")
        price =input("enter price : ")
        items[item] = price

     max_price = max(items.values())
     highest_priced_item = []
     for item,price in items.items():
         if price == max_price:
             highest_priced_item.append(item)
     print("highest priced item :",highest_priced_item)

fun()
'''
#14. Convert two lists into a dictionary in Python without using a built-in method


list1 = input("Enter the first list (seperated by comma) : ").split(',')
list2 = input("Enter the second list (seperated by comma) : ").split(',')

dictionary = {}
for i in range(min(len(list1), len(list2))): #min ensures to run only upto length of shortest list
    dictionary[list1[i].strip()] = list2[i].strip()  #strip strips out elements btw delimeter

print(dictionary)

