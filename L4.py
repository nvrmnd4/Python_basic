# Занятие 4, условные выражения и циклы

"""
тут только только одно из условий будет выполнено (первое правдивое)
if <condition>:
    <body of if>
elif <condition>:
    < body of elif >
elif <condition>:
    < body of elif >
...
elif <condition>:
    < body of elif >
else:
    < body of else>
*to be continued*
тут каждое условие может быть выполнено
if <condition>:
    <body of if>
if <condition>:
    <body of if>
if <condition>:
    <body of if>
if <condition>:
    <body of if>
"""

# 0-6 лет - ребёнок
# 6-18 лет - школьник(ца)
# 18-23 лет - студент(ка)
# 23-30 лет - юноша/девушка
# 30-65 лет - мужчина/женщина
# 65-90 лет - дедушка/бабушка
# 90+ лет - долгожитель

# while - пока
while True:
    try:
        user_input = input('Сколько вам полных лет? (или введите exit чтобы выйти) ')
        if user_input.lower() == 'exit':
            exit(0)
            quit(0)
        age_of_user = int(user_input)
        if age_of_user < 0:
            print('Ваш возраст отрицательный, с вами точно всё в порядке?')
        if 0 <= age_of_user < 6:
            print('Вы ребёнок!')
        if 6 <= age_of_user < 18:
            print('Вы школьник или школьница!')
        if 18 <= age_of_user < 23:
            print('Вы студент или студентка!')
        if 23 <= age_of_user < 30:
            print('Вы юноша или девушка!')
        if 30 <= age_of_user < 65:
            print('Вы взрослый!')
        if 65 <= age_of_user < 90:
            print('Вы дедушка или бабушка!')
        if age_of_user >= 90:
            print('Вы долгожитель!')
    except Exception:
        print('Возраст должен быть числом!')
        # ключевое слово, используется внутри циклов. Означает прервать текущую итерацию и начать всё с начала
        # (переход к первой строке тела цикла)
        continue




if age_of_user < 0:
    print('Ваш возраст отрицательный, с вами точно всё в порядке?')
elif age_of_user < 6:
    print('Вы ребёнок!')
elif age_of_user < 18:
    print('Вы школьник или школьница!')
elif age_of_user < 23:
    print('Вы студент или студентка!')
elif age_of_user < 30:
    print('Вы юноша или девушка!')
elif age_of_user < 65:
    print('Вы взрослый!')
elif age_of_user < 90:
    print('Вы дедушка или бабушка!')
else:
    print('Вы долгожитель!')


# ветвление - процесс производный от условных выражений

x = 5
y = 6

print(type(x / y))

print(type(x > y))
# bool - да или нет, правда или не правда, True or False
print(type(True))
print(type(False))

# примеры сравнения чисел (конвертирования их у тип булеан или флаг)
print('Int or float')
print(type(x < y))
print(type(x == y))
print(type(x != y))
print(type(x <= y))
print(type(x >= y))

print('Strings')
print(type('a' in 'Ukraine'))
print(type('Ukraine' in 'I live in Ukraine'))
# is - "является ли" ответ - да/нет True/False
print(type('Ukraine'.islower()))
print(type('Ukraine'.isupper()))
print(type('Ukraine'.isspace()))

if 5:
    print('Пять так пять :)')
else:
    print('Ну, не пять :(')
# при проверке значений проверяется не-пустота
print(bool(20))
print(bool(-0.0000001))
print(bool(0))
print(bool(''))
print(bool('a'))

s = 'Python'
s = ''
if s:
    print(s[-1])
else:
    print('String s is empty')



import time


def say_hi():
    print('hi')
    print('hi')


i = 0
# пока условие не перестанет быть правдой
while i < 10:
    # i = i + 1
    i += 1
    print(i)
# наконец-то (то что после цикла)
# infinite loop - вечный цикл. Ситуация, когда условие в цикле никогда не перестаёт быть правдой
# из него можно выйти, некорректно завершив работу программы:
# - кнопка СТОП в пайчарм
# - Закрыть пайчарм
# - если в консоли/терминале (не пайчарм), то Ctrl+C прерывает работу программы
while False:
    print('*')

text = """в
# наконец-то (то что после цикла)
# infinite loop - вечный цикл. Ситуация, когда условие в цикле никогда не перестаёт быть правдой
# из него можно выйти, некорректно завершив работу программы:
# - кнопка СТОП в пайчарм
# - Закрыть пайчарм
# - если в консоли/терминале (не пайчарм), то Ctrl+C прерывает работу программы
"""
search_query = 'в'
print(f'Searching in text for all "{search_query}"')
# while
print('Решение используя break')
search_index = 0
while True:
    search_index = text.find(search_query, search_index)
    say_hi()
    if search_index == -1:
        break
    print(f'{search_query} was found at position {search_index}')
    search_index += 1
    # time.sleep(2)
else:
    print('Из цикла НЕ вышли через break')

print('Решение без break')
# без использованя break, а использует условие в while
search_index = text.find(search_query)
while search_index != -1:
    print(f'{search_query} was found at position {search_index}')
    search_index += 1
    search_index = text.find(search_query, search_index)
else:
    print('Цикл выполнился 0 раз или он закончился без break :)')

#
# step over - переступить
# step into - вступить в функцию (в конце функции вернёмся где были)
# step into my code - вступать только в мои функции (а не библиотечные/служебный/встроенные)
# step out - находясь внутри функции, выйти из неё сразу на уровень выше
# run to cursor - выполнять до курсора