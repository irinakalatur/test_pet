class Pet:
    '''Инициализация переменных
        name: имя питомца
        color: цвет питомца
        age: возраст питомца
    '''
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        
    ''' Вывод информации о питомце'''
    def cat(self):
        print(f"Кот {self.name}, цвет {self.color}, возраст {self.age}")


class Cat(Pet):
    '''Метод для вывода информации об игре с питомцем'''
    def play(self):
        print(f"Кот {self.name} играет дразнилкой")

    '''Метод для вывода информации о сытости питомца
        satiety: сытость (True/False)
    '''
    def eating(self,satiety):
        self.satiety = satiety
        if satiety == False:
            print(f"{self.name} не голоден")
        else:
            print(f"{self.name} ест сосиску")



simon = Cat("Саймон", "серый", 2)
simon.cat()
simon.play()
simon.eating(True)
simon.eating(False)