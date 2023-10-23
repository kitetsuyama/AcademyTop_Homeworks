def password_check():
    while True:
        password = input("Введите пароль: ")
        if len(password) <= 7:
            print("Пароль слишком короткий, придумайте другой.")
        elif " " in password:
            print("Пароль не должен содержать пробелы, придумайте другой.")
        elif password.lower() == password or password.upper() == password:
            print("Пароль должен содержать символы разных регистров, придумайте другой.")
        elif password.isalnum():
            print("Пароль должен содержать хотя бы один спецзнак, придумайте другой.")
        else:
            print("Пароль надежный!")
            # break


password_check()


input('\nНажмите "ENTER" для завершения.')


# !!! Мои вводы !!!

# Введите пароль: qwAS1!
# Пароль слишком короткий, придумайте другой.

# Введите пароль: qweASD 123!
# Пароль не должен содержать пробелы, придумайте другой.

# Введите пароль: qweasd123!!!
# Пароль должен содержать символы разных регистров, придумайте другой.

# Введите пароль: qweASD123
# Пароль должен содержать хотя бы один спецзнак, придумайте другой.

# Введите пароль: qweASD123!!!
# # Пароль надежный!
