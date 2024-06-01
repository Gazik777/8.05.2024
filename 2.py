from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass
    @abstractmethod
    def get_sauce(self):
        pass
    @abstractmethod
    def get_filling(self):
        pass
    @abstractmethod
    def get_additives(self):
        pass

class Spaghetti(Pasta):
    def get_type(self):
        return "Спагетти"
    def get_sauce(self):
        return "Томатный соус"
    def get_filling(self):
        return "Фарш"
    def get_additives(self):
        return ["Пармезан", "Базилик"]

class Fettuccine(Pasta):
    def get_type(self):
        return "Феттучине"
    def get_sauce(self):
        return "Сливочный соус"
    def get_filling(self):
        return "Курица"
    def get_additives(self):
        return ["Грибы", "Петрушка"]

class Penne(Pasta):
    def get_type(self):
        return "Пенне"
    def get_sauce(self):
        return "Соус песто"
    def get_filling(self):
        return "Морепродукты"
    def get_additives(self):
        return ["Чеснок", "Оливковое масло"]

class PastaFactory:
    def create_pasta(self, type):
        if type == "Спагетти":
            return Spaghetti()
        elif type == "Феттучине":
            return Fettuccine()
        elif type == "Пенне":
            return Penne()
        else:
            raise ValueError("Неизвестный тип пасты")

# Пример использования
factory = PastaFactory()
pasta = factory.create_pasta("Спагетти")
print(f"Тип пасты: {pasta.get_type()}")
print(f"Соус: {pasta.get_sauce()}")
print(f"Начинка: {pasta.get_filling()}")
print(f"Добавки: {pasta.get_additives()}")