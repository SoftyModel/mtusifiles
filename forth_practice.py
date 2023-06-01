def f_t():
    s = input('Введите слово\n')
    # строка - массив символов. В квадратных скобках можно выделить диапазон, например [1:4] или [:5] (с 1 по 6 невкл.)
    # [::] значит от начала до конца, -1 значит шаг, в данном случае развернуть все символы
    if s[::-1] == s:
        print('Слово - палиндром')
    else:
        print('Обычное слово')
def s_t():
    s = input('Введите строку\n')
    print(len(s))
    print(s * 3)
    print(s[0])
    print(s[:3])
    print(s[len(s) - 3:])
    print(s[::-1])
    print(s[1:-1])
def th_t():
    s = input('Введите строку\n')
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:-2])
    print(s[::2])
    print(s[1::2])
    print(s[-1::-2])
def fth_t():
    s = input('Введите строку\n')

    # проверка, четно или нет количество символов в строке
    if len(s) % 2 == 0:
        # Если да, берутся два среза и меняются местами от середины
        half = int(len(s) / 2)
        s1 = s[:half]
        s2 = s[half:]
        print(s2 + s1)
    else:
        # Если нет, первый срез (первая половина строки) больше второй на один символ
        half = int(len(s) / 2)
        s1 = s[:half + 1]
        s2 = s[half + 1:]
        print(s2 + s1)
def fifth_t():
    s = input('Введите строку\n')
    n = 0
    # n - счетчик, пополняется на 1, если для одного элемента из всей строки выполняется правило задачи
    for i in s:
        if i.isalpha():
            if i.islower():
                n += 1
    print(n)
def sixth_t():
    s = input('Введите строку\n')
    n = 0

    for i in s:
        if i.isnumeric():
            n += 1
    print(n)