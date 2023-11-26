def count_vowels_consonants(string):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    vowel_count = 0
    consonant_count = 0
    for letter in string.lower():
        if letter in vowels:
            vowel_count += 1
        elif letter in consonants:
            consonant_count += 1
    return vowel_count, consonant_count


user_input = input('Напиши какое нибудь предложение: ')
vowels_found, consonants_found = count_vowels_consonants(user_input)
print(f'Количество гласных букв: {vowels_found}\n'
      f'Количество согласных букв: {consonants_found}')


input('\n\nНажмите "ENTER" для завершения.')


# Мой ввод

# Напиши что-нибудь: Ван Пис величайшее аниме!
# Количество гласных букв: 10
# Количество согласных букв: 11
