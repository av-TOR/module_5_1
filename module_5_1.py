class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor > 1:
            print(f"Номер этажа {new_floor}")
        else:
            print("Такого этажа не существует")


Home1 = House('Дом', 1)
Home2 = House('Высотка', 13)
Home1.go_to(0)
Home2.go_to(5)
Home1.go_to(2)
Home2.go_to(6)