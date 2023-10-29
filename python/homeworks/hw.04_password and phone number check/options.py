password = input("Введите пароль: ")
if len(password) <= 7:
    print("Пароль слишком короткий, придумайте другой.")
elif " " in password:
    print("Пароль не должен содержать пробелы, придумайте другой.")
elif password.lower() == password or password.upper() == password:
    print("Пароль должен содержать символы разных регистров, придумайте другой.")
elif password.isalpha():
    print("Пароль должен содержать хотя бы один спецзнак, придумайте другой.")
else:
    print("Пароль надежный!")


input('\n\nНажмите "ENTER" для завершения.')
