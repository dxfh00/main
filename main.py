from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (self.name, self.weight, self.category)


class Shop(Product):
    __file_name = 'products.txt'
    def __init__(self):
        Product.__init__(self)

    def get_products(self, file):
        self.file = file
        self.file = open(__file_name, 'r')
        self.file.close()
        return self.file

    def add(self, *products):
        self.products = products
        self.file = open(__file_name, 'w')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
