# date_validator.py


def _is_leap_year(year):
    """
    Возвращает True, если год високосный, иначе False.

    Аргументы:
    year -- год для проверки

    Возвращает:
    True, если год високосный; False в противном случае
    """

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(date_str):
    """
    Проверяет, является ли дата в формате DD.MM.YYYY валидной.

    Аргументы:
    date_str -- строка с датой в формате DD.MM.YYYY

    Возвращает:
    True, если дата валидная; False в противном случае
    """
    
    # Проверяем длину строки
    if len(date_str) != 10:
        return False

    # Разделяем строку даты на день, месяц и год
    parts = date_str.split('.')
    
    # Проверяем, что строка корректно разделилась на три части
    if len(parts) != 3:
        return False
    
    # Проверяем, что все части являются целыми числами
    try:
        day, month, year = map(int, parts)
    except ValueError:
        return False
    
    # Проверяем валидность месяца
    if not (1 <= month <= 12):
        return False

    # Проверяем валидность дня в зависимости от месяца
    if not (1 <= day <= 31):
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if _is_leap_year(year) and day > 29:
            return False
        elif not _is_leap_year(year) and day > 28:
            return False
    
    # Если все проверки пройдены, дата валидна
    return True