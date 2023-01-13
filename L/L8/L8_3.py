my_fruits = {'banana': 2, 'apple': 3, 'pineapple': 1}
friend_fruits = {'banana': 1, 'apple': 5, 'watermelon': 1}

our_fruits = dict(my_fruits)

# считаем сколько всего фруктов
for name, quantity in friend_fruits.items():
    if name in our_fruits:
        our_fruits[name] += quantity
    else:
        our_fruits[name] = quantity
print(our_fruits)

# our_fruits = dict(my_fruits) тоже самое our_fruits_2 = {**my_fruits}

our_fruits_2 = {**my_fruits, **friend_fruits}
for name, quantity in my_fruits.items():
    if name in friend_fruits:
        our_fruits_2[name] += quantity
print(our_fruits_2)

our_fruits_3 = dict(my_fruits, **friend_fruits)
print(our_fruits_3)

my_fruits.update(friend_fruits)
print(my_fruits)

# union - объединение
print('Какие виды фруктов у нас есть вместе', set(my_fruits.keys()).union(set(friend_fruits.keys())))
print('Есть только у меня', set(my_fruits.keys()) - set(friend_fruits.keys()))
print('Есть только у друга', set(friend_fruits.keys()) - set(my_fruits.keys()))

# проверка есть ли пересечения в ключах, нужно ли писать обработку
print('Общие виды фруктов', set(friend_fruits.keys()).intersection(set(my_fruits.keys())))
