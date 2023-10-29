import csv
import json


class CsvFileHandler:
    """
    Класс для работы с файлами CSV.
    """
    def read_file(self, filepath, as_dict=False):
        """
        Метод для чтения данных из файла CSV.

        :param filepath: Путь к файлу.
        :param as_dict: Флаг, указывающий, нужно ли возвращать данные в виде списка словарей.
        :return: Список данных из файла.
        """
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            if as_dict:
                headers = next(reader)
                return [dict(zip(headers, row)) for row in reader]
            else:
                return [row for row in reader]

    def write_file(self, filepath, data, as_dict=False):
        """
        Метод для записи данных в файл CSV.

        :param filepath: Путь к файлу.
        :param data: Данные для записи.
        :param as_dict: Флаг, указывающий, являются ли данные словарями.
        :return: None
        """
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            if as_dict:
                headers = data[0].keys()
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())
            else:
                writer.writerows(data)

    def append_file(self, filepath, data, as_dict=False):
        """
        Метод для добавления данных в конец файла CSV.

        :param filepath: Путь к файлу.
        :param data: Данные для добавления.
        :param as_dict: Флаг, указывающий, являются ли данные словарями.
        :return: None
        """
        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            if as_dict:
                headers = data[0].keys()
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())
            else:
                writer.writerows(data)


class JsonFileHandler:
    """
    Класс для работы с JSON-файлами.
    """
    def read_file(self, filepath, as_dict=False):
        """
        Читает содержимое JSON-файла.

        :param filepath: Путь к файлу.
        :param as_dict: Флаг, указывающий нужно ли преобразовать содержимое в словарь.
        :return: Содержимое файла в виде словаря (если as_dict=True) или объекта JSON.
        """
        with open(filepath, 'r') as file:
            if as_dict:
                return json.load(file)
            else:
                return json.load(file)

    def write_file(self, filepath, data, as_dict=False):
        """
        Записывает данные в JSON-файл.

        :param filepath: Путь к файлу.
        :param data: Данные для записи.
        :param as_dict: Флаг, указывающий нужно ли преобразовать данные в словарь.
        :return: None.
        """
        with open(filepath, 'w') as file:
            if as_dict:
                json.dump(data, file, indent=4)
            else:
                json.dump(data, file, indent=4)

    def append_file(self, filepath, data):
        """
        Вызывает исключение, так как JSON-файлы не поддерживают операцию добавления.

        :param filepath: Путь к файлу.
        :param data: Данные для добавления.
        :return: None.
        """
        raise TypeError("JSON files do not support append operation.")


class TxtFileHandler:
    """
    Класс для работы с TXT-файлами.
    """
    def read_file(self, filepath):
        """
        Читает содержимое TXT-файла.

        :param filepath: Путь к файлу.
        :return: Содержимое файла в виде списка строк.
        """
        with open(filepath, 'r') as file:
            return file.readlines()

    def write_file(self, filepath, data):
        """
        Записывает данные в TXT-файл.

        :param filepath: Путь к файлу.
        :param data: Данные для записи в виде списка строк.
        :return: None.
        """
        with open(filepath, 'w') as file:
            file.writelines(data)

    def append_file(self, filepath, data):
        """
        Добавляет данные в конец TXT-файла.

        :param filepath: Путь к файлу.
        :param data: Данные для добавления.
        :return: None.
        """
        with open(filepath, 'a') as file:
            file.write(data)


# Пример использования класса CsvFileHandler
csv_handler = CsvFileHandler()

# Чтение данных из CSV файла
data = csv_handler.read_file('data.csv')
print(data)

# Запись данных в CSV файл
data = [['Name', 'Age'], ['Misha', 25], ['Bob', 30]]
csv_handler.write_file('data.csv', data)

# Дополнение данных в CSV файле
new_data = [['Sam', 35], ['David', 33]]
csv_handler.append_file('data.csv', new_data)

# Пример использования класса JsonFileHandler
json_handler = JsonFileHandler()

# Чтение данных из JSON файла
data = json_handler.read_file('data.json')
print(data)

# Запись данных в JSON файл
data = [{'Name': 'Oleg', 'Age': 25}, {'Name': 'Alex', 'Age': 21}]
json_handler.write_file('data.json', data)

# Попытка дополнения данных в JSON файле (должно возникнуть исключение TypeError)
new_data = {'Name': 'Boby', 'Age': 30}
try:
    json_handler.append_file('data.json', new_data)
except TypeError as e:
    print(f"Ошибка: {e}")

# Пример использования класса TxtFileHandler
txt_handler = TxtFileHandler()

# Чтение данных из TXT файла
data = txt_handler.read_file('data.txt')
print(data)

# Запись данных в TXT файл
data = 'Hello Vladimir!'
txt_handler.write_file('data.txt', data)

# Дополнение данных в TXT файле
new_data = ' Wazzuuuuuuuup!'
txt_handler.append_file('data.txt', new_data)


input('\n\nНажмите "ENTER" для завершения.')
