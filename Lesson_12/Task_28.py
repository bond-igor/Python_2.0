'''Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует условию, выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
Предмет {Название предмета} не найден
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:
Оценка должна быть целым числом от 2 до 5
Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
Атрибуты класса:
name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.
Магические методы (Dunder-методы):
__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.
__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История
Методы класса:
load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.
add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.
add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.
get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
get_average_grade(self): Возвращает средний балл по всем предметам.'''


import csv

class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и содержать только буквы.")
        setattr(instance, self._name, value)

# Основной класс
class Student:
    first_name = NameDescriptor()
    middle_name = NameDescriptor()
    last_name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

        # Загрузка предметов из CSV файла
    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if score < 0 or score > 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.subjects[subject]["test_scores"].append(score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        scores = self.subjects[subject]["test_scores"]
        return sum(scores) / len(scores) if scores else 0

    def get_average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return sum(total_grades) / len(total_grades) if total_grades else 0

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)