'''На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из
list1 со списком выпавших чисел list2'''


class LotteryGame:
	def __init__(self, list1, list2):
		self.list1 = list1
		self.list2 = list2
	def compare_lists(self):
		repeated_elements = []
		for item in self.list1:
			if item in self.list2:
				repeated_elements.append(item)
		if len(repeated_elements) == 0:
			return print("Совпадающих чисел нет.")
		else:
			return print(f'Совпадающие числа: {repeated_elements}\nКоличество совпадающих чисел: {len(repeated_elements)}')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

