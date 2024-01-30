import os
import csv
import pytest

class Exists_grade(Exception):
    pass

class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name (str): ФИО студента
    - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
    - __init__(self, name, subjects_file): конструктор класса
    - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
    - __getattr__(self, name): получение значения атрибута
    - __str__(self): возвращает строковое представление студента
    - load_subjects(self, subjects_file): загрузка предметов из файла CSV
    - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
    - get_average_grade(self): возвращает средний балл по всем предметам
    - add_grade(self, subject, grade): добавление оценки по предмету
    - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)


    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        if not os.path.exists(subjects_file): # Создаётся файл, если он не существует
            open(subjects_file, 'w')
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f) # Файл читается
            for row in reader: # берёт ряды
                subject = row[0] # из нулвего ряда берём Предметы
                print(subject)
                if subject not in self.subjects: # Создаём предмет, если он не существует
                    self.subjects[subject] = {'grades': [], 'test_scores': []} # Создаётся предмет, с словарём внутри

    def add_grade(self, subject, grade): # Добавляем оценку, к указанному предмету
        if subject not in self.subjects: # Если нет предмета, то создаём. Иначе ошибка, предмет уже существует
            self.subjects[subject] = {'grades': [], 'test_scores': []} # Создаётся предмет, с словарём внутри
        else:
            raise Exists_grade(f"Этот предмет {subject} уже существует")
        if not isinstance(grade, int) or grade < 2 or grade > 5: # Оценка должа быть в диапазоне от 2-5. Иначе ошибка.
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade) # Добавляем оценку в выбранному предмету. ["grades"] = оценка

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)


    # def save_subjects(self, subjects_file = "subjects.csv"):
    #     print(end="\n"*4)
    #     with open(subjects_file, 'w') as csvfile:
    #         spamwriter = csv.writer(csvfile, delimiter=' ',
    #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #         spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])




student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

# student.save_subjects()

# print(end="\n"*4)
# print(student.__str__())
# print(end="\n"*2)
# print({student.name:{"Предметы":student.subjects}})
#
# {'Иван Иванов': {'Предметы': {'Математика': {'grades': [4], 'test_scores': [85]}, 'История': {'grades': [5], 'test_scores': [92]}}}}



def test_get_average_test_score_alg():
    assert student.get_average_test_score("Алгебра") == "ValueError: Предмет Алгебра не найден", "Предмет не найден"

def test_add_grade_history():
    assert student.add_grade("История", 5) == "Exists_grade: Этот предмет История уже существует", "Предмет уже существует"

def test_add_grade_history_grade():
    assert student.add_grade("История", 8) == "Exists_grade: Этот предмет История уже существует", "Предмет уже существует"

def test_add_grade_history_lit():
    assert student.add_grade("Литература", 8) == "ValueError: Оценка должна быть целым числом от 2 до 5", "Число вне 2-5 значения"

def test_add_test_score_physics_chemistry():
    assert student.add_test_score("физика","химия") == "ValueError: Результат теста должен быть целым числом от 0 до 100", "Значение должно быть целым числом"

if __name__ == "__main__":
    r"""
Запускал с pytest.main()
Результат:

============================= test session starts =============================
platform win32 -- Python 3.10.6, pytest-8.0.0, pluggy-1.4.0
rootdir: D:\Погружение в Python (семинары)\Zadanie15
collected 0 items
============================ no tests ran in 0.00s ============================

Формат csv, мне понятен. Но не понял как составить данные об предметах с ученика.
Можно было сделать так.
Id;Name;Subname;{Items{grade:average_grade}}
Может Id лишнее.
Name;Subname;{Items{grade:average_grade}}
Или сократить до двух ячеек.
Name Subname;{subjects{grade:average_grade}}
    """
    pytest.main() # Он не работает.

    # student.add_test_score("физика",50)
    # average_grade = student.get_average_grade()
    # print(f"Средний балл: {average_grade}")

    # student.add_grade("История", 5)
    # average_grade = student.get_average_grade()
    # print(f"Средний балл: {average_grade}")

