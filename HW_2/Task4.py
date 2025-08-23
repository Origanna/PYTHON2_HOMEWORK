# Задание 4.

# Импортируем класс Fraction из модуля fractions
from fractions import Fraction

# Вводим первую дробь
frac1 = input("Введите первую дробь (a/b): ")

# Вводим вторую дробь
frac2 = input("Введите вторую дробь (a/b): ")

# Разделяем строки и преобразуем числитель и знаменатель первой дроби в целые числа
numerator1, denominator1 = map(int, frac1.split('/'))

# Разделяем строки и преобразуем числитель и знаменатель второй дроби в целые числа
numerator2, denominator2 = map(int, frac2.split('/'))

# Создаем объекты Fraction для первой и второй дроби
f1 = Fraction(numerator1, denominator1)
f2 = Fraction(numerator2, denominator2)

# Находим сумму дробей
sum_frac = f1 + f2

# Находим произведение дробей
product_frac = f1 * f2

# Выводим результат суммы дробей
print("Сумма:", sum_frac)

# Выводим результат произведения дробей
print("Произведение:", product_frac)