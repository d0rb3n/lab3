#ex 1
class string:
  def getString(self):
    self.s=str(input())
  def printString(self):
    print(self.s.upper())
p1=string()
p1.getString()
p1.printString()

#ex 2
class shape:
    def area(self):
        self.a=0
        print ("area: ", self.a)
class square(shape):
    def __init__(self):
        self.length=float(input("length: "))
    def area(self):
        a=self.length**2
        print("area: ",a)

p1=shape()
p1.area()

p2=square()
p2.area()

#ex 3
class shape:
    def area(self):
        self.a=0
        print ("area: ", self.a)
class rectangle(shape):
    def __init__(self):
        self.length=float(input("length: "))
        self.width=float(input("width: "))
    def area(self):
        a=self.length*self.width
        print("area: ", a)
p1=shape()
p1.area()

p2=rectangle()
p2.area()

#ex 4
import math
class point:
    def show(self):
        self.x1=int(input("x1= "))
        self.y1=int(input("y1= "))
    def move(self):
        self.x2=int(input("x2= "))
        self.y2=int(input("y2= "))
    def dist(self):
        self.AB=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        print("distance= ", self.AB)

p1=point()
p1.show()
p1.move()
p1.dist()


#ex 5
class Account:
    def __init__(self):
        self.owner=str(input("Имя: "))
        self.balance=0
    def deposit(self):
        self.amount=int(input("Введите сумму: "))
        self.balance+=self.amount
        print("Пополнение: ", self.balance, "\nДоступно:", self.balance)
    def widthdrawals(self):
        self.amount=int(input("Введите сумму для снятия: "))
        if self.amount<=self.balance:
            self.balance-=self.amount
            print("Вы успешно сняли сумму.")
            print ("Доступно:", self.balance)
        else:
            print("У вас недостаточно средств.")

p1=Account()
p1.deposit()
p1.widthdrawals()

#ex 6
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)