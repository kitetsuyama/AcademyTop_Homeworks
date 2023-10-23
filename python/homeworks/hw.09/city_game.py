from cities import cities


def game():
    city_set = set()
    for city in cities:
        city_set.add(city['name'])

    while True:
        user_input = input('Введите название города: ').title()

        if user_input == 'Стоп':
            print('Вы вышли из игры. Вы проиграли!')
            break

        if user_input not in city_set:
            print('Такого города нет. Вы проиграли')
            break

        city_set.remove(user_input)
        last_letter = user_input[-1].upper()

        if last_letter == 'Ь':
            second_last_letter = user_input[-2].upper()

            found_city = False
            for city in city_set:
                if city[0].upper() == second_last_letter:
                    print('Компьютер называет город:', city)
                    city_set.remove(city)
                    found_city = True
                    break

            if not found_city:
                print('Компьютер не может найти подходящий город. Вы победили')
                break

        else:
            found_city = False
            for city in city_set:
                if city[0].upper() == last_letter:
                    print('Компьютер называет город:', city)
                    city_set.remove(city)
                    found_city = True
                    break

            if not found_city:
                print('Компьютер не может найти подходящий город. Вы победили')
                break


game()


input('\nНажмите "ENTER" для завершения.')