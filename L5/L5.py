# list - список

x = [3,4,5]
print(type(x))
print(x)

x = list((3,4,5))
print(type(x))
print(x)

# обращаемся поэлементно к списку
print(x[0], x[1], x[2])
# обращение к элементу, которого нет, выдает ошибку
# print(x[3])

# первый элемент с конца (справа)
print(x[-1])
print(x[-2])
print(x[-3])

random_list = [True, 5, 0.3, -905.43, 'I am a programmer', 'Hello', False, 3212]
print(random_list)
print(type(random_list))

# первый и последний элементы строки - такая же индексация
s = 'I am a programmer'
print(s[0], s[-1])

# задом на перед список вывести
print(x)
print(x[::-1])

# поменять местами первый и последний элементы

y = [7, 4, 98, 3]
z = [86, 23, 54790, 21, 5]

temp_y = y[0]
y[0] = y[-1]
y[-1] = temp_y
print(y)

# присваивание многих элементов в одну строку
print(z)
z[0], z[3] = z[3], z[0]
print(z)

# slice - диапазон/отрезок
sorted_marks = [100,98, 93, 85, 70, 60, 30]
# логика slice - [откуда вырезать (включительно): до куда резать (исключительно)]

print(sorted_marks[0:-1])
print(sorted_marks[:])
print(sorted_marks[0:3])

# исключить 3 элемент
print(sorted_marks[:3] + sorted_marks[4:])


# делаем наборной список

# фильтр по списку
# задаём новый пустой список, куда попадут все прошедшие проверку оценки
correct_marks = list()
# correct_marks = []  # Так тоже можно задать пустой список
# задаём пороговое значение
threshold_value = 60
# iteration - итерация (пройтись по массиву/списку данных)
print(len(sorted_marks))  # длина списка
i = 0  # итератор - показывает какой элемент мы сейчас рассматриваем
while i < len(sorted_marks):
    if sorted_marks[i] >= threshold_value:
        correct_marks.append(sorted_marks[i])
        print(f'{sorted_marks[i]} больше (или равно) {threshold_value}')
    # увеличиваем итератор чтобы на следующем шаге цикла обрабатывать новую переменную
    i += 1
print(correct_marks)

from random import shuffle, choice, choices

# loop - цикл (в программировании) петля (художественное)
# for - для

marks = [100, 101, 101, 3, 98, 93, 85, 70, 60, 30, 25, 5]
shuffle(marks)
print(marks)

correct_marks = list()
threshold = 60
# цикл-итератор, который заменяет необходимость i = 0 и i += 1 в цикле while
for mark in marks:
    if mark >= threshold:
        correct_marks.append(mark)
        # так тоже можно, но не нужно
        # [mark] - это создание списка из 1 элемента
        # создание списка занимает больше ресурсов чем создание переменной
        # correct_marks += [mark]
        # а вот так ничего не выйдет - прибавлять можно только список к списку
        # correct_marks += mark

print(correct_marks)

apple_weights = list(marks)
print(apple_weights)
max_apple = 0
for apple_weight in apple_weights:
    if max_apple < apple_weight:
        max_apple = apple_weight

print(max_apple)
# поиск минимального и максимального значений в списке (любом итерируемом объекте)
print(max(apple_weights))
print(min(apple_weights))

# sorted() не меняет исходного списка, а возвращает копию сортированную
# сортировка от меньшего большему
print(sorted(apple_weights))
# сортировка от большего к меньшему
print(sorted(apple_weights, reverse=True))

# .sort() меняет исходный список и не возвращает никакой копии
print('Before', apple_weights)
print(apple_weights.sort())
print('After', apple_weights)

# работает как и .sort() - меняет исходный список и не возвращает никакой копии
apple_weights.reverse()

# по индексу убрать элемент из списка
popped_element = apple_weights.pop(3)
print(apple_weights)
print(popped_element)

x = [5, 6, 9]
y = [13, 43, 2]
print(x + y)
y.extend(x)
print(y)

"""
# методы из random
print(choice(apple_weights))
print(choices(apple_weights, k=3))
"""