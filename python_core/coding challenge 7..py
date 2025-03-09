#24.Write a Python program that uses list comprehension to create a new list containing the squares of the numbers from 1 to 10.
 
squares = [x**2 for x in range(1, 11)]
print(squares)







#25.Write a Python program that uses a "for" loop to iterate over a string and prints out each character along with its count.


text = "Hello, World!"
for index, char in enumerate(text, start=1):
    print(f"Character {index}: {char}")






#26.Write a Python program that uses a list comprehension to create a new list that contains only the uppercase letters in an existing list of strings.

words = ["Hello", "WORLD", "Python", "PROGRAMMING", "AI"]
uppercase_letters = [char for word in words for char in word if char.isupper()]
print(uppercase_letters)







#27.To write a program in python find the  second smallest and  third largest number in a  list.


#sort then index
def find_numbers(lst):
    # Remove duplicates and sort the list
    sorted_lst = sorted(set(lst))

    # Ensure the list has enough elements
    if len(sorted_lst) < 3:
        return "List doesn't have enough unique elements."

    # Get second smallest and third largest numbers
    second_smallest = sorted_lst[1]
    third_largest = sorted_lst[-3]

    return second_smallest, third_largest

# Example list
numbers = [12, 45, 23, 51, 19, 8, 30, 45, 8]

# Calling the function
result = find_numbers(numbers)

# Printing the result
print(f"Second Smallest: {result[0]}, Third Largest: {result[1]}")














#28.Write a Python program to remove duplicates from a list while preserving the order of elements.


# Given list
numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

# Using a set to track seen elements
seen = set()
unique_list = []

for item in numbers:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)

# Printing the result
print("List after removing duplicates:", unique_list)
