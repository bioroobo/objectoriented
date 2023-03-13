print('\n--------------------------------------------------------------------')
class Point:
    not_own = 1  # это не собственный атрибут объекта
    def __init__(self, x, y):
        print('\nPoint,__init__: self=', self)
        print('Point,__init__: type(self)=', type(self))
        # собственные атрибуты объекта:
        self.x = x
        self.y = y
        self.thickness = 1

    def move(self):
        print('Point is moving')

    def stop(self):
        print("Point stopped")

pnt = Point(3,4)
pnt2 = Point(10, 40)
print(f'pnt == pnt2 : {pnt == pnt2}') # False

print()
print(f'print pnt: {pnt}')  # <__main__.Point object at 0x7f89cd6aefd0>
print(f'pnt type: {type(pnt)}')  # <class '__main__.Point'>
print(f'pnt is instance Point: {isinstance(pnt, Point)}')  # True
print(f'pnt is instance object: {isinstance(pnt, object)}')  # True

print()
pnt2.not_own = 2
print(f'атрибут класса: pnt.not_own={pnt.not_own}; pnt.not_own={pnt2.not_own}')  # pnt.not_own=1; pnt.not_own=2
pnt.atr1 = 1
print(f'собственные атрибуты объекта pnt и их значения: {pnt.__dict__}')  # {'x': 3, 'y': 4, 'thickness': 1, 'atr1': 1}
print(f'все доступные методы и атрибуты объекта pnt: {dir(pnt)}')

print()
print(f'вызов метода pnt.move(): {pnt.move()};  вызов метода Point.move(pnt): {Point.move(pnt)}')   # None  None
print('вызов метода pnt.move():')
pnt.move()
print('вызов метода Point.move(pnt)')
Point.move(pnt)

print('\nновый собственный атрибут с именем, совпадающим с именем метода: закоментирован')
#pnt2.move = 1000  # новый собственный атрибут с именем, совпадающим с именем метода "забивает" метод:
#pnt2.move()  # эта команда выбросит ошибку, т.к. здесь move уже не метод, а собственный атрибут

print('\n--------------------------------------------------------------------')
print('\n ===== Comment =====\n')

class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        """
        return tuple: (<comment text>, <votes_qty>):
        return (f"{self.text} {other.text}",
                self.votes_qty + other.votes_qty)
         return dict:
        """
        return {
            'text': f"{self.text} {other.text}",
            'votes_qty': self.votes_qty + other.votes_qty,
        }

    def __eq__(self, other) -> bool:
        if self.text == other.text and self.votes_qty == other.votes_qty :
            return True
        else:
            return False

first_comment = Comment("First comment")
first_comment.upvote()
second_comment = Comment("Second comment")  # Comment("First comment")  #
second_comment.upvote()

print('first_comment =', first_comment)
print('second_comment =', second_comment)
print('first_comment + second_comment =', first_comment + second_comment)
print('first_comment == second_comment :', first_comment == second_comment)
print('\n ===== END Comment =====\n')
print('\n--------------------------------------------------------------------')

x, _, y = (1, 2, 3) # x = 1, y = 3
print(f'{x},{y}')
for _ in range(10):
    print("_!", end='')


print('\n----Встроенные функции issubclass и isinstance отвечают на вопрос о наследовании----')
class A: pass
class B(A): pass

print(f'class A - parent; class B - subclass')
print(f'issubclass (B, A) == {issubclass(B, A)}')  # True
print(f'issubclass (A, B) == {issubclass(A, B)}')  # False
print(f'isinstance (B(), A) == {isinstance(B(), A)}')  # True
print(f'isinstance (B, A) == {isinstance(B, A)}')  # False
class C(A): pass
print(f"List of Class A Subclass Types: {A.__subclasses__()}")
print(f"type of A: {type(A)}")

print('\n--------------------------------------------------------------------')


