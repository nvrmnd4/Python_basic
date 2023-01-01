# ДОМАШНЕЕ ЗАДАНИЕ №5 Полищук Анастасия

def n():
    a = int(input("""Введите сторону треугольника """))
    if a > 0:
        return a
    else:
        raise ValueError

def existance(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        result = True
        print(f'Треугольник со сторонами {a}, {b}, {c} существует')
    else:
        result = False
        print(f'Треугольника со сторонами {a}, {b}, {c} существовать не может')
    return result

def p(a, b, c):
    p = a + b + c
    print(f'Периметр треугольника со сторонами {a}, {b}, {c} будет равен {p}')
    return p

def s(a, b, c):
    pp = (a + b + c) / 2
    sq = pow(pp * (pp - a) * (pp - b) * (pp - c), 0.5)
    print(f'Площадь треугольника со сторонами {a}, {b}, {c} будет равна {sq}')
    return sq

if __name__ == '__main__':
    x = n()
    y = n()
    z = n()
    exist = existance(x,y,z)
    if exist == True:
        perimetr = p(x, y, z)
        square = s(x, y, z)
    else:
        print(f'У такого треугольника нет площади и периметра')