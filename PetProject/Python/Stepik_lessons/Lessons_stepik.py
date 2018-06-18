# 1.12 - 2
a = int(input("enter the number"))
if ((-15) < a <= 12) or (14 < a < 17) or (a >= 19):
    print(True)
else:
    print(False)

# 1.12 - 3
a = float(input("Input first value"))
b = float(input("Input second value"))
c = str(input("Input one of operations:'+', '-', '/', 'mod', 'div', 'pow' "))

def calc():
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/' and b != 0:
        print(a / b)
    elif c == '/' and b == 0:
        print("Деление на 0!")
    elif c == '*':
        print(a * b)
    elif c == 'mod'and b != 0:
        print(a % b)
    elif c == 'mod'and b == 0:
        print("Деление на 0!")
    elif c == 'pow':
        print(a ** b)
    elif c == 'div' and b != 0:
        print(a // b)
    elif c == 'div' and b == 0:
        print("Деление на 0!")
    else:
        print("Operation do not supported")

calc()
# 1.12 - 4
name = str(input("Input figure name"))

if name == "прямоугольник":
    a = float(input("Input the length of the first side"))
    b = float(input("Input the length of the second side"))
    count = a * b
    print(count)
elif name == "треугольник":
    a = float(input("Input the length of the first side"))
    b = float(input("Input the length of the second side"))
    c = float(input("Input the length of the third side"))
    p = (a+b+c)/2
    count = (p*(p-a)*(p-b)*(p-c))**0.5
    print(count)
elif name == "круг":
    r = float(input("Input radius"))
    pi = 3.14
    count = pi * (r**2)
    print(count)

# 1.12 - 4
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
if (a >= b and a >= c) and c >= b:
    print(a, "\n", b, "\n", c)
elif (a >= b and a >= c) and b >= c:
     print(a, "\n", c, "\n", b)

elif (b >= a and b >= c) and a >= c:
     print(b, "\n", c, "\n", a)
elif (b >= a and b >= c) and c >= a:
     print(b, "\n", a, "\n", c)

elif (c >= a and c >= b) and a >= b:
     print(c, "\n", b, "\n", a)
elif (c >= a and c >= b) and b >= a:
     print(c, "\n", a, "\n", b)

# 1.12 - 5
a = int(input("Сколько программистов в комнате? "))
if a == 0 or 5 <= a <= 20 or a % 10 >= 5 or 11 <= a % 100 <= 15 or a % 10 == 0:
    print(a, "программистов")
elif a % 10 == 1 or a == 1:
    print(a, "программист")
else:
    print(a, "программиста")

# 1.12 - 6
n = int(input("Узнай, счастливый ли твой билет. Введи номер билета:"))
a = n // 1000
b = n % 1000
c1 = (a // 100 ) + (a%100//10) + (a%100%10)
c2 = (b // 100 ) + (b%100//10) + (b%100%10)
if c1 == c2:
    print("Счастливый")
else:
    print("Обычный")