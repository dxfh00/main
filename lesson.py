class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        min_floors = 0
        if new_floor <= min_floors or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            while min_floors < new_floor:
                min_floors += 1
                print(min_floors)

    def __str__(self):
        return (f"Название: {self.name}: {self.number_of_floors}")

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
# h1.go_to(5)
# h2.go_to(10)

print(h1)
print(h2)
# print(len(h1))
# print(len(h2))

print(h1 == h2)
h1 = h1 + 10
print(h1)
# print(h1 == h2)

# print(h1 > h2)
# print(h1 >= h2)
# print(h1 < h2)
# print(h1 <= h2)
# print(h1 != h2)
