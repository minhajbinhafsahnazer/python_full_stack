#42

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda and map() to calculate squares and cubes
square = list(map(lambda x: x**2, list1)) #key not used in map fn
cube = list(map(lambda x: x**3, list1))

print("Squared List:", square) 
print("Cubed List:", cube)
