#42
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = (list1,key = lambda x : x**2)
print(square)
cube = (list1,key = lambda x : x**3)
print(cube)

--------------------------------------------------
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda and map() to calculate squares and cubes
square = list(map(lambda x: x**2, list1))
cube = list(map(lambda x: x**3, list1))

print("Squared List:", square)
print("Cubed List:", cube)
