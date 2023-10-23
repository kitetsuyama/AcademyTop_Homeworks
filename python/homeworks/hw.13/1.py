from cities import cities


def check_input(user_input, city_set):
    if user_input == 'Стоп':
        print('Вы вышли из игры. Вы проиграли!')
        return False
    elif user_input not in city_set:
        print('Такого города нет. Вы проиграли')
        return False
    else:
        return True


def find_city(city_set, letter):
    for city in city_set:
        if city[0].upper() == letter:
            print('Компьютер называет город:', city)
            city_set.remove(city)
            return True
    return False


def game():
    city_set = set()
    for city in cities:
        city_set.add(city['name'])

    while True:
        user_input = input('Введите название города: ').title()

        if not check_input(user_input, city_set):
            break

        city_set.remove(user_input)
        last_letter = user_input[-1].upper()

        if last_letter == 'Ь':
            second_last_letter = user_input[-2].upper()
            if not find_city(city_set, second_last_letter):
                print('Компьютер не может найти подходящий город. Вы победили')
                break
        else:
            if not find_city(city_set, last_letter):
                print('Компьютер не может найти подходящий город. Вы победили')
                break


game()
