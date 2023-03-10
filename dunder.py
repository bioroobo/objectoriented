"""
смотри главы 13.5 13.6 Прохоренок Python3 PyQt
"""

# Магические методы — это специальные методы в python, обрамленные двумя нижними
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
class Student1():
    def __init__(self, id, name):
        self.id, self.name = id, name

s = Student1(1, 'Dipam')
print(s)  # <__main__.Student object at 0x7fe1e7f49f70>


# 2. __str__()
# При создании объектов классов очень хотелось бы видеть, что у них внутри,
# в легко читаемом для человека представлении. И здесь пригождается str:
class Student2():
    def __init__(self, id, name):
        self.id, self.name = id, name

    def __str__(self):
        return f"Student {self.name} with id {self.id}"

s = Student2(1, 'Dipam')
print(s)  # Student Dipam with id 1


# 3. __len__()
# Теперь, предположим, у нас есть класс School, который хранит детальную информацию о
# студентах. И вот простой способ посчитать количество студентов в School.
class School1():
    def __init__(self, students, grades):
        self.students, self.grades = students, grades

    def __len__(self):
        return len(self.grades)

students = [Student2(1, 'Dipam'), Student2(2, 'Darshan'), Student2(3, 'Dhaval')]
grades = ['F', 'A-', 'B+']
sc = School1(students, grades)
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


print('\n-------dunder methods: __new__() __init__() ------)----')
# 1. __new__() __init__()
class Product1:
    def __new__(cls, *args):
        new_product = object.__new__(cls)
        print("Product1 __new__ gets called")
        return new_product

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("Product1 __init__ gets called")

product = Product1("Vacuum", 150.0)
# will print:
# Product __new__ gets called
# Product __init__ gets called


print('\n------- dunder methods: __repr__() __str()__ ----------')
# 2. __repr__()
# используется для возврата состояния объекта как он есть.
# Метод __repr__ должен возвращать строку, показывающую, как может быть создан экземпляр.
# Эта строка может быть передана в eval() для повторного создания экземпляра.
class Product2:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product2({self.name!r}, {self.price!r})"

    def __str__(self):
        return f"Product2: {self.name}, ${self.price:.2f}"

product2 = Product2("Vacuum2", 1500.0)
print(f'type(product2): {type(product2)}')
print(f'repr(product2): {repr(product2)}')
evaluated = eval(repr(product2))
print(f'type(evaluated): {type(evaluated)}')
product3 = Product2("Vacuum3", 100.0)
print(f'method __str__(): {product3}')


print('\n------- dunder methods: __iter__()  __next__()  -------')
# 7. Итерация: __iter__ and __next__ 
# С помощью кода мы можем автоматизировать одну из ключевых операций, а именно повторение
# некоторого действия, реализация которого подразумевает использование цикла for,
# выступающего в роли логического процесса. Речь идет об итерируемом объекте, который
# можно использовать в этом цикле. Ниже представлена самая простая форма цикла for:
# for item in iterable:
#     # Далее следуют нужные операции 
# Согласно внутренней логике итерируемый объект преобразуется в итератор, который показывает
# элементы этого объекта при выполнении каждого цикла. В целом, итераторы — это объекты
# Python, которые предоставляют элементы для перебора. Преобразование же осуществляется
# магическим методом __iter__. Кроме того, извлечение следующего элемента итератора
# подразумевает реализацию еще одного магического метода __next__. Вернемся к предыдущему
# примеру и обеспечим работу нашего класса Product в качестве итератора в цикле for:
# Как показано ниже, создается список из объекта, содержащего free_samples (бесплатные
# образцы) в методе __iter__, который образует итератор для экземпляра пользовательского
# класса. Чтобы произвести итерацию, мы реализуем метод __next__, предоставляя объект из
# списка free_samples. Перебор элементов завершается в тот момент,
# когда заканчиваются free_samples.
class Product4:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, ${self.price:.2f}"

    def __iter__(self):
        self._free_samples = [Product4(self.name, 0) for _ in range(3)]
        print("Iterator of the product is created.")
        return self

    def __next__(self):
        if self._free_samples:
            return self._free_samples.pop()
        else:
            raise StopIteration("All free samples have been dispensed.")
 
product = Product4("Perfume", 5.0)
for i, sample in enumerate(product, 1):
    print(f"Dispense the next sample #{i}: {sample}")
# will print:
# Iterator of the product is created.
# Dispense the next sample #1: Product: Perfume, $0.00
# Dispense the next sample #2: Product: Perfume, $0.00
# Dispense the next sample #3: Product: Perfume, $0.0


