# Домашнее задание №3 Полищук Анастасия

while True:
    try:
        inp = str(input())
        if 'Привіт' in inp or "Хай" in inp or "Доброго вечора" in inp:
            print("Доброго вечора, я бот з України!")
            feeling = str(input())
        elif "Як справи?" in feeling or "Що робиш?" in feeling or "Чим займаєшся?" in feeling:
            print ("Вчусь програмувати на Python!")
            film = str(input())
        elif "Фільм" in film or "Кінотеатр" in film or "Серіал" in film:
            print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Бойцовський клуб, він просто бомба!")
            bye = str(input())
        elif "Бувай" in bye or "Надобраніч" in bye or "Гудбай" in bye or "До зустрічі" in bye:
            print("Побачимось у мережі, I'll be back")
        else:
            print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
            break
    except Exception:
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
        continue