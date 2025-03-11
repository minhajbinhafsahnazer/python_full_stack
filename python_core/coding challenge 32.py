#32
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def Get_Book_info(self):
        print("The details of the book :")
        print(f"Title :{self.title}\nAuthor : {self.author}\nyear : {self.year}")
new_book = Book("sunshine","john doe","1991")
new_book.Get_Book_info()
