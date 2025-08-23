# Задание 5.

import csv
import json

def convert_csv_to_json(input_file, output_file):
    books_by_author = {} # Словарь для хранения книг по авторам
    
    # Чтение данных из CSV файла
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }
            if author in books_by_author:
                books_by_author[author].append(book) # Добавляем книгу к существующему автору
            else:
                books_by_author[author] = [book] # Создаем новый список книг для нового автора
            
    # Запись данных в JSON файл
    with open(output_file, 'w') as f:
        json.dump(books_by_author, f, indent=4) # Сохраняем данные в JSON формате

if __name__ == "__main__":
    convert_csv_to_json('books.csv', 'books_by_author.json')