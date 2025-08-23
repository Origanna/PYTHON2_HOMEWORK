# Задание 4.

# main.py
import sys
import date_validator

# Проверяем количество аргументов командной строки
if len(sys.argv) != 2:
    print("Usage: python date_validator.py DD.MM.YYYY")
    sys.exit(1)

# Получаем дату из аргументов командной строки
date_input = sys.argv[1]

# Проверяем, является ли дата валидной
if date_validator.is_valid_date(date_input):
    print("True")
else:
    print("False")