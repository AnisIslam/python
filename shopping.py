class Shopper:
    def __init__(self, name):
        self.name  = name
        self.cart = []
    
    def add_to_cart (self , item, price, quantity):
        self.cart.append({'name': item, 'price':price, 'quantity': quantity })

    def checkout (self, amount):
        # print(self.cart)
        price = 0
        for item in self.cart:
            print(item)
            price = price + item['price'] * item['quantity']
        # print(price)
        if amount< price:
            return f'Please give me more {price - amount} taka'


shopping = Shopper('Bag')
shopping.add_to_cart('shirt', 400, 3)
shopping.add_to_cart('pant', 300, 12)
shopping.add_to_cart('show', 700, 4)

reply = shopping.checkout(9000)
print (reply)