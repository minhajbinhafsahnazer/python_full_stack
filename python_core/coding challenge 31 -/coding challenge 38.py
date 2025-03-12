class AlphabetIterator:
    def __init__(self):
        self.current = ord('A')

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > ord('Z'):
            raise StopIteration
        letter = chr(self.current)
        self.current+=1
        return letter
    
for letter in AlphabetIterator():
    print(letter,end = " ")