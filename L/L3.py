# Занятие 3 про строки

# int - целые числа
# float - плавающая запятая (нецелые)
# str - строка

# \ - escape character (символ избежания интерпретация, не будет видеть его как часть кода)
s1 = 'This is a "quote"'
s2 = "I've a laptop"
print(s1)
print(s2)
s3 = 'I\'ve something to say'
print(s3)

# много строк - это как запилить большой текст
text1 = """Hello
This is a multiline text
Another line
And another one!"""

text2 = '''Hello
This is a multiline text
Another line
And another one!'''

text3 = '''Hello 
this is Nastya hruck
pig pig'''

print(text1)
print(text2)
print(text3)

# текст с более чем одной строкой - в отличии от тройной кавычки
# здесь каждая строка приклеивается (конкатенируется) к предыдущей и между ними нет символа переноса строки
s4 = 'I\'ve something to ' \
     'say'

print(s4)

# создание пустой строки
empty_str = str()
another_empty_str = ''
yet_another_empty_str = ""
converted_int = str(5678)
print(empty_str)
print(converted_int)

print(type(converted_int))

# проверяем тип данных
print(type(empty_str))
print(type(converted_int))
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))
print(type(text1))
print(type(text2))

# конкатенация (concatenation) - это склеивание строк
s1s2 = s1 + ' ' + s2
print(s1s2)

# умножение строки на число это ее повторение, поставили точку и они через точку будут писаться
s3_5 = (s3 + '. ') * 5
print(s3_5)

text3 = ''
text3 += s1 + ' '
text3 += s2 + ' '
text3 += s3 + ' '
print(text3)

# оно узнает правда или неправда что слово есть в тексте
# операция присутствия (membership, substring)
if 'another' in text1.lower():
    print('Another is in text1')
else:
    print('Another is not in text1')


# группа функций, связанных с регистром
print(text1.lower())  # перевести всё в нижний регистр
print(text1.upper())  # перевести всё в верхний регистр
print(text1.capitalize())  # перевести первую букву всего текста в верхний регистр, остальные - в нижний
print(text1.title())  # перевести первую букву каждого слова в верхний регистр, остальные - в нижний
print(text1)

print(text1.lower().islower())  # проверяет всё ли в нижнем регистре
print(text1.isupper())  # проверяет всё ли в верхнем регистре


recipient_name = "John"
sender_name = "Sarah"
date = "7 Dec 2022"
pattern_letter = f"""
Hello, dear {recipient_name}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada eleifend risus eu finibus. Pellentesque vestibulum purus eget felis pulvinar.
Date: {date}
Sincerely yours, {sender_name} 
"""

print(pattern_letter)

# функция замены cлова в тексте
print(pattern_letter.replace('finibus', 'a bus'))

# убираем запятые и другие знаки из текста
s = "And, so, ; bye:!?."
filtered_s = s.replace(',', '').replace('.', '').replace('?', '').replace(';', '').replace('!', '').replace(':', '')
print(s)
print(filtered_s)

s = '__ _  ___My name is_____Kyrylo__ _  __   ___'
print(s.strip('_ '))  # убрать указанные символы с обоих внешних сторон строки
print(s.lstrip('_ '))  # убрать указанные символы с только левой стороны строки
print(s.rstrip('_ '))  # убрать указанные символы с только правой стороны строки


# индексация строк, поиск по символам
s = 'I live in Ukraine'
# в квадратных скобочках [] можно указывать адрес (индекс) символа внутри строки
# также можно указать диапазон, пользуясь :
# slice - указание какой диапазон
print(s[2:9])
print(s[:9])
print(s[2:])
print(s[:])

# синтаксис слайса: [start:end:step]
print(s[::-1])
# s = '1234567890'
# выводим строку наоборот через символ (желательно в комментариях так же указывать зачем)
print(s[::-2])


# функция find возвращает индекс (адрес) указанной подстроки
print(s.find('U'))
# вывести всю строку до буквы U
print(s[:s.find('U')])

# можно искать слова и даже фразы
print(s.find('Ukraine'))
print(s.find('in Ukraine'))

# поиск с левой и правой сторон
print(s.find('i'))
print(s.rfind('i'))  # поиск справа

# ищем расширение файла
filename1 = 'myfile.txt'
filename2 = 'mydocument.docx'
filename3 = 'run.exe'
filename4 = 'a.r.c.h.i.v.e.txt.zip'

print(filename4.rfind('.'))
print(filename4.find('.'))

# ищем точку, добавляем 1,то есть как со след. индекса вывести и отрезаем, но лучше искать справа.

print(filename1[filename1.rfind('.')+1:])
print(filename2[filename2.rfind('.')+1:])
print(filename3[filename3.rfind('.')+1:])
print(filename4[filename4.rfind('.')+1:])



text_to_split = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque sit amet est mattis elementum. Integer vitae hendrerit felis. Maecenas pulvinar auctor nulla, eget finibus diam ultrices eget. Morbi quis urna at mi aliquet laoreet et commodo turpis." \
                " Duis condimentum elementum dui vel viverra." \
                " Mauris sapien risus, volutpat suscipit fermentum varius, egestas id erat. Praesent a dui eget lorem luctus imperdiet. Morbi sodales pellentesque ante vel maximus. Ut consectetur tempor metus, quis tincidunt purus placerat vitae. Etiam augue ipsum, consectetur sed accumsan non, feugiat a risus. Pellentesque interdum nisi ex, ac tempus lorem semper quis. Aenean elit risus, auctor a."

# разделяем строки по какому-то символу. Этот символ вытирается, а возвращается список строк
print(text_to_split.split('.'))
# список
print(type(text_to_split.split('.')))


multiline_text = """line 1
line 2
line 3
line 4
line 5
"""

# по умолчанию делит по всем символам разделителям (whitespace)
print(multiline_text.split())
# делим по пробелам и видим странный символ \n
print(multiline_text.split(' '))
# делим по переносу на новую строку
print(multiline_text.split('\n'))

tabs = """asdsa	adssa
dsad	another tab	yet another
"""

print(tabs.split('\t'))
print(tabs.split('\n'))
print(tabs.split(' '))
print(tabs.split())

# join - обратная операция split, соединяет/склеивает список строк
print(("\n" + '*' * 10 + '\n').join(text_to_split.split('. ')))

# длина строки
print(len('12345'))
print(len('Python'))

x = input('Input something: ')
print(type(x))
# годятся чтобы проверить является ли строка целым числом больше ноля.
# отрицательное или десятичное число не узнаёт
print(x.isdigit())
print(x.isnumeric())
print(x.isdecimal())


x = ''
# while type(x) != int:
while not isinstance(x, int):
    # пытаемся
    try:
        x = input('Input integer number: ')
        x = int(x)
    # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
    except Exception:
        print(f'Your input {x} was incorrect, we expected an integer number')
        # в случае без цикла while, когда за исключением следует код,
        # требующий переменных, которые не получилось объявить - делаем exit()
        # exit(0)
    print(type(x))


x = ''
# while type(x) != float:
while not isinstance(x, float):
    # пытаемся
    try:
        x = input('Input float number: ')
        x = float(x)
    # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
    except Exception:
        print(f'Your input {x} was incorrect, we expected a float number')
    print(type(x))