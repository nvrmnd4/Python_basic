# Лекция 10 Comprehension

import os
# range c 1 параметром - ДО чего (строго до, исключаем последний элемент)
print(list(range(10)))

# range c 2 параметрами - ОТ чего  вклю и до чего искл
print(list(range(5, 10)))

# range c 3 параметрами - ОТ чего  вклю и до чего искл и с каким шагом
print(list(range(50, 19, -5)))

l = list()
for el in range(10):
    if el > 2:
        l.append(el ** 2)
print(l)

# list comprehension - [
# <конечный элемент списка>
# for <обьявленная переменная>
# in <iterable из которого извлекаются значения>
# if <условие чтобы переменная попала в список>
l_comprehension = [x ** 2 for x in range(10) if x > 2]
print(type(l_comprehension), l_comprehension)

l_comprehension = [x ** 2 for x in range(10)]
print(type(l_comprehension), l_comprehension)

with open(os.path.join('..','L9','cafe_menu')) as f:
    clear_lines = [line.strip() for line in f.readlines()]
    print(clear_lines)
    for line in clear_lines:
        print(line)

d = {
    'one': 1,
    'two': 2,
    'three': 3
}
# Сделали кажды  пункт меню с ключом 0
d = {line:0 for line in clear_lines}
print(type(d), d)

# set comprehension
s = {x for x in [1, 2, 3, 4, 5]}
print(type(s), s)

# <class 'generator'> не хранит в памяти значения, только способ (for x in range(10))
comprehension = (x ** 2 for x in range(10))
print(type(comprehension), comprehension)

# Много раз запускаем и итерируем, чтобы он выдал значения
for x in comprehension:
    print(x)
    break
print(comprehension)

for x in comprehension:
    print(x)
    break
print(comprehension)

for x in comprehension:
    print(x)
    break
print(comprehension)

for x in comprehension:
    print(x)
    break
print(comprehension)
