# Задача 1. 
# Say Hello World
print('Hello World!')

# Arithmetic operators 
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

# Задача 2. Квадрат и прямоугольник
l_sq = int(input('Введите длину стороны квадрата: '))

print(f' Периметр: {l_sq * 4}')
print(f' Площадь: {l_sq * l}')

l_rect = int(input('Введите длину прямоугольника: '))
w_rect = int(input('Введите ширину прямоугольника: '))

print(f' Периметр: {(l_rect + w_rect) * 2}')
print(f' Площадь: {l_rect * w_rect}')

# Задача 3. Приложение для финансового планирования

salary = int(input('Введите заработную плату руб/мес: '))
hyphoteca = int(input('Какой процент ЗП уходит на ипотеку?: '))
life = int(input('Какой процент уходит на жизнь?: '))

print(f'На ипотеку было потрачено: {salary / 100 * hyphoteca * 12} рублей')
print(f'Было накоплено: {salary * ((100 - hyphoteca - life)/100) * 12} рублей')

