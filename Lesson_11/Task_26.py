'''Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
Атрибуты класса:
width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
Методы класса:
__init__(self, width, height=None): Конструктор класса. Принимает ширину и высоту прямоугольника. Если высота не указана (по умолчанию None), то считается, что прямоугольник является квадратом, и высота устанавливается равной ширине.
perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра.
area(self): Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.
__add__(self, other): Магический метод, который определяет операцию сложения (+) для двух прямоугольников. Принимает другой прямоугольник other. Создает новый прямоугольник, который представляет собой объединение исходных прямоугольников по периметру. Возвращает новый прямоугольник.
__sub__(self, other): Магический метод, который определяет операцию вычитания (-) одного прямоугольника из другого. Принимает вычитаемый прямоугольник other. Создает новый прямоугольник, представляющий разницу периметров исходных прямоугольников, и вычисляет высоту на основе этой разницы. Возвращает новый прямоугольник.
__lt__(self, other): Магический метод, который определяет операцию "меньше" (<) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше площади второго, иначе False.
__eq__(self, other): Магический метод, который определяет операцию "равно" (==) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площади равны, иначе False.
__le__(self, other): Магический метод, который определяет операцию "меньше или равно" (<=) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше или равна площади второго, иначе False.
__str__(self): Магический метод, возвращающий строковое представление прямоугольника. Возвращает строку, описывающую ширину и высоту прямоугольника.
__repr__(self): Магический метод, возвращающий строковое представление прямоугольника, которое может быть использовано для создания нового объекта такого же класса с теми же атрибутами.
Пояснение:
Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров исходных прямоугольников, и создает новый прямоугольник.
Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.'''

class Rectangle:
	def __init__(self, width, height=None):
		self.width = width
		if height:
			self.height = height
		else:
			self.height = width

	def perimeter(self):
		return 2 * (self.width + self.height)

	def area(self):
		return self.width * self.height

	def __add__(self, other: "Rectangle"):
		width = self.width + other.width
		sum_per = self.perimeter() + other.perimeter()
		height = sum_per // 2 - width
		return Rectangle(width, height)

	def __sub__(self, other: "Rectangle"):
		if self.perimeter() < other.perimeter():
			self, other = other, self
		width = abs(self.width - other.width)
		sum_per = self.perimeter() - other.perimeter()
		height = sum_per // 2 - width
		return Rectangle(width, height)

	def __eq__(self, other: "Rectangle"):
		return self.area() == other.area()

	def __gt__(self, other: "Rectangle"):
		return self.area() > other.area()

	def __lt__(self, other: "Rectangle"):
		return self.area() < other.area()

	def __le__(self, other):
		return self.area() <= other.area()

	def __str__(self):
		return f"Прямоугольник со сторонами {self.width} и {self.height}"

	def __repr__(self) -> str:
		return f"Rectangle({self.width}, {self.height})"


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))