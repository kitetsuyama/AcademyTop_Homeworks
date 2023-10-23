def find_intersection(list1, list2):
    # return list(set(list1) & set(list2))
    intersection = []
    for item in list1:
        if item in list2:
            intersection.append(item)
    return intersection


alex_list = ['Ван Пис', 'Блич', 'Магическая битва', 'Бродяга Кеншин', 'Скитальцы']
max_list = ['Наруто', 'Блич', 'Магическая битва', 'Берсерк', 'Скитальцы']
result = find_intersection(alex_list, max_list)
print(result)


input('\nНажмите "ENTER" для завершения.')
