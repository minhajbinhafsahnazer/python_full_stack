class Shoppingcart:
    def __init__(self):
        self.items = {}

    def add_product(self):
        name = input("Enter the name of product : ")
        price = float(input("Enter the price : "))
        quantity = int(input("Enter the quantity : "))

        if name in self.items:
            self.items[name]["quantity"]+=quantity
        else:
            self.items[name]={ "price": price , "quantity" : quantity }

    def remove_product(self):
        name = input("Enter the name of product to remove : ")
        if name in self.items:
            del self.items[name]
            print(name,"Element deleted \n")
        else:
            print("product not found \n")

cart = Shoppingcart()

while True:
    choice = (input("Enter the Choice Number : \n 1.Add product \n 2.Remove product \n 3. Exit \n Choice : "))
    if choice == "1":
        cart.add_product()
    elif choice == "2":
        cart.remove_product()
    elif choice == "3":
        print("exit")
        break
    else :
        print("invalid choice \n")
    