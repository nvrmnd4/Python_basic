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