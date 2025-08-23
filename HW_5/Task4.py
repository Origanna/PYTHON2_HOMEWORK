# Задание 4.

def substrings(s):
    """
    Генератор всех возможных подстрок строки s.
    :param s: Строка, из которой будут извлекаться подстроки
    :return: Генератор подстрок
    """

    length = len(s)
    # Генерируем подстроки, начиная с каждой позиции в строке
    for start in range(length):
        # Итерируем от текущей позиции до конца строки
        for end in range(start + 1, length + 1):
            yield s[start:end]

# Пример использования
for substring in substrings('abc'):
    print(substring)