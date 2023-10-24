# password = input("Введите пароль: ")
#
# symbols = ["!", "@", "#", "$", "%", "&"]
# symbols_check = any(char in password for char in symbols)
# space_check = " " in password
# uppercase = any(char.isupper() for char in password)
# lowercase = any(char.islower() for char in password)
# different_cases = uppercase and lowercase
# length = len(password)
# valid_length = length >= 8
# if symbols_check and not space_check and different_cases and valid_length:
#     print("Пароль надежный!")
# else:
#     print("Пароль не надежный. Рекомендуется придумать другой.")

# password = input('Введите пароль: ')
#
# if ' ' in password:
#     print('Пароль не должен содержать пробелы')
# elif len(password) <= 7:
#     print('Пароль должен быть более 7 символов длиной')
# elif not any(char.isdigit() for char in password):
#     print('Пароль должен содержать хотя бы одну цифру')
# elif not any(char.isupper() for char in password) or not any(char.islower() for char in password):
#     print('Пароль должен содержать символы разных регистров')
# elif not any(not char.isalnum() for char in password):
#     print('Пароль должен содержать хотя бы один спецзнак')
# else:
#     print('Пароль надежный')

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
