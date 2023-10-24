user_input = input('Введите номера телефонов через точку с запятой (без пробелов): ').split(';')
for number in user_input:
    cleaned_number = number.replace('(', '').replace(')', '').replace('-', '').replace(' ', '').replace('+', '')
    try:
        if len(cleaned_number) != 11:
            raise ValueError(f'Номер телефона {number} не содержит 11 цифр')
        if not cleaned_number.startswith('8') and not cleaned_number.startswith('7'):
            raise ValueError(f'Номер телефона {number} не начинается с 8, 7, +7')
        if not cleaned_number[1:].isdigit():
            raise ValueError(f'Номер телефона {number} содержит недопустимые символы')
        print(f'Номер телефона {number} валиден')
    except ValueError as e:
        print(e)


input('\n\nНажмите "ENTER" для завершения.')


# +77053183958;+77773183958;87773183958;+(777)73183958;+7(777)-731-83-58;+7(777) 731 83 58 - номера все валидные
# +770531383958;+97773183958;87d731g3958;+(777)73183958;+7(777)-731-8g-58;+7(7778) 731 83 58 - номера с косяками
