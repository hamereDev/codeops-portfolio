# Exercise 1: Book Class

class Book:
    # Constructor to initialize book information
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method to display book information
    def describe(self):
        print(f'"{self.title}" by {self.author} has {self.pages} pages.')


book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Learning Python", "Mark Lutz", 1648)

book1.describe()
book2.describe()

print()

# Exercise 2-5: Product Class

class Product:
    # Constructor to initialize product information
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    # Getter for the private quantity attribute
    @property
    def quantity(self):
        return self.__quantity

    # Setter with validation
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    # Increase the quantity
    def restock(self, n):
        if n > 0:
            self.__quantity += n

    # Decrease the quantity if enough stock exists
    def sell(self, n):
        if n <= 0:
            raise ValueError("Quantity must be positive.")
        if n > self.__quantity:
            raise ValueError("Not enough stock.")
        self.__quantity -= n

    # Display product information
    def display(self):
        print(f"{self.name} Price: {self.price} ETB Quantity: {self.quantity}")


product1 = Product("Shoes", 3500, 15)
product2 = Product("Skirt", 1800, 20)
product3 = Product("Jacket", 4500, 10)

product1.restock(5)
product1.sell(3)

product1.display()
product2.display()
product3.display()