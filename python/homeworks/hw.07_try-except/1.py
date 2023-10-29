data = ['1', '2', 3, '4d', '4', 5, 'six', '7', 8, '9', 'ten']
new_list = []

for item in data:
    try:
        new_list.append(int(item))
    except ValueError:
        print(f"Данные невалидны: {item}")

print(new_list)


input('\n\nНажмите "ENTER" для завершения.')


# Результат:
# Данные невалидны: 4d
# Данные невалидны: six
# Данные невалидны: ten
# [1, 2, 3, 4, 5, 7, 8, 9]
