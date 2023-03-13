print('\n--------------------- class attributes -------------------------------------\n')
class Pet:
    cnt_n = 0  # count new
    cnt_ip = 0  # count init Pet
    cnt_is = 0  # count init sef
    cnt_isc = 0  # count init self class

    def __new__(cls, *args, **kwargs):
        cls.cnt_n += 1  # увеличевают экземпляры подклассов
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        Pet.cnt_ip += 1  # будут увеличивать только экземпляры данного класса ?? смотри Cat там увеличевает экземпляр подкласса
        self.cnt_is += 1  # увеличение только для экземпляра
        self.__class__.cnt_isc += 1  #ТАК ПРАВИЛЬНО! Будут увеличивать также экземпляры подклассов???? смотри Cat
        # такой же эффект: type(self).cnt_isc += 1
        self.sequence_number = type(self).cnt_isc
        p = 1

def check_pet_cnt():
    if Pet.cnt_isc == 0:
        print("\n--- Not create Pet ---\n")
    else:
        print(f"\n+++ Create {Pet.cnt_isc} pets +++\n")

check_pet_cnt()

print('---abstract Pet---')
pet_list = [Pet('abstract Pet') for _ in range(10)]
print('Pet.cnt_n=', Pet.cnt_n)  # 10
print('Pet.cnt_ip=', Pet.cnt_ip)  # 10
print('Pet.cnt_is=', Pet.cnt_is)  # 0
print('Pet.cnt_isc=', Pet.cnt_isc)  # 0
# Error: print(Pet.sequence_number)  # AttributeError: type object 'Pet' has no attribute 'sequence_number'

print('\npet_list[7]:')
# если в данной точке посмотреть через отладчик значения всех экземпляров в списке pet_list,
# то увидим у всех одинаковые значения cnt_n, cnt_ip, cnt_is, cnt_ics
# а вот sequence_number будет у каждого свой, например посмотрим значения pet_list[7]
print('cnt_n=', pet_list[7].cnt_n)  # 10
print('cnt_ip=', pet_list[7].cnt_ip)  # 10
print('cnt_is=', pet_list[7].cnt_is)  # 1
print('cnt_isc=', pet_list[7].cnt_isc)  # 10
print('sequence_number=', pet_list[7].sequence_number)  # 8
print()

class Cat(Pet):
    pass

def check_cat_cnt():
    if Pet.cnt_isc == 0:
        print("\n--- Not create Cat ---\n")
    else:
        print(f"\n+++ Create {Cat.cnt_isc} Cats +++\n")

check_cat_cnt()

print('---Murka---')
murka = Cat('Murka')
print('(Murka)Pet.cnt_isc=', Pet.cnt_isc)  # 10  НЕ увеличился, а должен был?
print('Cat.cnt_n=', Cat.cnt_n)  # 11
print('Cat.cnt_ip=', Cat.cnt_ip)  # 11
print('Cat.cnt_is=', Cat.cnt_is)  # 0
print('Cat.cnt_isc=', Cat.cnt_isc)  # 11  А здесь УВЕЛИЧЕНО !!!!
# Error: print('Cat.sequence_number)  # AttributeError: type object 'Cat' has no attribute 'sequence_number'

print('---Nika---')
nika = Cat('Nika')
print('(Nika)Pet.cnt_isc=', Pet.cnt_isc)  # 10  ВНИМАНИЕ! экземпляры Cat не увеличивают Pet.cnt_isc
print('Cat.cnt_n=', Cat.cnt_n)  # 12
print('Cat.cnt_ip=', Cat.cnt_ip)  # 12
print('Cat.cnt_is=', Cat.cnt_is)  # 0
print('Cat.cnt_isc=', Cat.cnt_isc)  # 12
print()
print('nika.cnt_n=', nika.cnt_n)  # 12
print('nika.cnt_ip=', nika.cnt_ip)  # 12
print('nika.cnt_is=', nika.cnt_is)  # 1
print('nika.cnt_isc=', nika.cnt_isc)  # 12
print('nika.sequence_number=', nika.sequence_number)  # 12
print('murka.sequence_number=', murka.sequence_number)  # 11

check_pet_cnt()
check_cat_cnt()

print('\n--------------------------------------------------------------------')
