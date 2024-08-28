
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

lion = Predator("Лев")
deer = Mammal("Олень")
rose = Flower("Роза")
apple = Fruit("Яблоко")

# Примеры действий
lion.eat(rose)
print(f"Лев жив: {lion.alive}, накормлен: {lion.fed}")

deer.eat(apple)  # Олень съест Яблоко
print(f"Олень жив: {deer.alive}, накормлен: {deer.fed}")

deer.eat(rose)   # Олень не станет есть Розу
print(f"Олень жив: {deer.alive}, накормлен: {deer.fed}")