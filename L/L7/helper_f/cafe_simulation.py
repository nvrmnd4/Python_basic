# можно, но не одобряется
 # from helper_functions.input_numbers import get_int_from_user
 # нужно, но возможно только при заполненном __init__.py
 from helper_functions import get_int_from_user


 def display_menu(menu_cafe: list):
     """ стандарт документирования функций
     # ответственность функции. Что она делает? (за что отвечает)
     Пронумеровывает меню и красиво его отображает. Всегда добавляет пункт "Выход" (последним в нумерации)
     :param menu_cafe: непосредственно меню, которое будет отображено
     :return: ничего
     """
     print('Меню')
     for i, element in enumerate(menu_cafe):
         print(f'  {i + 1}. {element[0]:25}{element[1]:5.2f} UAH ')
     print(f'  {len(menu_cafe) + 1}. Выход')


 def purchase_from_menu(pocket_size: float, menu_cafe: list) -> float:
     """
     Осуществляет покупку из меню menu_cafe, если у pocket_size хватает средств
     Предоставляет пользователю выбор что купить
     :param pocket_size: средства пользователя
     :param menu_cafe: меню из которого покупают
     :return: обновлённое значение средств пользователя
     """
     display_menu(menu_cafe)
     exit_index = len(menu_cafe) + 1
     print(f'У вас есть {pocket_size:6.2f} UAH. Что будете заказывать?')
     menu_index = get_int_from_user('> ', lower_bound=1, upper_bound=exit_index)
     if menu_index == exit_index:
         print(f'Приходите еще, будем рады вас видеть!')
         exit(0)
     menu_item = menu_cafe[menu_index - 1]
     if pocket_size < menu_item[1]:
         print(f'Вы не можете себе это позволить, у вас осталось только: {pocket_size:6.2f} UAH')
     else:
         pocket_size -= menu_item[1]
         print(f'Сейчас вам будет подано {menu_item[0]}, пожалуйста ожидайте. Желаете что-нибудь еще?')
     input('Нажмите Enter чтобы продолжить...')
     return pocket_size


 # проверка что это выполняется даже когда файл импортируется
 # print(f'My file.txt name is {__name__}')