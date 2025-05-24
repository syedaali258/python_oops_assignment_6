class Product:
    def __init__(self,name, price):
        self.name = name
        self._price = price  #private attribute

#Getter for the price attribute
@property
def price(self):
    return self._price

#setter to update the price attribute
@price.setter
def price(self, value):
    if value < 0:
        print("price cannot be negative!")
    else:
        self._price = value

#deleter to delete the price attribute
@price.deleter
def price(self):
    print(f"deleting the price of {self.name}")
    del self._price

#creating a project object
product = Product("laptop", 1000)

#Accessing the price using the @property
print(product.price)   #0utput 1000

#updating the price using the @price.setter
product.price = 1200
print(product.price)  #output:1200

#Trying to set a negative price
product.price = -500  #output: price cannot be negative

#deleting the price using @price.deleter
del product.price #output:deleting the price of laptop





