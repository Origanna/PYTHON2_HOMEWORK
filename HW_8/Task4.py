# Задание 4.

import csv

def calculate_total_sales(input_file, output_file):
    sales_totals = {} # Словарь для хранения общей выручки по каждому продукту
    # Чтение данных из исходного CSV файла
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            product = row['название продукта']
            quantity = int(row['количество']) # Преобразование количества в целое число
            price_per_unit = float(row['цена за единицу']) # Преобразование цены за единицу в вещественное число
            total_sales = quantity * price_per_unit # Вычисление общей выручки
            if product in sales_totals:
                sales_totals[product] += total_sales # Добавляем к существующей выручке
            else:
                sales_totals[product] = total_sales # Создаем новую запись в словаре

    # Запись итоговых данных в новый CSV файл
    with open(output_file, 'w', newline='') as f:
        fieldnames = ['название продукта', 'общая выручка']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for product, total_sales in sales_totals.items():
            writer.writerow({'название продукта': product, 'общая выручка': total_sales})
            
if __name__ == "__main__":
    calculate_total_sales('sales.csv', 'total_sales.csv')