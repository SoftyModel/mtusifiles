def lab3():
    # Функция для вычисления i-го члена последовательности
    func_a = lambda i: ((-1) ** i) * (1 - ((2 * i - 1) / (2 * (i + 1))))

    # Ввод чисел n и k
    n = int(input("Введите n: "))
    k = int(input("Введите k: "))

    # Проверка на корректность введенных данных
    if n < k:
        print("Ошибка: n должно быть больше или равно k")
    else:
        print("n = {}, k = {}".format(n, k))
        print("Члены последовательности:")
        sum_a = 0
        i = 0
        while i < n:
            a_i = func_a(i)
            if (i + 1) % k == 0:
                i += 1
                continue
            print("a_{} = {}".format(i, a_i))
            sum_a += a_i
            if abs(a_i) <= 10 ** (-6):
                print("Первый член последовательности, удовлетворяющий условию: a_{} = {}".format(i, a_i))
                break
            i += 1

        print("Сумма членов последовательности: {:.4f}".format(sum_a))