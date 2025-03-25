#Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.\

numbers = [19, 26, 38, 52, 65, 76, 91, 114, 133, 152, 190, 247]

divisible_numbers = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print("Numbers divisible by 19 or 13:", divisible_numbers)