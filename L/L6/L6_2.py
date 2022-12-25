from helper_functions import get_int_from_user

# positioned - идут по порядку
def get_float_from_user(comment: str, lower_bound: float = -9999999, upper_bound: float = 9999999) -> float:
    x = ''
    # while type(x) != float:
    while True:
        # пытаемся
        try:
            x = input(f'{comment} ')
            x = float(x)
            if x < lower_bound or x > upper_bound:
                # вызов исключений самостоятельно
                raise ValueError
            return x
        # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
        except Exception:
            print(f'Your input {x} was incorrect, we expected a float number lesser than {upper_bound} and bigger than {lower_bound}')
    # команда return возвращает результат работы функции


# print(3, 5, 6, 7)

my_number = get_float_from_user('Input float:')
print(my_number)
print(get_float_from_user('Float:', upper_bound=9999999999, lower_bound=0))


my_number = get_int_from_user('Input int:', lower_bound=0)
print(my_number)