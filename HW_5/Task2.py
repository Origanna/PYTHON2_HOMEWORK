# Задание 2.

def calculate_bonus(names, salary, bonus):
    """
    Рассчитывает бонус для каждого сотрудника.

    :param names: Список имен сотрудников.
    :param salary: Список зарплат сотрудников.
    :param bonus: Список премий в процентах.
    :return: Словарь с именем сотрудника в качестве ключа и суммой премии в качестве значения.
    """

    # Генератор словаря для расчета бонуса: имя сотрудника -> сумма премии
    result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
    return result

# Пример использования функции
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = calculate_bonus(names, salary, bonus)
print(result)