from marvel import full_dict


def get_sort_dict(key, reversed=False):
    """
    Функция для сортировки словаря по заданному ключу и опциональному обратному порядку
    :param key: Ключ, по которому будет производиться сортировка
    :param reversed: Опциональный параметр, указывающий, нужно ли сортировать в обратном порядке (по умолчанию False)
    :return: Отсортированный словарь
    """
    sorted_dict = dict(sorted(full_dict.items(), key=lambda x: x[1][key], reverse=reversed))
    return sorted_dict


# вызов функции для сортировки словаря по ключу 'screenwriter' во вложенных словарях в прямом порядке
sorted_result = get_sort_dict('screenwriter')
print(sorted_result)

# вызов функции для сортировки словаря по ключу 'screenwriter' во вложенных словарях в обратном порядке
reversed_sorted_result = get_sort_dict('screenwriter', reversed=True)
print(reversed_sorted_result)


input('\n\nНажмите "ENTER" для завершения.')

