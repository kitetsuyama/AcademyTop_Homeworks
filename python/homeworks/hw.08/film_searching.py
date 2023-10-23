from marvel_base import full_dict

stage = {
    1: 'Первая фаза',
    2: 'Вторая фаза',
    3: 'Третья фаза',
    4: 'Четвёртая фаза',
    5: 'Пятая фаза',
    6: 'Шестая фаза'
}

user_input = input('Введите номер фазы: ')

try:
    phase = int(user_input)
except ValueError:
    raise TypeError('Введено некорректное значение. Ожидается цифра.')

if phase not in stage:
    raise ValueError('Фазы с таким номером не существует.')

phase_name = stage[phase]
print(f'Ваш выбор: {phase_name}')

films = []
for key, value in full_dict.items():
    if value["phase"] == phase_name:
        films.append(value['film'])

if films:
    print('\nСписок фильмов в выбранной фазе:')
    for film in films:
        print(film)
else:
    print('В выбранной фазе нет фильмов.')


input('\nНажмите "ENTER" для завершения.')
