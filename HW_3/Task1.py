# Задание 1.

elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]

# Создаем пустой список для дублирующихся элементов
duplicates = []

# Проходим по каждому элементу в списке
for x in elements:
    # Если элемент встречается больше одного раза и его еще нет в списке дубликатов
    if elements.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)
