# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# # Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:
# # Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# # Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины
# рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# # Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса.
# # Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного
# типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
# # animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal'). *args - переменное количество аргументов,
# представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости
# от типа животного. Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.



class Animal:
	def __init__(self, name):
		self.name = name


class Bird(Animal):
	def __init__(self, name, wingspan):
		super().__init__(name)
		self.wingspan = wingspan

	def wing_length(self):
		return self.wingspan / 2


class Fish(Animal):
	def __init__(self, name, max_depth):
		super().__init__(name)
		self.max_depth = max_depth

	def depth(self):
		if self.max_depth < 10:
			return 'Мелководная рыба'
		elif self.max_depth > 100:
			return 'Глубоководная рыба'
		return 'Средневодная рыба'


class Mammal(Animal):
	def __init__(self, name, weight):
		super().__init__(name)
		self.weight = weight

	def category(self):
		if self.weight < 100:
			return "Малявка"
		if self.weight > 1000:
			return "Гигант"
		return "Обычный"

class AnimalFactory:
	def create_animal(self, animal_type, *args):
		if animal_type == "Bird":
			return Bird(*args)
		elif animal_type == 'Fish':
			return Fish(*args)
		elif animal_type == 'Mammal':
			return Mammal(*args)
		else:
			return ValueError ("Недопустимый тип животного")


factory = AnimalFactory()
# Создание экземпляров животных
animal1 = factory.create_animal("Bird", 'Орел', 200)
animal2 = factory.create_animal('Fish', 'Лосось', 50)
animal3 = factory.create_animal('Mammal', 'Слон', 5000)
animal4 = factory.create_animal('Mamma', 'Слон', 5000)

# Вывод результатов
print(animal1)
print(animal2)
print(animal3)
print(animal4)
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())
