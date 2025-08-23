# Задание 5.

def calculate_danger(x):
    """Функция для расчета уровня опасности по формуле."""
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


def find_safe_depth(max_danger):
    """Функция для нахождения глубины, при которой уровень опасности близок к нулю."""
    d_min = 0
    d_max = 4
    d_middle = (d_min + d_max) / 2
    middle_danger = calculate_danger(d_middle)

    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            d_min = d_middle
        else:
            d_max = d_middle
        d_middle = (d_min + d_max) / 2
        middle_danger = calculate_danger(d_middle)

    return d_middle


def main():
    """Основная функция для управления программой и ввода данных."""
    max_danger = float(input('Введите допустимый уровень опасности: '))
    if max_danger < 0:
        print('Вы ввели недопустимое значение! Попробуйте еще раз.')
    else:
        safe_depth = find_safe_depth(max_danger)
        print(f'Приблизительная глубина безопасной кладки: {safe_depth:.9f} м')

        
main()