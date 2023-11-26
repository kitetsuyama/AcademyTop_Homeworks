user_name = input('Введите имя: ')
user_input = input('Напишите что-нибудь: ')


class ExtraMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['extra_field'] = f'Привет {user_name}!'
        attrs['extra_method'] = lambda self: print(user_input)
        return super().__new__(cls, name, bases, attrs)


class MyClass1(metaclass=ExtraMeta):
    pass


class MyClass2(metaclass=ExtraMeta):
    pass


obj1 = MyClass1()
obj2 = MyClass2()

print(f'\nКласс 1:\n{obj1.extra_field}\n'
      f'Вы написали в метод:')
obj1.extra_method()

print(f'\nКласс 2:\n{obj2.extra_field}\n'
      f'Вы написали в метод:')
obj2.extra_method()


input('\n\nНажмите "ENTER" для завершения.')


# Мой ввод
#
# Введите имя: Алекс
# Напишите что-нибудь: Надеюсь, что правильно сделал ДЗ ^_^
#
# Класс 1:
# Привет Алекс!
# Вы написали в метод:
# Надеюсь, что правильно сделал ДЗ ^_^
#
# Класс 2:
# Привет Алекс!
# Вы написали в метод:
# Надеюсь, что правильно сделал ДЗ ^_^
