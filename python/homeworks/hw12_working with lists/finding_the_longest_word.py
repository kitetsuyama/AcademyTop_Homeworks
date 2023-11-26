def longest_string(strings: list) -> str:
    """
    Функция принимает список строк и возвращает самую длинную строку из списка.
    :param strings: список строк
    :return: самая длинная строка из списка
    """
    longest = ''
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest


strings = input('Напиши какое-нибудь предложение: ').split(' ')
# специально вывел чтобы было видно список
print(strings)
print(longest_string(strings))


input('\n\nНажмите "ENTER" для завершения.')


# Мои вводы

# Напиши какое нибудь предложение: One Piece the greatest anime
# ['One', 'piece', 'the', 'greatest', 'anime']
# greatest

# Напиши какое-нибудь предложение: Ван Пис величайшее аниме
# ['Ван', 'Пис', 'величайшее', 'аниме']
# величайшее
