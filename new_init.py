print('\n--------------------------------------------------------------------')
print('------------class and instance--------------------------------------\n')
class Matr:
    pass

print(1, Matr)  # <class '__main__.Matr'>
print(2, Matr())  # <__main__.Matr object at 0x7f9a37036d00>
print('type(Matr) =', type(Matr))  # <class 'type'>
print('type(Matr())', type(Matr()))  # <class '__main__.Matr'>
print('type(Matr())():', type(Matr())())  # <__main__.Matr object at 0x7f9a37036d00>
print(type(int))  # <class 'type'>
print(int)  # <class 'int'>


print('\n--------------------------------------------------------------------')
print('------------- __new__() and __init__() -----------------------------')
class Detail:
    def __init__(self, size):
        print('\nDetail,__init__(): self=', self)  # <__main__.Detail object at 0x7f9a36f61220>
        print('Detail,__init__(): type(self)=', type(self))  # <class '__main__.Detail'>
        self.size = size  # атрибут size появится в объекте 0x7f9a36f61220 только после выполнения данной команды
        self.speed = 1

    def __new__(cls, *args, **kwargs):
        """__new__ ВЫДЕЛЕТ память под объект класса cls (т.е. создает этот объект в памяти)"""
        print("\nDetail,__new__(): cls=", cls)  # <class '__main__.Detail'>
        print("Detail,__new__(): type(cls)=", type(cls))  # <class 'type'>
        s = super()
        print('s=', s)  # <super: <class 'Detail'>, <Detail object>>
        res = s.__new__(cls)
        print('res=', res)  # <__main__.Detail object at 0x7f9a36f61220>
        return res

detl = Detail(1)  # вначале выполнится __new__() а затем __init__()


print('\n--------------------------------------------------------------------')
