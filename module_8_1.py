def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exc:
        print(f'Нельзя сложить строку и число', exc)
        return str(a) +str(b)
    finally:
        print('Проверка успешна!')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(round(add_everything_up(123.456, 7),3))