import copy
class PastaPrototype:
    def __init__(self, type, sauce, filling, additives):
        self.type = type
        self.sauce = sauce
        self.filling = filling
        self.additives = additives
    def clone(self):
        return copy.deepcopy(self)

original_pasta = PastaPrototype("Спагетти", "Томатный соус", "Фарш", ["Пармезан", "Базилик"])

cloned_pasta = original_pasta.clone()

print(f"Оригинальная паста: {original_pasta.type}, {original_pasta.sauce}, {original_pasta.filling}, {original_pasta.additives}")
print(f"Клонированная паста: {cloned_pasta.type}, {cloned_pasta.sauce}, {cloned_pasta.filling}, {cloned_pasta.additives}")
print(f"Оригинал и клон - это один и тот же объект? {'Да' if original_pasta is cloned_pasta else 'Нет'}")
