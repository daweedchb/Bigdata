import math


def task1(tr1, tr2, tr3, sq1, sq2, r):
    res = {"Triangle": task3(tr1, tr2, tr3), "Rectangle": (sq1 * sq2), "Circle": math.pi * pow(r, 2)}
    return res


def task2(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    elif op == '//':
        return a // b
    elif op == 'pow':
        return math.pow(a, b)
    elif op == 'abs':
        return abs(a)
    elif op == '**':
        return a ** b


def task3(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print('===Задание 1===')
a, b, c = [int(x) for x in input('Введите стороны треугольника: ').split()]
sq1, sq2 = [int(x) for x in input('Введите стороны прямоугольника: ').split()]
r = int(input('Введите радиус круга: '))
print(task1(a, b, c, sq1, sq2, r))

print('===Задание 2===')
a, b, operation = input("Введите числа и требуемую операцию: ").split()
print(task2(int(a), int(b), operation))

print('===Задание 3===')
tr1, tr2, tr3 = [int(x) for x in input('Введите стороны треугольника: ').split()]
print(task3(tr1, tr2, tr3))
