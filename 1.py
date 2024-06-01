
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    def __str__(self):
        return f"Пользователь: {self.first_name} {self.last_name}, Возраст: {self.age}, Email: {self.email}"

class UserBuilder:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.email = None

    def with_first_name(self, first_name):
        self.first_name = first_name
        return self

    def with_last_name(self, last_name):
        self.last_name = last_name
        return self

    def with_age(self, age):
        self.age = age
        return self

    def with_email(self, email):
        self.email = email
        return self

    def build(self):
        return User(self.first_name, self.last_name, self.age, self.email)

user = UserBuilder() \
    .with_first_name("Иван") \
    .with_last_name("Иванов") \
    .with_age(30) \
    .with_email("ivanov@mail.com") \
    .build()

print(user)