# Магические методы  —  это специальные методы в python, обрамленные двумя нижними
# подчеркиваниями. Они также известны как dunder методы. Многое из того, что мы делаем
# в Python, делается с использованием dunder методов. Посмотрите на примеры ниже:

x = 5
print(x + 3)  # 8
print(x.__add__(3))  # 8

animals = ['cat', 'dog', 'cow', 'horse']
print(animals[2])  # 'cow'
print(animals.__getitem__(2))  # 'cow'

# Мы внедрим эти методы в наши классы, чтобы сделать их интуитивно понятными.
# Давайте разбираться как.


# 1. __init__()
# метод init используется в качестве конструктора для классов в Python.
class Student():
    def __init__(self, id, name):
        self.id, self.name = id, name

s = Student(1, 'Dipam')
print(s)  # <__main__.Student object at 0x7fe1e7f49f70>


# 2. __str__()
# При создании объектов классов очень хотелось бы видеть, что у них внутри, в легко читаемом
# для человека представлении. И здесь пригождается str:
class Student2():
    def __init__(self, id, name):
        self.id, self.name = id, name

    def __str__(self):
        return f"Student {self.name} with id {self.id}"

s = Student2(1, 'Dipam')
print(s)  # Student Dipam with id 1


# Существует другой метод — __repr__() — который используется для возврата состояния
# объекта как он есть, но в данной статье мы пропустим этот метод.


# 3. __len__()
# Теперь, предположим, у нас есть класс School, который хранит детальную информацию о
# студентах. И вот простой способ посчитать количество студентов в School.
class School():
    def __init__(self, students, grades):
        self.students, self.grades = students, grades

    def __len__(self):
        return len(self.grades)

students = [Student2(1, 'Dipam'), Student2(2, 'Darshan'), Student2(3, 'Dhaval')]
grades = ['F', 'A-', 'B+']
sc = School(students, grades)
print(len(sc))  # 3


# 4. __getitem__()
# Нам также нужен простой способ получить доступ к записям о конкретном студенте:
# 5. __setitem__()
# …и возможность редактировать их.
class School2():
    def __init__(self, students, grades):
        self.students, self.grades = students, grades

    def __getitem__(self, i):
        return self.students[i].name, self.grades[i]

    def __setitem__(self, i, g):
        self.grades[i] = g

students = [Student2(1, 'Dipam'), Student2(2, 'Darshan'), Student2(3, 'Dhaval')]
grades = ['F', 'A-', 'B+']
sc = School2(students, grades)
print(sc[0])  # ('Dipam', 'F')
sc[0] = 'A'
print(sc[0])  # ('Dipam', 'A')


# 6. __getattr__() and __setattr__()
# Эти методы доступны в Python автоматически при создании класса, чтобы получать и
# задавать его атрибуты, следовательно нам не нужно их определять.
# Однако мы можем сделать это, если захотим изменить их поведение.
# Например, можно изменить поведение __setattr__() для сохранения атрибута в списке,
# когда бы он ни был задан, чтобы легко получить доступ ко всем атрибутам.
class School3():
    def __init__(self, students, grades):
        self._all_attr = {}
        self.students, self.grades = students, grades

    def __setattr__(self, k, v):
        if not k.startswith('_'): self._all_attr[k] = v
        super().__setattr__(k, v)

    def print_all(self):
        for atr, val in self._all_attr.items(): print(f"atr={atr}, val={val}")

students = [Student2(1, 'Dipam'), Student2(2, 'Darshan'), Student2(3, 'Dhaval')]
grades = ['F', 'A-', 'B+']
sc = School3(students, grades)
sc.print_all()  #
# atr=students, val=[<__main__.Student2 object at 0x7f0eb6c4ba00>, <__main__.Student2 object at 0x7f0eb6c4bc70>, <__main__.Student2 object at 0x7f0eb6c4baf0>]
# atr=grades, val=['F', 'A-', 'B+']
# Если закоментировать def __setattr__(), то две строки выше выводиться не будут

# 7. __iter__()
# Мы можем создать итератор, используя метод __iter__(). Затем мы можем использовать его
# для доступа к данным каждого студента.
class School4():
    def __init__(self, students, grades):
        self.students, self.grades = students, grades

    def __iter__(self):
        for i in range(0, len(self.grades)): yield self.students[i].name, self.grades[i]

students = [Student2(1, 'Dipam'), Student2(2, 'Darshan'), Student2(3, 'Dhaval')]
grades = ['F', 'A-', 'B+']
sc = School4(students, grades)
next(iter(sc))
print(sc)  # <__main__.School4 object at 0x7f28950d7880>
for s, g in iter(sc):
    print(f's={s}  g={g}')
# s=Dipam  g=F
# s=Darshan  g=A-
# s=Dhaval  g=B+

# 8. __add__() и другие математические методы
# Предположим, у нас есть класс Cost.
# Имеет смысл осуществлять математические операции с этими объектами — это сделает
# наш код интуитивно понятнее и элегантнее.
class Cost():
    def __init__(self, symbol, value):
        self.symbol, self.value = symbol, value

    def __add__(self, other):
        return self.value + other.value

pizza = Cost('$', 100)
burger = Cost('$', 50)
print(f'pizza + burger = {pizza + burger}')  # pizza + burger = 150