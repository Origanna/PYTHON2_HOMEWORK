# Задание 4. Яма

# Запрос у пользователя глубины ямы
depth = int(input('Введите глубину ямы: '))

# Внешний цикл проходит по каждой строке ямы
for line in range(depth):
    # Генерация левой части ямы
    for left_number in range(depth, depth - line - 1, -1):
        print(left_number, end="")
    # Подсчёт количества точек
    point_count = 2 * (depth - line - 1)
    # Вывод точек
    print("." * point_count, end="")
    
    # Генерация правой части ямы
    for right_number in range(depth - line, depth + 1):
        print(right_number, end="")
    # Переход на новую строку после завершения текущей
    print()