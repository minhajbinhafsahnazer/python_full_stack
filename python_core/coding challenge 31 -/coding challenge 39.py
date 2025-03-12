#39. Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals.
class Numbers:
    def __init__(self):
        self.dig = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.dig > 10:
            raise StopIteration
        current = self.dig
        self.dig += 0.5
        return current

num = Numbers()
for i in num:
    print(i)