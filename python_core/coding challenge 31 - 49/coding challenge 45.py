# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function

numbers = [10, -5, 20, -15, 30, -25, 40, -35]

positive_sum = sum(filter(lambda x: x > 0, numbers))
negative_sum = sum(filter(lambda x: x < 0, numbers))

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)