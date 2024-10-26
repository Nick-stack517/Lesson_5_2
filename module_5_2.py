"""
Домашняя работа по уроку "Специальные методы классов"
Цель: понять как работают базовые магические методы на практике.

Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

"""


class House:
    def __init__(self, name, number_of_floors):
        self.number_of_floors = int(number_of_floors)
        self.name = name

    def go_to(self, new_floor):
        if int(new_floor) < 1 or int(new_floor) > self.number_of_floors:
            print("Такого этажа не существует")

        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        # print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))
