while True:
    try:
        inp = str(input())
        if inp == "Привіт" or inp == "Хай" or inp == "Доброго вечора":
            print("Доброго вечора, я бот з України!")
        else:
            print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
            feeling = str(input())
            if feeling == "Як справи?" or feeling == "Що робиш?" or feeling == "Чим займаєшся?":
                print ("Вчусь програмувати на Python!")
            else:
                print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
                film = str(input())
                if film == "Фільм" or film == "Кінотеатр" or film == "Серіал":
                    print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Бойцовський клуб, він просто бомба!")
                else:
                    print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
                    bye = str(input())
                    if film == "Бувай" or film == "Надобраніч" or film == "Гудбай" or film == "До зустрічі":
                        print("Побачимось у мережі, I'll be back")
                    else:
                        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
                        break
    except Exception:
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
        continue
