from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def get_products(self):
        __file_name = 'products.txt'
        file = open(__file_name, 'r')
        print(file.read())
        file.close()

    def add(self, *products):
        list_products = ''
        __file_name = 'products.txt'
        self.products = products
        file = open(__file_name, 'a')
        for i in self.products:
            list_products += str(i) + ' ' '\n'
        file.write(list_products)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
