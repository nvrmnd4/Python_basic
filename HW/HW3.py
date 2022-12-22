# Домашнее задание №3 Полищук Анастасия

while True:
    try:
        inp = str(input())
        inp = inp.capitalize()
        if 'Привіт' in inp or "Хай" in inp or "Доброго вечора" in inp:
            print("Доброго вечора, я бот з України!")
        elif "Як справи?" in inp or "Що робиш?" in inp or "Чим займаєшся?" in inp:
            print ("Вчусь програмувати на Python!")
        elif "Фільм" in inp or "Кінотеатр" in inp or "Серіал" in inp:
            print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Бойцовський клуб, він просто бомба!")
        elif "Бувай" in inp or "Надобраніч" in inp or "Гудбай" in inp or "До зустрічі" in inp:
            print("Побачимось у мережі, I'll be back")
        else:
            print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
            break
    except Exception:
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
        continue