print('\n------- dunder methods: __enter__()  __exit__()  -------')
# 9. Контекстный менеджер: __enter__ and __exit__ 
#Работая с файловыми объектами Python, вы, возможно, не раз наталкивались на такой
# распространенный синтаксис:
# with open('filename.txt') as file:
#     # Далее следуют ваши операции с файлом
# Инструкция with является методом контекстного менеджера. В вышеприведенном примере она
# создает контекстный менеджер для файлового объекта, который по завершении нужных операций
# будет закрыт этим же менеджером, что снова сделает его доступным для других процессов.
# В целом, контекстные менеджеры — это объекты Python, которые управляют совместно
# используемыми ресурсами, например открывают и закрывают за нас файлы. Не будь их, нам бы
# пришлось управлять ими вручную, что, возможно, повлекло бы за собой ошибки.
# Чтобы реализовать такое поведение с помощью пользовательского класса, в этот класс нужно
# добавить методы __enter__ и __exit__. Первый из них послужит для создания контекстного
# менеджера, подготавливающего необходимый нам ресурс для работы. Второй же будет
# закрывать использованные ресурсы, снова делая их доступными для остального кода.
# Рассмотрим простой пример с классом Product:

class Product5:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product5: {self.name}, ${self.price:.2f}"

    def _move_to_center(self):
        print(f"The product ({self}) occupies the center exhibit spot.")

    def _move_to_side(self):
        print(f"Move {self} back.")

    def __enter__(self):
        print("__enter__ is called")
        self._move_to_center()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ is called")
        self._move_to_side()

product = Product5("BMW Car", 50000)
with product:
     print("It's a very good car.")
# will print:
# __enter__ is called
# The product (Product5: BMW Car, $50000.00) occupies the center exhibit spot.
# It's a very good car.
# __exit__ is called
# Move Product5: BMW Car, $50000.00 back.

# Как видите, когда экземпляр встраивается в инструкцию with, вызывается метод __enter__.
# По завершении в ней операции происходит вызов метода __exit__.

# Однако следует отметить, что для создания контекстного менеджера мы можем реализовать
# методы __enter__ и __exit__.
# Это намного легче сделать с помощью функции декоратора contextmanager.


print('\n------- dunder methods: __getattr__()  __setattr__()  -------')
# 6. Улучшенный контроль доступа к атрибутам: __getattr__ and __setattr__
# Если у вас есть опыт программирования на других языках, то, возможно, вы привыкли
# создавать явные геттеры и сеттеры для атрибутов экземпляра. В Python нам не нужно
# использовать эти методы контроля доступа для каждого конкретного атрибута. Однако у нас
# есть возможность получить контроль благодаря реализации методов __getattr__ и __setattr__.
# Метод __getattr__ вызывается при обращении к атрибутам экземпляра, а метод __setattr__ —
# при их установке: (смотри пример ниже)
# 
# Метод __setattr__ вызывается каждый раз при попытке установить атрибут объекта.
# Для правильного его применения вам придется использовать метод суперкласса — super().
# В противном случае это приведет к бесконечной рекурсии. 
# 
# После установки атрибута formatted_name он станет частью объекта __dict__, вследствие 
# чего __getattr__ вызываться не будет.
# 
# Отмечу, что есть и другой магический метод, тесно связанный с контролем доступа — 
# это __getattribute__. Он похож на __getattr__, но вызывается при каждом обращении к
# атрибуту. Кроме того, он схож и с __setattr__, в связи с чем также подразумевает
# использование super() в своей реализации во избежание ошибки бесконечной рекурсии.
class Product:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == "formatted_name":
            print(f"__getattr__ is called for {item}")
            formatted = self.name.capitalize()
            setattr(self, "formatted_name", formatted)
            return formatted
        else:
            raise AttributeError(f"no attribute of {item}")

    def __setattr__(self, key, value):
        print(f"__setattr__ is called for {key!r}: {value!r}")
        super().__setattr__(key, value)
 
product = Product("taBLe")  # prints: __setattr__ is called for 'name': 'taBLe'
print(f'product.name: {product.name}')  # product.name: taBLe
print('------')
print(f'product.formatted_name(1): {product.formatted_name}')
# prints:
# __getattr__ is called for formatted_name
# __setattr__ is called for 'formatted_name': 'Table'
# product.formatted_name(1): Table
print('------')
print(f'product.formatted_name(2): {product.formatted_name}')  # prints: product.formatted_name(2): Table

