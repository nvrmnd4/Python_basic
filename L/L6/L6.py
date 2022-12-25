# пример работы с множеством (будет продолжение и разбор дальше)
x = set([5, 5, 4, 5, 4, 3, 1, 4, 3])
print(type(x), x)

x = {5, 5, 4, 5, 4, 3, 1, 4, 3}
print(type(x), x)

set_x = {'hello', 'python', 'world', 'hello', 'hello', 'python'}
print(set_x)
# set убивает дубликаты, когда мы выводим

# к сетам нельзя обращаться по индексу
# print(x[0])  # вызывает ошибку

# можно проходиться по всему сету (множеству), выдает все элементы в столбик
for element in set_x:
    print(element)

# операция поиска
if 'javascript' in set_x:
    print(True)
else:
    print(False)

if 'hello' in set_x:
    print(True)
else:
    print(False)


list_x = ['hello', 'python', 'javascript']

for element in list_x:
    if element in set_x:
        print(f'{element} is in {set_x}')
    else:
        print(f'{element} is not in {set_x}')

set_y = set(list_x)

# пересечение двух сетов
print("Пересечение", set_x.intersection(set_y))
# разница (то что есть только в левом, том из которого вычитаем)
print("Разница", set_x - set_y, set_y - set_x)
print("Разница с ключевым словом", set_x.difference(set_y), set_y.difference(set_x))
# объединение
print("Объединение", set_x.union(set_y))
print(set_x)

print("Симметричная разница (то чего нету обоих из них)", set_x.symmetric_difference(set_y))
# то же самое что симметрическая разница (set_x - set_y).union(set_y - set_x), то чего нет в них обоих сразу

# удаляем значение если оно известно, меняет исходный сет
set_x.remove("python")
print(set_x)

set_x.add("python3")
print(set_x)

# pop == "выдавить" первый элемент сета
x = set_x.pop()
print(x, set_x)

set_x.add('hello')
print(set_x)


set_tuple_check = {(5, 3), (3, 5)}
print(set_tuple_check)

# так делать нельзя, потому как сет не работает со списками - они непостоянны (динамичны),
# что делает невозможным гарант уникальности
# set_list_check = {[5, 3], [3, 5]}
# print(set_list_check)

# tuple / кортеж
# не редактируемый
# у него есть индексы и порядок
# могут быть дубликаты

x = (3, 5, [])
print(type(x), x)
print(x[0], x[1], x[-1], x[:1])

# не изменяемый
# x[0] = 0

x[2].append(2)
x[2].append(4)
print(x)