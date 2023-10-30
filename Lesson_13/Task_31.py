'''В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.'''

class Person:

	def __init__(self, lastname, firstname, patronymic, age):
		if not isinstance(lastname, str) or len(lastname.strip()) == 0:
			raise InvalidTextError(lastname)
		if not isinstance(firstname, str) or len(firstname.strip()) == 0:
			raise InvalidTextError(firstname)
		if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
			raise InvalidTextError(patronymic)
		self.firstname = firstname
		self.lastname = lastname
		self.patronymic = patronymic
		if not isinstance(age, int) or age < 1:
			raise InvalidAgeError(age)
		self.age = age

	def birthday(self):
		self.age += 1

	def full_name(self):
		return f'{self.lastname} {self.firstname} {self.patronymic}'

	def get_age(self):
		return self.age

class Employee(Person):

	def __init__(self, lastname, firstname, patronymic, age, id):
		super().__init__(lastname, firstname, patronymic, age)
		if not isinstance(id, int) or id < 100_000 or id > 999_999:
			raise InvalidIdError(id)
		self.id = id

	def get_level(self):
		res = sum(num for num in str(self.id))
		return res%7

class InvalidTextError(ValueError):
	def __init__(self, text):
		self.text = text

	def __str__(self):
		return f'Invalid text: {self.text}. Text should be a non-empty string.'


class InvalidAgeError(ValueError):
	def __init__(self, age):
		self.age = age

	def __str__(self):
		return f'Invalid age: {self.age}. Age should be a positive integer.'

class InvalidIdError(ValueError):
	def __init__(self, id):
		self.id = id

	def __str__(self):
		return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'

person = Person("hjk", 2, "Doe", 30)
print(person)
