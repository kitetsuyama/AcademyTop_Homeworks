def check_palindrome(*args):
    """
    Проверяет, являются ли заданные слова палиндромами.
    :param args:
    :return:
    """
    result = []
    for word in args:
        if word == word[::-1]:
            result.append({word: True})
        else:
            result.append({word: False})
        # if word == word[::-1]:
        #     result.insert(0, {word: True})
        # else:
        #     result.insert(0, {word: False})
    return result


def main():
    """
    Запрашивает у пользователя несколько слов через запятую, разбивает их на список.
    Выводит результат проверки на палиндром.
    :return:
    """
    user_input = input("Введите несколько слов через запятую: ").replace(' ', '').lower()
    word_list = user_input.split(',')
    result = check_palindrome(*word_list)
    # Решил сделать красивый вывод в столб
    print("Результат проверки на палиндром:")
    for item in result:
        for key, value in item.items():
            print(f"  {key}: {value}")
    # Простой вывод в строку в виде списка
    # print(result)


main()


input('\n\nНажмите "ENTER" для завершения.')


# Мой ввод!

# Введите несколько слов через запятую: мадАм, Левел,берсерк, радар, ванпис, ШАЛАШ

#       Красивый вывод
# Результат проверки на палиндром:
#  мадам: True
#  левел: True
#  берсерк: False
#  радар: True
#  ванпис: False
#  шалаш: True

#       В виде списка
# [{'мадам': True}, {'левел': True}, {'дом': False}, {'радар': True}, {'ванпис': False}, {'шалаш': True}]
