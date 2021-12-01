
class MyMath:

    a = int()
    b = int()

    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b, 'Это сумма')

    def multiplication(self):
        c = self.a * self.b
        if c % 1 == 0:
            c = int(c)
        else:
            c = float(c)
        print(c, 'Это произведение')

    def division(self):
        if self.b == 0:
            print('Невозможно выполнить!!!')
        else:
            print(self.a / self.b, 'деление с остатком')
            print(self.a // self.b, 'деление без остатка')

    def subtraction(self):
        print(self.a - self.b, 'Вычитание')

    def pow_a(self):
        print(self.a ** self.b, '= Возведение числа', number1, 'в степень', number2)

    def pow_b(self):
        print(self.b ** self.a, '= Возведение числа', number2, 'в степень', number1)

    def sqrt_a(self):
        w = self.a ** 0.5
        if w % 1 == 0:
            w = int(w)
        else:
            w = float(w)
        print(w, 'Квадратный корень из числа', number1)

    def sqrt_b(self):
        y = self.b ** 0.5
        if y % 1 == 0:
            y = int(y)
        else:
            y = float(y)
        print(y, 'Квадратный корень из числа', number2)


number1 = float(input('Введите ваше число "а"\n'))
if number1 % 1 == 0:
    number1 = int(number1)
else:
    number1 = float(number1)
number2 = float(input('Введите ваше число "b"\n'))
if number2 % 1 == 0:
    number2 = int(number2)
else:
    number2 = float(number2)

while True:

    numbers = MyMath(number1, number2)
    print('(1) - addition(Сумма)')
    print('(2) - multiplication(Произведение)')
    print('(3) - division(Деление с остатком/без остатка)')
    print('(4) - subtraction(Вычитание)')
    print('(5) - pow_a(Возведение', number1, 'в степень (степень =', number2, ')')
    print('(6) - pow_b(Возведение', number2, ' в степень (степень =', number1, ')')
    print('(7) - sqrt_a(Квадратный корень из числа', number1, ')')
    print('(8) - sqrt_b(Квадратный корень из числа', number2, ')')
    print('(9) - exit(Ливнуть с этой говно программы)')
    command = input('Введите команду!\n')
    if command == '1':
        numbers.addition()
    elif command == '2':
        numbers.multiplication()
    elif command == '3':
        numbers.division()
    elif command == '4':
        numbers.subtraction()
    elif command == '5':
        numbers.pow_a()
    elif command == '6':
        numbers.pow_b()
    elif command == '7':
        numbers.sqrt_a()
    elif command == '8':
        numbers.sqrt_b()
    elif command == '9':
        print('ДО-СВИ-ДА-НИ-Я')
        break
    else:
        print(command + ': нераспознана')

numbers = MyMath(number1, number2)
