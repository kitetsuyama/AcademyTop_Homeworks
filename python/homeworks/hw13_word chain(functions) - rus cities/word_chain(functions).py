from cities import cities


def create_city_set():
    city_set = set()
    for city in cities:
        city_set.add(city['name'])
    return city_set


def check_input(city_set, user_input):
    if user_input == 'Стоп':
        print('Вы вышли из игры. Вы проиграли!')
        return False
    elif user_input not in city_set:
        print('Такого города нет. Вы проиграли')
        return False
    else:
        city_set.remove(user_input)
        return True


def find_city(city_set, letter):
    found_city = False
    for city in city_set:
        if city[0].upper() == letter:
            print('Компьютер называет город:', city)
            city_set.remove(city)
            found_city = True
            break
    return found_city


def game():
    city_set = create_city_set()

    while True:
        user_input = input('Введите название города: ').title()

        if not check_input(city_set, user_input):
            break

        last_letter = user_input[-1].upper()

        if last_letter == 'Ь':
            second_last_letter = user_input[-2].upper()
            found_city = find_city(city_set, second_last_letter)

            if not found_city:
                print('Компьютер не может найти подходящий город. Вы победили')
                break
        else:
            found_city = find_city(city_set, last_letter)

            if not found_city:
                print('Компьютер не может найти подходящий город. Вы победили')
                break


game()


input('\n\nНажмите "ENTER" для завершения.')
