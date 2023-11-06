# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import logging

logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def log_dec(func):
	def wrapper(*args):
		try:
			return func(*args)
		except Exception as e:
			logger.error(f'Ошибка {e} в функции {func.__name__} при аргументах {args}')
		return None

	return wrapper



class Person:

	@log_dec
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

	def __str__(self):
		return f'{self.lastname} {self.firstname} {self.patronymic} {self.age}лет'

	def get_age(self):
		return self.age


class Employee(Person):

	@log_dec
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

person = Person(1, 'dfh', "Doe", 30)
print(person)

def par():
	parser = argparse.ArgumentParser(description='Добавление сотрудника')
	parser.add_argument('-lastname', type=str, help='Фамилия')
	parser.add_argument('-firstname', type=str, help='Имя')
	parser.add_argument('-patronymic', type=str, help='Отчество')
	parser.add_argument('-age', type=int, help='Возраст')
	args = parser.parse_args()
	return Person(args.lastname, args.firstname, args.patronymic, args.age)

print(par())