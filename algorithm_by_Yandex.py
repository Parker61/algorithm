# #https://education.yandex.ru/handbook/algorithms/article/polnyj-perebor-i-optimizaciya-perebora

# Выведите число перестановок P(n). В первой строке находится одно число n (1≤ n ≤7)

import math

n = int(input("Введите число n: "))

# Проверка условия 1 ≤ n ≤ 7
if n < 1 or n > 7:
    print("Число n должно быть от 1 до 7.")
else:
    # Вычисление факториала числа n
    permutations = math.factorial(n)
    print("Число перестановок P(n) =", permutations)
########################################################################
# # Выведите число сочетаний C(n,k). Формат ввода В первой строке находится два числа n (1≤n≤7), k (1≤k≤7).
# Для вычисления числа сочетаний C(n, k) можно использовать формулу:
# C(n, k) = n! / (k! * (n-k)!)# Где "!" обозначает факториал числа.# Например, если n=5 и k=3:#
# C(5, 3) = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = (5 * 4 * 3 * 2 * 1) / ((3 * 2 * 1) * (2 * 1)) = 10.
# Для реализации этого решения в программе на языке Python, можно использовать функцию math.factorial()
# для вычисления факториалов чисел:

import math

n, k = map(int, input().split())

result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

print(int(result))
# 2/
import math

n, k = map(int, input().split())
combination = math.comb(n, k)
print(combination)
# math.comb(n, k) используется для вычисления количества комбинаций из n элементов, выбранных k элементов одновременно.
# Это вычисляется с использованием формулы биномиальных коэффициентов, равной n! / (k! * (n-k)!), где n! обозначает
# факториал числа n.
################################################################
# Выведите число сочетаний с повторением С (n,k).).
# Формат ввода В первой строке находится два числа n (1≤n≤4), k (1≤k≤4).
# Для вычисления числа сочетаний с повторением С(n,k) можно воспользоваться формулой С (n + k - 1, k).

n, k = map(int, input().split())
result = 1
for i in range(k + n - 1, k, -1):
    result *= i
for i in range(n, 1, -1):
    result //= i
print(result)

################################################################
# вычисления числа сочетаний с повторениями из n объектов по k, вы можете использовать формулу:
# C(n,k)=n!/( (n−k)!⋅k!)
# Выведите число сочетаний с повторением С (n,k).
# В первой строке находятся два числа n(1≤n≤4), k(1≤k≤4).
# Выведите ответ на задачу.
import math

n, k = map(int, input().split())
comb = math.factorial(n + k - 1) // (math.factorial(k) * math.factorial(n - 1))
print(comb)


################################
def combination_with_repeats(n, k):
    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    return numerator / denominator


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


result = combination_with_repeats(n, k)
print(result)
################################################################
## Жадные алгоритмы
# #Бронирование переговорки
# Задано n интервалов. Требуется найти максимальное количество взаимно непересекающихся интервалов.
# Два интервала пересекаются, если они имеют хотя бы одну общую точку.
# Формат ввода
# В первой строке задано одно число n (1≤n≤100) — количество интервалов.
# В следующих n строках заданы интервалы li,ri (1 ≤ li ≤ ri ≤ 50). li и ri - начало и конец i-го интервала.
# Ввод 3 (n - intervals)
# 1 3
# 2 3
# 4 5
n = int(input())  # Ввод количества интервалов
intervals = []  # Создание списка для интервалов
for _ in range(n):
    l, r = map(int, input().split())  # Ввод левой и правой границы интервала
    intervals.append((l, r))  # Добавление интервала в список

intervals = [(1, 3), (2, 3), (4, 5)]
intervals.sort(key=lambda x: x[1])  # Сортировка интервалов по правой границе [(1, 3), (2, 3), (4, 5)]

count = 0  # Счетчик непересекающихся интервалов
last_end = -1  # Правая граница последнего выбранного интервала

for interval in intervals:
    if interval[0] > last_end:  # Если левая граница текущего интервала больше правой границы последнего выбранного инт.
        count += 1  # Увеличиваем счетчик
        last_end = interval[1]  # Обновляем правую границу последнего выбранного интервала

print(count)  # Вывод ответа на задачу 2


# 2.
def find_max_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # Сортируем список intervals по правому концу интервала.

    count = 0  # Счетчик взаимно непересекающихся интервалов
    end_time = -1  # Переменная для хранения времени окончания предыдущего интервала

    for interval in intervals:
        start_time, finish_time = interval
        if start_time > end_time:  # Если начало интервала больше времени окончания предыдущего интервала
            count += 1
            end_time = finish_time  # Обновляем время окончания

    return count


n = int(input())  # Считываем количество интервалов n.
intervals = [list(map(int, input().split())) for _ in range(n)]  # Создаем список интервалов intervals.

result = find_max_non_overlapping_intervals(n, intervals)
print(result)

# 3.
# сортирует интервалы по убыванию длины (т.е. добавляем самые максимальные интервалы), которые не пересекаются
# с уже выбранными интервалами.
intervals = [(1, 2), (1, 3), (4, 10)]
intervals.sort(key=lambda x: x[1] - x[0], reverse=True)  # [(4, 10), (1, 3), (1, 2)]
count = 0  # Счетчик непересекающихся интервалов
set_interval = set()
max_intervals = []  # max intervals to add
for interval in intervals:
    set_now = set(range(interval[0], interval[-1] + 1))
    if not set_now & set_interval:  # set(set_now).intersection( set_interval)
        set_interval = set_interval.union(set_now)  # set_interval | set_now
        max_intervals.append(interval)
        count += 1
print(count, set_interval, max_intervals, sep='\n')


# 2
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# [(4, 10), (1, 3)]
######################################################################
# Камни
# Вы играете в игру >: игру для двух игроков с двумя наборами камней по
# n и m штук. С каждым ходом один игрок может взять один камень (из любого набора) или два камня (по одному из обоих). Когда камень забрали, он выходит из игры. Побеждает игрок, который заберет последний камень. Первый ход за вами.
# Вы и ваш оппонент играете оптимально.# Формат ввода
# В первой строке содержится два числа # (1≤n≤10),
# (1≤m≤10) — количество ваших камней и количество камней у вашего оппонента.
# Формат вывода# В единственной строке выведите
# Loose, если вы заведомо проиграете, и # Win,
def game_result(n, m):
    if n % 2 == 0 and m % 2 == 0:
        print('Loose')
    else:
        print('Win')


n, m = map(int, input().split())
print(game_result(n, m))


###################################################################
# Ханойские башни
# Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3.
# Также в головоломке используется стопка дисков с отверстием посередине. Радиус дисков уменьшается снизу вверх.
# Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу.
# Диски в игре перемещаются по одному со стержня на стержень. Диск можно надеть на стержень, только если он пустой
# или верхний диск на нём большего размера, чем перемещаемый.
# Цель головоломки — перенести все диски со стержня 1 на стержень 3.
# Требуется найти последовательность ходов, которая решает головоломку <<Ханойские башни>>.
# Формат ввода В первой строке задано одно число �n (3≤�≤10)(3≤n≤10) — количество дисков на первой башне.
# Формат вывода# В первой строке выведите количество операций k.
# В следующих k строках выведите по два числа в каждой xi,yi (1≤xi,yi≤3) —
# переместить верхний диск со стержня xi на стержень yi.

def HanoiTowers(n, from_Peg, to_Peg, temp_Peg, lst):
    global move
    if n > 0:
        HanoiTowers(n - 1, from_Peg, temp_Peg, to_Peg, lst)
        # print(f'переложить с {from_Peg} на {to_Peg}')
        lst.append([from_Peg, to_Peg])
        move += 1
        HanoiTowers(n - 1, temp_Peg, to_Peg, from_Peg, lst)


if __name__ == '__main__':
    n = int(input())
    move = 0
    lst = []
    HanoiTowers(n, 1, 3, 2, lst)
    print(move)
    # [print(*i) for i in lst]
    [print(f'переложить с {i[0]} на {i[1]}') for i in lst]


################################################################################
# Ханойские башни
# Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3.
# Также в головоломке используется стопка дисков с отверстием посередине. Радиус дисков уменьшается снизу вверх.
# Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу.
# Диски в игре перемещаются по одному со стержня на стержень. Диск можно надеть на стержень, только если он пустой
# или верхний диск на нём большего размера, чем перемещаемый.
# Цель головоломки — перенести все диски со стержня 1 на стержень 3.
# Немного изменим правила. Теперь головоломка состоит из четырех стержней, а цель головоломки —
# перенести все диски со стержня 1 на стержень 4. Найдите минимальное количество ходов, за которое можно решить головол
# В единственной строке выведите ответ на задачу.
# решение не верно!!
def hanoi(n, source, target, auxiliary, extra):
    global move
    if n > 0:
        hanoi(n - 2, source, extra, target, auxiliary)
        print(f"Переместить диск {n} со стержня {source} на стержень {extra}")
        print(f"Переместить диск {n - 1} со стержня {source} на стержень {target}")
        print(f"Переместить диск {n} со стержня {extra} на стержень {target}")
        move += 1
        hanoi(n - 2, auxiliary, target, source, extra)


move = 0
n = 4  # Количество дисков
source = 1  # Начальный стержень
target = 3  # Целевой стержень
auxiliary = 4  # Вспомогательный стержень
extra = 2  # Дополнительный стержень

hanoi(n, source, target, auxiliary, extra)
print(move)

################################################################
# Сортировка выбором. Реализуйте сортировку выбором.
n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    min_indx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_indx]:
            min_indx = j
    arr[i], arr[min_indx] = arr[min_indx], arr[i]

print(*arr)
########################################################
# Слияние сортированных последовательностей
# Задано # n отсортированных по неубыванию последовательностей.
# Требуется найти отсортированную по неубыванию конкатенацию этих последовательностей.
# Запрашиваем у пользователя количество последовательностей
n = int(input())

# Создаем пустой список, в который будем добавлять последовательности
sequences = []

# Цикл для получения последовательностей от пользователя
for i in range(n):
    # Запрашиваем у пользователя саму последовательность и преобразуем её в список чисел
    sequence = list(map(int, input().split()))
    # Добавляем последовательность в список sequences
    sequences.append(sequence)

# Создаем пустой список, в который будем добавлять все числа из всех последовательностей
result = []

# Цикл для добавления чисел из всех последовательностей в список result
for sequence in sequences:
    # Расширяем список result, добавляя все числа из текущей последовательности
    result.extend(sequence)

# Сортируем список result в возрастающем порядке
result.sort()

# Выводим все числа из списка result, через пробел
for num in result:
    print(num, end=' ')


################################################################
# Сортировка слиянием  Реализуйте сортировку слиянием.
# Для реализации сортировки слиянием, нам понадобится две функции: функция merge_sort, которая разделяет массив на две
# половины и рекурсивно сортирует их, и функция merge, которая объединяет отсортированные половины обратно в один массив
# Сначала реализуем функцию merge, которая будет принимать на вход два отсортированных массива и возвращать
# объединенный отсортированный массив:
def merge(left, right):
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    # merged.extend(left[l:])
    merged += right[r:]
    # merged.extend(right[:r])
    return merged


# Затем реализуем функцию merge_sort, которая будет разделять массив на две половины и рекурсивно сортировать их:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# Теперь можем считать числа из ввода, вызвать функцию merge_sort и вывести отсортированный массив:
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = merge_sort(arr)
print(*sorted_arr)

##############################
# fibonacci
# recursion ( more memory) Рекурсивный алгоритм требует так много времени, потому что он повторяет множество одинаковых вычислений
n = int(input(''))


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(n))


# 2/ iteration method
def fib(n):
    if n <= 1:
        return n
    num_1, num_2 = 0, 1
    for _ in range(2, n + 1):
        res_now = num_1 + num_2  # без хранения всего массива
        num_1 = num_2
        num_2 = res_now
    return num_2


# 3/мемоизация: при вычислении чего-либо сохраните это в структуре данных, чтобы избежать повторных вычислений в будущем
def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]


print(fibonacci(10))  # Вывод: 55


# 4/ Последняя цифра числа Фибоначчи
def fibonacci_last_digit(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10

    return b % 10


n = int(input("Введите номер числа Фибоначчи: "))
last_digit = fibonacci_last_digit(n)
print(f"Последняя цифра числа Фибоначчи под номером {n} равна {last_digit}")

################################################################
# Наибольший общий делитель GCD(a,b)  двух положительных целых чисел  и  — это самое большое целое число
# , на которое можно поделить  и   без остатка
# 1.
a, b = map(int(input()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


################################################################
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = 24
num2 = 36
result = gcd(num1, num2)
print("Наибольший общий делитель чисел", num1, "и", num2, "равен", result)
# 2.
import math


def gcd(a, b):
    return math.gcd(a, b)


# Наименьшее общее кратное LCM(a,b)  для двух положительных целых чисел a и b — это самое маленькое целое число
# m, которое можно разделить и на a, и на b.
a, b = map(int, input().split())


def gcd(a, b):
    # Алгоритм Евклида для вычисления наибольшего общего делителя (НОД)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a, b):
    # НОК = a * b / НОД
    return (a * b) // gcd(a, b)


# Пример использования функции
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

lcm_result = lcm(num1, num2)
print("Наименьшее общее кратное:", lcm_result)
# 2.
import math

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

lcm = math.lcm(a, b)

print("Наименьшее общее кратное чисел", a, "и", b, "равно", lcm)


################################
# Жадные алгоритмы
# Задача «Размен»
# Размен: 1, 5, 10, 20, 50
# Предположим, что у кассира есть бесконечное количество монет номиналами 11, 55, 1010, 2020 и 5050.
# Найдите набор монет, с суммарным номиналом  в котором наименьшее количество монет. Требуется вывести
# номиналы монет в этом наборе.
# 1.
# Алгоритм решения этого кода основан на динамическом программировании и использует метод "минимальных монет" для
# размена суммы денег.
# - В начале определяется список возможных номиналов монет и создается список num_coins длиной (money + 1),
# который будет хранить количество монет для каждой суммы от 0 до money.
# - Затем устанавливается значение num_coins[0] равным 0, так как для суммы 0 не требуются монеты.
# - Создается список used_coins, который будет хранить список использованных монет для каждой суммы от 0 до money.
# - Далее, для каждой суммы m от 1 до money проходим по каждому номиналу монет.
# - Если текущая сумма больше или равна номиналу монеты и количество монет для (текущая сумма - номинал) плюс одна
# монета меньше количества монет для текущей суммы, то обновляем количество монет и список использованных монет.
# - На каждом шаге выбирается минимальное количество монет для текущей суммы.
# - В итоге, значение num_coins[money] будет содержать минимальное количество монет для размена суммы money.
# # - Чтобы восстановить список использованных монет, используется список used_coins[money].
# В конце программа выводит количество монет и список использованных монет для размена введенной суммы.

def exchange(money):
    coins = [1, 5, 10, 20, 50]  # Возможные номиналы монет
    num_coins = [float('inf')] * (money + 1)  # Инициализация количества монет для каждой суммы
    num_coins[0] = 0  # Для суммы 0 не нужны монеты
    used_coins = [[] for _ in range(money + 1)]  # Инициализация списка использованных монет

    for m in range(1, money + 1):  # Для каждой суммы
        for coin in coins:  # Проходим по каждому номиналу монет
            if m >= coin and num_coins[m - coin] + 1 < num_coins[m]:
                # Если текущая сумма больше или равна номиналу монеты и
                # количество монет для (текущая сумма - номинал) плюс одна
                # монета меньше количества монет для текущей суммы,
                # то обновляем количество монет и список использованных монет
                num_coins[m] = num_coins[m - coin] + 1
                used_coins[m] = used_coins[m - coin] + [coin]

    return num_coins[money], *used_coins[money]


n = int(input())  # Ввод суммы
count, *coins = exchange(n)  # Подсчет количества монет и использованных монет
print(count)  # Вывод количества монет
print(*coins)  # Вывод использованных монет
################################################################
# Специи Вор пробрался в лавку специй и нашел там n видов специй. В его рюкзак можно сложить до
# W фунтов, поэтому забрать все он не сможет. Предположим, в лавке находится   фунтов специй с номером i и стоимостью
# Первая строка ввода содержит n специй и вместимость рюкзака W. Следующие n строк указывают цену и вес специй.
# i-я строка включает в себя цену
# Формат вывода Максимальное значение специй, которые вместятся в рюкзак.

# n, W = map(int, input().split())
# c = [0] * n
# w = [0] * n
# for i in range(n):
#     c[i], w[i] = map(int, input().split())

n, W = 1, 1000
c, w = [500], [30]

d = {}  # dictionary - cost:weight
for i in range(n):
    c_i, w_i = c[i], w[i]
    d[c_i] = w_i
c = sorted(d, reverse=True)

# print(d)  # {60: 20, 100: 50, 120: 30}
# print(c)  # [120, 100, 60]

weight = 0
cost = 0
count = W
for i in range(n):
    if w[i] > W:
        while weight + (w[i] / w[i]) <= W and count:
            weight += w[i] / w[i]
            cost += (c[i] / w[i])
            count -= 1
    else:
        if weight + w[i] <= W and count:
            weight += w[i]
            cost += c[i]
            count -= 1

print(f'{cost:.3f}')
########################################################################
# Сувениры Турист зашел в сувенирную лавку и нашел там много привлекательных вариантов подарков друзьям и родным.
# Всего в лавке n сувениров, стоимость i-го сувенира i​  рублей.пределите, какое наибольшее количество сувениров
# сможет купить турист, если он может потратить не более �S рублей.
n, s = map(int, input().split())
prices = []

for _ in range(n):
    price = int(input())
    prices.append(price)

prices.sort()
count = 0
for i in range(n):
    if s - prices[i] >= 0:
        s -= prices[i]
        count += 1

print(count)
################################
# Рекламная кампанияУ вас есть популярная страница в интернете, на которой есть �n рекламных мест. Вы хотите
# продать их рекламодателям. Аналитики рассчитывают на �2clicks 2​ licks n​  кликов в день, соответственно.
# С вами связались �n рекламодателей, которые готовы заплатить �price 1​Как подобрать пары рекламных мест и
# рекламодателей так, чтобы получить максимальную прибыль?


n = int(input())
prices = list(map(int, input().split()))
clicks = list(map(int, input().split()))

prices.sort()
clicks.sort()

total = []
for i in range(n):
    total.append(prices[i] * clicks[i])

print(sum(total))
################################################################
# Сбор подписей Ваша задача — собрать подписи всех жильцов в доме. Вам известно время, в которое каждый
# из жильцов находится дома. Вы хотели бы собрать все подписи, приходя в дом минимальное количество раз.
# Для простоты давайте предположим, что вы сразу же собираете подписи всех жильцов, находящихся дома, когда заходите.
# Формат ввода Количество сегментов в первой строке — � n. Каждая из следующих � n строк содержит два целых числа
# � � l i​и � � r i​(разделены пробелом), которые указывают на координаты границ � i-го сегмента.
# Ограничения: 1 ≤ � ≤ 100 1≤n≤100; 0 ≤ � � ≤ � � ≤ 1 0 9 0≤l i​≤r i​≤10 9 для всех � i.
# Формат вывода Минимальное количество � k точек на первой строке и координаты � k точек целыми числами
# (разделены пробелом) на второй строке. Выводить точки можно в любом порядке. При наличии нескольких наборов точек,
# можно вывести любой из них.
# Таким образом, мы приходим к следующему алгоритму:
# -добавить в решение минимальное значение правой границы
# - отбросить все сегменты, покрытые
# - повторить.
n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments = sorted(segments, key=lambda x: x[1])
points = [segments[0][1]]
for i in range(1, n):
    if segments[i][0] > points[-1]:
        points.append(segments[i][1])

print(len(points))
print(" ".join(map(str, points)))
# 2.
segments.sort(key=lambda x: x[1])
points = []
while segments:
    r_m = segments[0][1]
    points.append(r_m)
    segments = [seg for seg in segments if seg[0] > r_m]

print(len(points))
print(" ".join(map(str, points)))


############################################################################################################
# Вычисление арифметического выражения без скобок Ввод содержит только
# строку � s длиной � n. Строка состоит из чисел операндов (числа от 0 до 99)
# и операций +, -, *. Посчитайте значения выражения.
# Формат ввода Ограничения: строка содержит максимум 20 20 символов.
# Формат вывода Выведите ответ на задачу.
# Пример 1 Ввод 5-8+7*4-8+9 Вывод 26 код на питоне
# алгоритм с использованием стека.
def calculate_expression(expression):
    operators = []
    operands = []

    # Разделяем арифметическое выражение на операторы и операнды
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Считываем число и добавляем его в список операндов
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            operands.append(int(num))
        elif expression[i] in ['+', '-', '*']:
            # Если встретили оператор, добавляем его в список операторов
            operators.append(expression[i])
            i += 1
        else:
            # Пропускаем пробелы
            i += 1
    # operands = sorted(operands, reverse=True) # may be will sort
    # Выполняем операции в порядке убывания приоритета
    while '*' in operators:
        i = operators.index('*')
        result = operands[i] * operands[i + 1]
        del operators[i]
        del operands[i]
        operands[i] = result

    while operators:
        operator = operators.pop(0)
        operand = operands.pop(0)
        next_operand = operands.pop(0)
        if operator == '+':
            result = operand + next_operand
        elif operator == '-':
            result = operand - next_operand
        operands.insert(0, result)

    return operands[0]


expression = input()
result = calculate_expression(expression)
print(result)


#######################################################################################################
################################################################################################################
#######################################################################################################
################################################################################################################
#######################################################################################################
################################################################################################################
#######################################################################################################
################################################################################################################
#######################################################################################################
################################################################################################################
#######################################################################################################
################################################################################################################
def exchange(money):
    coins = [1, 5, 10, 20, 50]
    num_coins = [0] * (money + 1)
    used_coins = [[] for _ in range(money + 1)]

    for m in range(1, money + 1):
        min_coins = float('inf')
        for coin in coins:
            if m >= coin and num_coins[m - coin] + 1 < min_coins:
                min_coins = num_coins[m - coin] + 1
                used_coins[m] = used_coins[m - coin] + [coin]
        num_coins[m] = min_coins

    return num_coins[money], *used_coins[money]


n = int(input())
count, *coins = exchange(n)
print(count)
print(*coins)


################################################################
# 2.
def exchange(money):
    coins = [1, 5, 10, 20, 50]
    prev_num_coins = [0] * (money + 1)
    curr_num_coins = [0] * (money + 1)
    used_coins = [[] for _ in range(money + 1)]

    for m in range(1, money + 1):
        min_coins = float('inf')
        for coin in coins:
            if m >= coin and prev_num_coins[m - coin] + 1 < min_coins:
                min_coins = prev_num_coins[m - coin] + 1
                used_coins[m] = used_coins[m - coin] + [coin]
        curr_num_coins[m] = min_coins
        prev_num_coins = curr_num_coins[:]

    return curr_num_coins[money], *used_coins[money]


n = int(input())
count, *coins = exchange(n)
print(count)
print(*coins)
# 3.

########################################################################
# удалить все вхождения val и вернуть длину массива
numbers = ['1', '2', '3', '1', '5', '1', '1', '8', '9']

print(numbers)
# 1    O(n)
res = []
val = '1'
for i in numbers:
    if i != val:
        res.append(i)
print(res)

# 2  O(n2)
for i in range(len(numbers)):
    i = 0
    while i < len(numbers):
        if numbers[i] == val:
            del numbers[i]
            continue
        else:
            i += 1
print(numbers)
# 3 в худшем случае O(n)

start = 0
end = len(numbers) - 1
mid = 0
while mid < end:
    if numbers[mid] != val:
        numbers[start], numbers[mid] = numbers[mid], numbers[start]
        start += 1
        mid += 1
    else:
        mid += 1

print(start)


# связные списки

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


def insert_node(node, index, value):
    head = node
    new_node = Node(value)
    if index == 0:  # если index=0 вставляем в начало
        new_node.next = None
        return new_node
    while index - 1 != 0:
        node = node.next
        index -= 1

    tmp = node.next
    node.next = new_node
    new_node.next = tmp
    return head


# n1->n2->n3->None
n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)

print(n1)  # first
print(n2)  # second
print(n3)  # third

# insert a new node in position 2
node, index, value = n1, 2, 'new_node'
head = insert_node(node, index, value)
print(head)  # first
print(head.next)  # second
print(head.next.next)  # new_node

################################################################
from queue import Queue


class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max = n
        self.head = self.tail = self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):  # добавлкение в конец
        if self.size != self.max:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max  # %self.max чтобы зациклить список певый идёт после последнего
            self.size += 1

    def get(self):  # возврат из начала
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max  #
        self.size -= 1
        return x


q = Queue(3)
q.put(1)
print(q.queue)  # [1, None, None]
q.put(2)
print(q.queue)  # [1, 2, None]
print(q.get())  # 1
print(q.queue)
q.put(3)
print(q.queue)  # [None, 2, 3]
q.put(4)  # уходит в начало списка т.к. список зациклен
print(q.queue)  # [4, 2, 3]
print(q.get())  # 2
print(q.queue)  # [4, None, 3]


################################################################

# ____2. Основные структуры данных__
# связные списки
# функция def swapNodes(self): меняет местами каждые два соседних узла
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
            self.tail = None
        self.tail = node

    def get_data(self):
        lst = []
        h = self.head
        while h:
            lst.append(h.value)
            h = h.next
        return lst

    def swapNodes(self):
        lst = self.get_data()
        # if lst[1]:
        for i in range(0, len(lst) - 1, 2):
            tmp = lst[i + 1]
            lst[i + 1] = lst[i]
            lst[i] = tmp
        return lst


lst = LinkedList()
lst.insert(Node(1))
lst.insert(Node(2))
lst.insert(Node(3))
lst.insert(Node(4))
lst.insert(Node(5))
print(*lst.get_data())  # 1 2 3 4 5
res = lst.swapNodes()
print(res)  # [2, 1, 4, 3, 5]
################################################################
# раскодировать строку n -кол-во повторений символов

string = '3[a2[b]]'  # a b b a b b a b b


# string = '2[a]3[bc]1[d]'

def dec(string):
    l = []
    for i in range(len(string) - 1):
        if string[i] not in ('[', ']', ''):
            l.append(string[i])
    # print(*l)  # 3 a 2 b
    s = ''
    for i in range(-1, -len(l) - 1, -1):  # -1,-4
        if l[i].isdigit():
            s = int(l[i]) * s
        if l[i].isalpha():
            s = l[i] + s
    return s


print(*dec(string))  # a b b a b b a b b
################################################################
string = '2[a]3[bc]1[d]'  # a a b c b c b c d


def dec(string):
    l = []
    for i in range(len(string) - 1):
        if string[i] not in ('[', ']', ''):
            l.append(string[i])
    # print(*l)  # 2 a 3 b c 1 d
    s = ''
    tmp = 0
    for i in range(-1, -len(l) - 1, -1):  # -1,-4
        if l[i].isdigit():
            s = (int(l[i]) - 1) * s[0:tmp] + s
            tmp = 0
        else:
            s = l[i] + s
            tmp += 1
    return s


print(*dec(string))  # a a b c b c b c d
################################
# 1_____смешать поочерёдно плейлист
id_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
id_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = []
# for i in zip(id_1, id_2):
#     lst.append(i[0])
#     lst.append(i[1])
for i, j in zip(id_1, id_2):
    lst.extend([i, j])
print(*lst)
################################
from itertools import chain  # модуль itertools для создания собственных итераторов


# Объединить несколько списков в один  itertools.chain(*iterables) Функция chain() модуля itertools создает итератор,
# который возвращает элементы из первой iterables, пока она не будет исчерпана, а затем переходит к
# следующей iterables, пока все итерируемые последовательности не будут исчерпаны.
# эквивалентна следующему коду:
# def chain(*iterables):
#     # chain('ABC', 'DEF') --> A B C D E F
#     for it in iterables:
#         for element in it:
#             yield element


def main():
    mix = chain(*zip(id_1, id_2))
    print(mix)  # <itertools.chain object at 0x0000025ED68DB730>
    print(' '.join(map(str, mix)))  # 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 9 19 10 20


# str.join(iterable) iterable - итерируемый объект с элементами в виде строк.

if __name__ == '__main__':
    main()


# Вызов функции main(): В конце скрипт проверяет, является ли этот модуль главным, и если да, то вызывает функцию main().
# Это обеспечивает, что функция main() будет вызвана, только если этот скрипт запущен напрямую, а не импортирован как
# модуль в другой скрипт. Если этот скрипт импортирован, функция main() не будет вызвана автоматически.

################################
def main():
    with open('input.txt') as f:
        _ = f.readline
        rus = f.readline().split()
        foregion = f.readline().split()
        mix = chain(*zip(rus, foregion))
        print(' '.join(mix))


if __name__ == '__main__':
    main()
########################################################################
# В Python существует несколько способов перевернуть строку. Рассмотрим некоторые из них:

# 1. Используя срезы (slicing):

string = "Hello, World!"
reversed_string = string[::-1]
print(reversed_string)

# # 2. Используя функцию `reversed()` и метод `join()`:
string = "Hello, World!"
reversed_string = ''.join(reversed(string))
print(reversed_string)

# 3. Используя цикл:

string = "Hello, World!"
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)  # Результат также будет "!dlroW ,olleH"
# развернуть строку

string = '12345678-9'
print(list(range(len(string) - 1, -1)))  # range(8, -1) -> []


def main(string):
    temp = ''
    for i in range(len(string) - 1, -1, -1):
        temp += string[i]
    return temp


if __name__ == '__main__':
    print(main(string))  # 987654321


##################
def reversed1(variable):
    res = []
    for i in range(len(variable) - 1, -1, -1):
        res.append(variable[i])
    res = ''.join(res)
    return res


n = reversed1(input())
print(n)
########################
str = "pythonist"  # исходная строка
reversedString = []
index = len(str)  # вычисляем длину строки и сохраняем ее в переменной index
while index > 0:
    reversedString += str[index - 1]  # сохраняем значение str[index-1] в reverseString
    index = index - 1  # уменьшаем значение index на 1
print(reversedString)  # перевернутая строка


######################
# Рекурсия Начну объяснение с конца. Если мы записали в результат все символы кроме первого, то длина оставшейся строки
# равна единице и, следовательно, ее нужно вернуть. Получаем:Но если длина строки больше одного, то нужно вернуть
# последний из ее элементов и вызвать эту же функцию, но уже отрезав последний символ. Сделать это мы можем с помощью
# среза variable[:-1]
def reversed3(variable):
    if len(variable) == 1:
        return variable
    return variable[-1] + reversed3(variable[:-1])


n = reversed3(input())
print(n)
################################################################
n = input()[::-1]  # перебираем символы с шагом -1, то есть в обратном порядке.
print(n)
###########
# развернуть строку

string = '123456789'


def main(string):
    temp = ''
    for i in range(1, len(string) + 1):
        temp += string[-i]
    return temp


if __name__ == '__main__':
    print(main(string))  # 987654321
########################################################
# 2__развернуть число numbers = '1-223-40' (если 0 в начале - не писать, учитывая отрицательные числа)

# numbers = str(input('Number: '))
# numbers = '1-223-40'
# numbers = list(numbers)

# numbers = list(map(str, input('Numbers: ').split()))
numbers = input('Numbers: ').split()  # ->list()


def main(n):
    if n in ('', '0'):
        return n
    i = 0
    while True:  # развернуть '-'
        try:
            if n[i] == '-':
                n[i], n[i + 1] = n[i + 1], n[i]
                # if n[i] == n[-1]:
                #     break
                i += 2
            i += 1
        except IndexError:
            break
    print(''.join(reversed(n)).lstrip('0'))  # -432-21


# reversed(seq) - Возвращаемое значение:обратный итератор. <reversed object at 0x0000028A30F7BC70>
# недостаточно написать res = reversed(variable), данные нужно преобразовать в нужный тип (в нашем случае - в строку).
# Сделать мы это можем при помощи метода join()
if __name__ == '__main__':
    main(numbers)


################################
# нужно по возрастанию в одной строке вывести пропущенные числа # 7 первая строка
# 6 4 1 2 3 - вторая строка.
# 7
# 6 4 1 2 3
def find_two_missing_numbers(n_1: int, n_2: map):
    """if need to optimize memory,  can do with XOR O(1) memory
    -без доп памяти (если число XOR-рить само с собой.всегда-> 0 и XOR-рить то получим пропущенную последовательность"""
    all_nums = set(range(1, n_1 + 1)) - set(n_2)  # {1, 2, 3, 4, 5, 6, 7}
    # создаем множество всех чисел от 1 до максимального числа в исходном списке. Использование множества обеспечивает
    # эффективность выполнения операции вычитания, так как оно удаляет все повторяющиеся элементы и обеспечивает
    # быстрый доступ к данным. вычитаем из первой строки вторую с помощью множества
    return all_nums


def main():
    with open('text.txt', 'r') as f:
        n_1 = int(f.readline().strip())
        n_2 = map(int, f.readline().split())
        n_missing = find_two_missing_numbers(n_1, n_2)
        print(*n_missing)  # 5 7


if __name__ == ('__main__'):
    main()


################################################################
def find_two_missing_numbers(n_1: int, n_2: map):
    all_missing_nums = set(range(1, n_1 + 1))
    for i in n_2:
        all_missing_nums.remove(i)
    return all_missing_nums


def main():
    with open('text.txt', 'r') as f:
        n_1 = int(f.readline().strip())
        n_2 = map(int, f.readline().split())
        n_missing = find_two_missing_numbers(n_1, n_2)
        print(*n_missing)  # 5 7


if __name__ == ('__main__'):
    main()
################################################################
# нужно по возрастанию в одной строке вывести пропущенные числа n_1
n_1 = 7
n_2 = 6, 4, 1, 2, 3  # tuple


def find_two_missing_numbers(n_1: int, n_2):
    all_nums = set(range(1, n_1 + 1)) - set(n_2)
    return all_nums


def main(n_1: int, n_2):
    # with open('text.txt', 'r') as f:
    # n_1 = int(f.readline().strip())
    # n_2 = map(int, f.readline().split())
    n_missing = find_two_missing_numbers(n_1, n_2)
    print(*n_missing)  # 5 7


if __name__ == ('__main__'):
    main(n_1, n_2)
################################################################
# Этот алгоритм использует свойство операции XOR (исключающее ИЛИ) для нахождения двух пропущенных чисел. Вот как он
# работает:Вычисление XOR всех чисел от 1 до n и всех чисел в списке: В этом шаге алгоритм изначально закладывается на
# идею, что если мы выполним операцию XOR для двух одинаковых чисел, мы получим 0. Если мы выполним XOR для всех чисел
# от 1 до n и всех чисел в списке, то числа, которые присутствуют и в диапазоне, и в списке, исключат друг друга
# (т.е. дадут в результате 0), оставив нам XOR-значения только для пропущенных чисел.Пример:Рассмотрим список чисел
# [1, 2, 4] с n = 5. XOR всех чисел от 1 до n (1^2^3^4^5=1) и всех чисел в списке (1^2^4=7) даст 7^1, что равно 6.
# 6 в двоичном представлении — это 110, что представляет собой XOR от 2 и 4 (двух пропущенных чисел).Нахождение любого
# 'set bit': Далее алгоритм ищет любой 'set bit' (бит, установленный в 1) в полученном XOR. 'set bit' можно найти как
# XOR & ~(XOR - 1), где ~ это оператор НЕ (инверсия битов). Бит, установленный в 1, отличает два пропущенных числа,
# то есть одно число имеет этот бит равный 1, а другое — 0.Пример:Пусть XOR равно 6 (110 в двоичном виде). Получим
# 'set bit' как 110 & ~(110 - 1) = 110 & ~(101) = 110 & 010 = 010 (второй бит — это 'set bit').Разделение чисел на
# две группы и нахождение XOR в каждой группе: Начиная с набора чисел от 1 до n и списка, алгоритм делит числа на две
# группы: те, у которых 'set bit' установлен в 1, и те, у которых 'set bit' равен 0. Затем вычисляются XOR-значения в
# каждой группе, оставляя в каждой группе XOR только одного пропущенного числа.Пример:Числа от 1 до 5 можно разделить
# на две группы: [1, 3, 5] (у которых второй бит равен 0) и [2, 4] (у которых второй бит равен 1). Затем вычислим XOR
# для каждой группы как 1^3^5=3 и 2^4=6. Теперь, если мы сделаем то же самое для списка [1, 2, 4], мы получим XOR
# групп как 1 и 6. Наконец, XOR для значений в каждой группе даст нам пропущенные числа: 3^1=2 и 6^6=0.
# Итак, в конечном итоге этот алгоритм выделяет два отсутствующих числа: 2 и 0.
################################
# нужно по возрастанию в одной строке вывести пропущенные числа n_1
n_1 = 7
n_2 = 6, 4, 1, 2, 3  # tuple
from typing import List


def find_two_missing_numbers(nums: List[int], n: int) -> List[int]:
    # Вычисление XOR всех чисел от 1 до n и всех чисел в списке
    xor = 0
    for i in range(1, n + 1):
        xor ^= i
    for num in nums:
        xor ^= num

    # Нахождение любого 'set bit'
    set_bit = xor & ~(xor - 1)

    # Разделение чисел на две группы и нахождение XOR в каждой группе
    missing_nums = [0, 0]
    for i in range(1, n + 1):
        if i & set_bit:
            missing_nums[0] ^= i
        else:
            missing_nums[1] ^= i
    for num in nums:
        if num & set_bit:
            missing_nums[0] ^= num
        else:
            missing_nums[1] ^= num

    return missing_nums


print(*find_two_missing_numbers(n_2, n_1))
################################
# в первой строке n бактерий. В следующих n строках 4 числа:номер бактерии, количество прожитых часов, номера двух её
# потомков. Если номер потомка -1 значит нет потомка. Нужно вывести среднюю продолжительность жизни на каждом уровне, до
# двух знаков после запятоой
from collections import defaultdict


# 7
# 1 1 2 3
# 2 2 4 5
# 3 3 6 -1
# 4 4 7 -1
# 5 5 -1 -1
# 6 6 -1 -1
# 7 7 -1 -1

def main():
    levels_to_weight = defaultdict(list)
    levels = []  # 0 1 1 2 2 2 3
    parents = {}  # {1:0,2:0,3:1,4:1,5:2,6:3}
    with open('text.txt') as f:
        n = int(f.readline().strip())  # 1-я строка кол-во всех бактерий
        for i in range(n):
            _, h, a, b = map(int, f.readline().split())  # _ -№ бактерии игнорируется т.к тспользуем i вместо №,
            # h-часы, a, b - № потомков
            if i != 0:  # Если бактерия не является корневой (т.е. i != 0), уровнем бактерии становится уровень ее
                # родителя, увеличенный на 1.
                lvl = levels[parents[i]] + 1  # номер уровня для текущей бактерии i
                levels.append(lvl)  # levels будет хранить уровень для каждой бактерии (где уровень родительской
                # бактерии переносится на всех её потомков).
                # И также levels - это список, где каждому элементу соот. уровень (level) бактерии с тем же индексом.
            # Таким образом, для текущей бактерии с номером i, parents[i] дает номер ее родительской бактерии.
            # Выражение levels[parents[i]] используется для получения уровня (level) родительской бактерии, а затем
            # прибавляется 1, чтобы получить уровень текущей бактерии.В итоге, lvl будет содержать уровень бактерии i,
            # который затем используется для сохранения информации о средней продолжительности жизни на каждом уровне.
            else:  # root level
                lvl = 0
                levels.append(lvl)  # список, где каждому элементу соответствует уровень (level) бактерии с тем же индек

            levels_to_weight[lvl].append(h)  # dict{ lvl : h....} где ключами являются уровни, добавляется
            # продолжительность жизни каждой бактерии.т.е. кол-во часов для данного уровня [1,2,3...]
            if a != -1:
                parents[a - 1] = i  # записи о этих потомках и их родителе. словарь, в котором ключами являются номера
            # потомков, а значениями - номера их родительских бактерий.
            #  используете переменную i для указания родительской бактерии
            #  (т.е. текущую бактерию в текущей итерации), и a и b - номера её потомков.
            #  бактерия с номером a - 1 имеет родителя i. Вычитание 1 из a в a - 1 связано с тем, что в Python
            #  индексация элементов начинается с 0, а не с 1, а по условию задачи бактерии нумеруются начиная с 1.
            if b != -1:
                parents[b - 1] = i

    for lvl, weight in levels_to_weight.items():
        avl_weight = sum(weight) / len(weight)
        print(f'{avl_weight:.2f}', end=' ')


if __name__ == '__main__':
    main()

################################################################
# НАйти сымый часто встречающийся смимвол в строке, если несколько символов встречаются одинаковло часто вывести любой
# 1. O(n^2)
string = 'abaaba'

count = 0
simbol = ''
for i in range(len(string)):
    cur = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            cur += 1
            if cur > count:
                count = cur
                simbol = string[j]

print(simbol)  # a

# 2. O(n^2)
string = 'abaaba'
s = string
print(max(map(lambda x: (s.count(x), x), s))[1])  # a
# lambda, которая возвращает пару значений: количество вхождений этого элемента в строку s (s.count(x)) и сам элемент
# x. map возвращает итератор со всеми этими парами значений.max(...) - мы выбираем максимальное значение из всех пар
# значений. Если есть две или более пар со значением подсчета, равным максимальному, выбирается та, которая встречается
# позже, потому что max возвращает последнее максимальное значение в случае равенства.
# [1] at the end of the expression is used to access the second item of the returned tuple, which is the character
print(max(map(lambda x: (s.count(x), x), s)))  # (4, 'a')
# Если бы вы хотели сортировать по количеству повторений, но в обратном порядке,
# вы бы использовали key=lambda x: -int(x[0]). Однако, в данном контексте это не требуется.

# 3.
# НАйти сымый часто встречающийся смимвол в строке, если несколько символов встречаются одинаковло часто вывести любой
# O(N+K) k<N -> O(N)
string = 'ccafffxxvvvvvvvxxccc'
d = dict()
max_simbol = ''
max_cur = 0
for i in string:
    # mac_cur = 0
    if i not in d:
        d[i] = 0
    d[i] += 1

for key in d:
    if d[key] > max_cur:
        max_cur = d[key]
        max_simbol = key
print(d)  # {'c': 5, 'a': 1, 'f': 3, 'x': 4, 'v': 7}
print(max_simbol)  # v
################################################
d = dict()
max_simbol = ''
max_cur = 0
for i in string:
    if i not in d:
        d[i] = 0
    d[i] += 1

    if d[i] > max_cur:
        max_simbol = i
        max_cur = d[i]


################################
# 1. дана последовательность чисел ,найти первое левое положитеольное вхождение числа или вывести -1 если его нет
def function(seq, x):
    ans = -1
    for i in seq:
        if ans == -1 and i == x: ans = i
    return num


################################
# 2.
def function(seq, x):
    for i in seq:
        if ans == -1 and i == x: return i
    return -1


# 1. дана последовательность чисел ,найти последнее (правое) вхождение числа или вывести -1 если его нет
def function(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = seq[i]
    return ans


# 2 Дана последовательность  чисел длиной N>0.Найти максимаьное число
import math


def func(seq):
    # ans = -math.inf
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


################################################################
# 3 Дана последовательность  чисел длиной N>0.Найти максимаьное число
# более универсальный чтобы не пришлось копировать каждый раз в случае если будут использоваться строки,
# т.к. это займёт больше времени для других языков кроме Питона
# поэтому использовать ссылку на индекс объекта
def func(seq):
    ans = 0  # index sequence
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]


################################################################
# Дана последовательность  чисел длиной N>1. Найти макс число и второе по величине (такое кот будет макс
# если вычеркнуть из последовательности одно максимальное число)
# 1. O(n) / O(1) memory меньше всего из других вариантов
# задать первые 2 эл. макс1 и макс2 ->перебрать последовальность начиная с 3 эл. сравнивая с макс1 и макс2
def largest_two(seq):
    max_1 = max(seq[0], seq[1])
    max_2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if max_1 < seq[i]:
            max_2 = max_1
            max_1 = seq[i]
        elif max_2 < seq[i]:  # если вместо elif написать if то после первого if (if max_1 < seq[i]:)
            # max_2 сдесь перезапишется
            max_2 = seq[i]
    return max_1, max_2


################################
def largest_two(seq):
    max_1, max_2 = seq[:2]
    if max_1 < max_2:
        max_1, max_2 = max_2, max_1
    for i inn in range(2, len(seq)):
        if seq[i] > max_1:
            max_1, max_2 = seq[i], max_1
        elif seq[i] > max_2:
            max_2 = seq[i]
    return max_1, max_2


################################################################
# 2 . Найти макс1 скопировать список- удалить оттуда макс1 - найти там макс2
def double_two(seq):
    max_1 = max(seq)
    # copy_lst = list(seq)
    copy_lst = seq.copy()
    copy_lst.remove(max_1)
    return max_1, max(copy_lst)


################################
# 3. найти макс1 и его индекс - убрать его найти макс2 и вставить обратно макс1 прежний индекс
def mutable_two(seq):
    ind = max(range(len(seq)), key=seq.__getitem__)  # в key передаются индексы от range->0,1,2,.. идёт обращение в
    # seq.__getitem__ по индексу ч/з __getitem__ для того чтобы перебрать seq[i] и из значений seq выбрать индекс
    # соответсвующий макс элементу, т.е. вернёт индекс
    max_1 = seq[ind]
    del seq[ind]
    # seq.remove(max_1)
    max_2 = max(seq)
    seq.insert(ind, max_1)  # обратно вернули значение
    return max_1, max_2


################################
# 4.создать новый отсортированный список и взять 2 крайних значения
def sorting_two(seq):
    return tuple(sorted(seq, reverse=True)[:2])


################################
def sorting_two(seq):
    return tuple(sorted(seq)[-2:])


################################
def find_max_and_second_max(arr):
    if len(arr) < 2:
        return None, None

    max_num = float('-inf')  # неправильно если пустой [] то выдаст float('-inf')
    second_max_num = float('-inf')

    for num in arr:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num

    return max_num, second_max_num


################################################################
# Дана последовательность  чисел длиной N. Найти мин чётное число в последовательности или вывести -1,если егоdef

def f(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or ans > seq[i]):
            ans = seq[i]
    return ans


################################################################

def f(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or ans > seq[i]):
            ans = seq[i]
            flag = True
    return ans


################################################################
def find_min_even_number(sequence):
    min_even = float('inf')  # Используем бесконечность как начальное значение минимального четного числа

    for num in sequence:
        if num % 2 == 0 and num < min_even:
            min_even = num

    if min_even == float('inf'):
        return -1
    else:
        return min_even


################################################################
# Дана последовательность  слов . Вывести самые короткие через пробел
seq = 'Дана ff последовательность  слов ff Вывести ff aa bb самые короткие через пробел'


def f(string):
    seq = string.split()
    ans = [0]
    for i in range(1, len(seq)):
        if len(seq[i]) < len(seq[ans[0]]):
            ans = [i]
        elif len(seq[i]) == len(seq[ans[0]]):
            ans.append(i)
    return (seq[i] for i in ans)


print(*f(seq))  # ff ff ff aa bb


################################################################`
##2.
def f(string):
    seq = string.split()
    ans = [seq[0]]
    for i in range(1, len(seq)):
        if len(seq[i]) < len(ans[0]):
            ans = [seq[i]]
        elif len(seq[i]) == len(ans[0]):
            ans.append(seq[i])
    return ' '.join(ans)


print(f(seq))  # ff ff ff aa bb
################################################################
# 3/
# Дана последовательность  слов . Вывести самые короткие через пробел
seq = 'Дана ff слов ff Вывести ff aa bb '


def f(string):
    seq = string.split()
    min_len = len(seq[0])
    for i in seq:  # найти мин длину слов
        if len(i) < min_len:
            min_len = len(i)
    ans = []
    for j in seq:
        if len(j) == min_len:
            ans.append(j)

    return ' '.join(ans)


print(f(seq))


############################################################ ####
# В двумерном мире из блоков 1х1 метр. Остров - набор столбцов  состоящий из блоков. Над островом прошёл дождь
# и заполнил низины, сколько воды (блоков) осталось заполненными водой

def isleflood(h):
    # найти макс позицию и поделим остров пополам
    max_pos = 0
    for i in range(len(h)):
        if max_pos < h[i]:
            max_pos = i
    ans = 0
    now_max = 0
    # обойти обе половинки острова
    for i in max_pos:
        if now_max < h[i]:
            now_max = i
            ans += now_max - h[i]  # вычитаем и получаем пустые пространства занятые водой
    now_max = 0
    # теперь обход справа на лево в обратку
    for i in range(len(h - 1), max_pos, -1):
        if now_max < h[i]:
            now_max = i
            ans += now_max - h[i]
    return ans


################################################################
# Дана строка состоящая из букв A-Za-z. Написать функцию RLE которая на выходе даст ANBM..(N-кол-во повторений А
# M-КОЛ-во повторов B если символ встречается более одного раза к нему добавляется ко-во повторов) и сгенерит ошибку
# если пришла невалидная строка
# 1.
string = 'eAADDC'


def func(string):
    d = {i: 0 for i in set(string)}
    for i in string:
        d[i] += 1
    v = []
    for i in d.items():
        if i[1] == 1:
            v.append(i[0])
        else:
            v.append(i[0] + str(i[1]))
    return ''.join(v)


print(func(string))


################################################################
def func(string):
    d = {i: 0 for i in set(string)}
    for i in string:
        d[i] += 1
    lst = []
    for k, v in d.items():
        if v == 1:
            lst.append(''.join([k]))
        else:
            lst.append(''.join([k, str(v)]))
    return ''.join(lst)


################################
def rle(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    result = ''  # строку лучше не использовать т.к будет увечение времени алгоритма из-за того что она будет при каждом
    # проходе создаваться заново, лучше list
    for k, v in sorted(d.items(), key=lambda x: x[1]):  # сортировка по возрастанию значений
        # dict_items([('e', 4), ('A', 2), ('D', 2), ('C', 1)])
        if v == 1:
            result += k
        else:
            result += k + str(v)
    return result


################################################################
# не совсем верно если символы повторяются далее по тексту
string = 'eeAADDCee'


def rle(string):
    def pack(string, count):
        if count > 1:
            return string + str(count)
        return string  # если один символ то не пишем 1

    lastsym = string[0]
    last_pos = 0
    ans = []
    for i in range(len(string)):
        if string[i] != lastsym:
            ans.append(pack(lastsym, i - last_pos))  # i - last_pos -кол-во символов подряд
            last_pos = i
            lastsym = string[i]

    ans.append(pack(string[last_pos], len(string) - last_pos))
    return ''.join(ans)


print(rle(string))  # e2A2D2Ce2
################################################################
# проверить сможет ли кирпич размерами axbxc м  пролезти в проём размером dxe м.

a = 3
b = 2
c = 1
d = 5
e = 4
l = [c, b, a]
min_n = 0
for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

a, b = l[:2]
# d, e = (d, e) if d < e else (e, d)
# Это приводит к ошибке, потому что в Python оператор if имеет меньший приоритет, чем оператор присвоения (=). Однако,
# есть два возможных варианта корректного использования этого выражения:# Использовать скобки для каждого из кортежей:
# d, e = (d, e) if d < e else (e, d)
# Или использовать только один набор скобок:# (d, e) = d, e if d < e else e, d
# Оба этих варианта корректно работают, так как они задают необходимые приоритеты и соблюдают правило Python о
# распаковке значений.

d, e = (d, e) if d < e else (e, d)
print(d, e)
if a <= d and b <= e:
    print('yes')
else:
    print('no')
################################################################
import itertools


def check_brick_fit(a, b, c, d, e):
    # itertools.permutations([a, b, c], 3) автоматически создаст все возможные перестановки размеров кирпича.
    # Функция permutations() модуля itertools возвращает итератор с последовательными перестановками из элементов
    # входной последовательности iterable. Каждая комбинация заключена в кортеж с длинной r элементов.
    # Если r не указано или None, тогда по умолчанию r равна длине iterable и генерируются все возможные
    # перестановки полной длины.
    # Количество возвращенных сочетаний равно n! / (n-r)! если 0 <= r <= n или ноль если r > n.
    # orientations = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
    orientations = list(itertools.permutations([a, b, c], 3))

    for i in orientations:  # Проверяем, сможет ли кирпич пролезть в проём по каждой оси
        if i[0] <= d and i[1] <= e:
            return True
    return False


brick_size = (a, b, c)  # Размеры кирпича [3,2,1]
opening_size = (d, e)  # Размеры проёма [5,4]

if check_brick_fit(*brick_size, *opening_size):
    print("Кирпич пролезет в проём.")
else:
    print("Кирпич не пролезет в проём.")
################################################################
# человек ждёт поезда которые приходят на 1-й платформе с интервалом a и стоят 1 мин на 2-й платформе интервал b и
# стоят 1 мин.
# на 1-й платформе челевек увидел n поездов на 2-й m поездов. Сколько максимально и минимально времени он стоял?
# min_a = a * (n - 1) + n  # +n - одна минута прежде чем увидел последний поезд
# аналогично
min_a = (a - 1) * (n - 1) + n  #
max_a = min_a + 2 * a  # 2*a - 2 поезда по краям в начале и в конце если он стоял всё время

min_b = (b - 1) * (n - 1) + n
max_b = min_b + 2 * b

min_time = max(min_a, min_b)
max_time = min(max_a, max_b)
if min_time > max_time:
    print(-1)
else:
    print(min_time, max_time)
################################################################
# В доме есть квартира к2 в подъезде р2 на этаже n2. В доме M этажей и количество квартир на каждой площадке одинаково.
# написать программу вычисляющую подъезд р2 и номер этажа n2 если известна квартира к1. числа до 10^6

M = int(input("Введите количество этажей в доме: "))  # Вводим количество этажей в доме
k1 = int(input("Введите номер квартиры k1: "))  # Вводим номер исходной квартиры k1

apartments_per_floor = k1 // M  # Количество квартир на каждом этаже

entrance = (k1 - 1) // (apartments_per_floor * M) + 1  # Вычисляем подъезд
floor = ((k1 - 1) // apartments_per_floor) % M + 1  # Вычисляем этаж

print(f"Подъезд: р{entrance}, Этаж: n{floor}")


################################################################
# Необходимо определить, является ли это слово палиндромом (одинаково читается вперед и назад, например, АННА).
# Палиндром — это когда строка или число одинаково читается в прямом и обратном направлении:
def polindrom(word):
    return 'Yes' if word == word[::-1] else 'No'


#
def polindrom(word):
    w = []
    for i in range(len(word) - 1, -1, -1):
        w.append(word[i])
    return w == word


#
def polindrom(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


#
def polindrom(word):
    s1 = word[:len(word) // 2]
    s2 = word[(len(word) - len(word) // 2):]
    return s1 == ''.join(reversed(s2))


################################
# Дана последовательность чисел. Определить какое минимальное количество и каких чисел надо прописать в конец этой
# последовательности, чтобы она стала симметричной

# берём до той части строки которая является полиндромом
# ищет самую длинную суффиксную подпоследовательность, являющуюся палиндромом. Затем он добавляет до нее оставшиеся
# числа в обратном порядке в конец исходной последовательности. Этот алгоритм эффективно работает в случаях, когда у
# последовательности имеется большой палиндромический суффикс.
def make_symmetric(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        while i < len(seq) and j >= 0 and seq[i] == seq[j] and i <= j:  # двигаемся навстречу пока вып-ся усл
            i += 1  # сдвигаем указатели
            j -= 1
        if i > j:  # i=5>3=j значит мы успешно прошли по полиндрому, полиндром между i и j, т.е. мы сдвигали i и j пока
            # выполнялось  условие seq[i] == seq[j] and i <= j..
            ans = []  # берём значения до start т.е. до той части строки которая явл. полиндромом
            for i in range(start - 1, -1, -1):  # range(start-1=4-1=  3,-1,-1) перебор инд-в с инд=3 до 0 в обратку
                ans.append(seq[i])
            return seq + ans  # [1 2 3 4 5] + [4 3 2 1]


seq = [1, 2, 3, 4, 5]

print(*make_symmetric(seq))  # 1 2 3 4 5 4 3 2 1
print(len(make_symmetric(seq)))


################################################################№№№№№
# 2. не всегда работает верно______
# полиндром = просто сравнивает элементы от начала и конца последовательности. При нахождении несоответствующих пар,
# он добавляет элемент с конца последовательности в ее конец. Это продолжается до середины списка. Однако второй
# алгоритм не является кошерным для задачи, поскольку он может добавлять числа в конец даже в том случае, когда это
# ненужно
def make_sequence_symmetric(sequence):
    n = len(sequence)
    i = 0
    while i < n // 2:
        if sequence[i] != sequence[n - i - 1]:
            sequence.append(sequence[n - i - 1])
        i += 1
    return sequence


seq = [1, 2, 3, 4, 5]
symmetric_seq = make_sequence_symmetric(seq)
print(symmetric_seq)
# Этот код определяет функцию make_sequence_symmetric, которая принимает последовательность чисел sequence и добавляет
# недостающие числа в конец последовательности, чтобы сделать ее симметричной. Функция проходит по первой половине
# последовательности и сравнивает элементы с их зеркальными отражениями. Если элементы не совпадают, то зеркальное
# отражение добавляется в конец последовательности.

################################################################
# В списке целых чисел найти три числа, произведение которых максимально
# сложностью O(n), вывести эти три числа
# 1. отсортировать. 2 варианта 1-произведение 3-х последних. либо произведение 2-х наименьших отрицательных на одно
# максимальное
l = [4, 5, 6, -1, -7, -9, 7]
l.sort()  # [-9, -7, -1, 4, 5, 6, 7]
if l[0] * l[1] * l[-1] > l[-1] * l[-2] * l[-3]:
    print(l[0] * l[1] * l[-1])  # if all numbers are negative
else:
    print(l[-1] * l[-2] * l[-3])  # 9*7*7=441
################################################################
# 2/
l = [4, 5, 6, -1, -7, -9, 7]


def find_max_product(numbers):
    if len(numbers) < 3:
        return None

    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in numbers:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    product1 = max1 * max2 * max3
    product2 = max1 * min1 * min2

    if product1 > product2:
        return max1, max2, max3
    else:
        return max1, min1, min2


numbers = [1, 2, 3, 4, 5]
result = find_max_product(l)
print(result)  # (7, -9, -7)


################################################################
# https://new.contest.yandex.ru/42734/problem?id=215/2022_11_08/wGEXsFgrcB
# Максимальное произведение
# Дана последовательность неотрицательных целых чисел
# Вычислите max произведение , числа должны быть разные
def max_pairwise_product(seq):
    max_1 = seq[0]
    max_2 = seq[1]
    if max_1 < max_2:
        max_1 = seq[1]
        max_2 = seq[0]

    for i in range(2, len(seq)):
        if max_1 < seq[i]:
            max_2 = max_1
            max_1 = seq[i]
        elif max_2 < seq[i]:
            max_2 = seq[i]

    return max_1 * max_2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    # seq = [1, 2, 3]
    print(max_pairwise_product(input_numbers))
# seq = [7, 5, 14, 2, 8, 8, 10, 1, 2, 3]
# print(max_num(seq))
################################
# 2.
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
max_product = a[0] * a[1]
print(max_product)


################################
# Максимальное произведение — контрпример
# Рассмотрим псевдокод поиска двух максимальных элементов массива:Определите, можно ли построить такой пример
# входных данных, чтобы количество сравнений в алгоритме MaxPairwiseProduct было больше 1.5.Формат ввода
# Целое число n.Ограничения: 2≤n≤200000 Формат вывода В единственной строке выведите No, если подходящих входных
# данных не существует. Иначе в первой строке выведите Yes, а во второй строке �n чисел �1,�2,…,��a1,a2,…,an
# (0≤��≤2000000≤ai≤200000) — найденный контрпример.Если походящих последовательностей несколько, выведите любую из них.

def max_pairwise_product(seq):
    max_1, max_2 = seq[0], seq[1]
    c = 0
    if max_1 < max_2:
        max_1, max_2 = max_2, max_1
        c += 1

    for i in range(2, len(seq)):
        if max_1 < seq[i]:
            max_2 = max_1
            max_1 = seq[i]
            c += 2
        elif max_2 < seq[i]:
            max_2 = seq[i]
            c += 1
    return c
    # return max_1 * max_2


if __name__ == '__main__':
    n = int(input())
    seq = [i for i in range(1, n + 1)]
    count = max_pairwise_product(seq)
    seq.insert(0, seq.pop())
    if count > (1.5 * n):
        print('Yes')  # при n > 6 т.е. от 7....
        print(' '.join(str(i) for i in seq))
    else:
        print('No')


# Оценим количество сравнений в алгоритме. Количество сравнений в первом if-условии (m2 > m1) равно 1.
# Количество сравнений во втором if-условии (A[i] > m1) равно n-2. Количество сравнений внутри else-условия равно n-2.
# Итого количество сравнений равно 1 + (n-2) + (n-2) = 2n-3. Чтобы количество сравнений было больше 1.5n, необходимо
# выполнение неравенства 2n-3 > 1.5n. Решим это неравенство: 2n-3 > 1.5n 2n > 3
# n > 6 То есть, количество элементов массива должно быть больше 6.
########################################################################
##########################################################
# maximum prodact of 4 numbers
def max_product(nums):
    # Убедимся, что список чисел содержит по крайней мере 4 элемента
    if len(nums) < 4:
        return None

    # Отсортируем список в порядке возрастания
    nums.sort()

    # Максимальное произведение четырех чисел будет либо
    # произведение четырех самых больших чисел, либо
    # произведение двух наименьших чисел и двух самых больших чисел.
    return max(nums[0] * nums[1] * nums[2] * nums[3], nums[-1] * nums[-2] * nums[-3] * nums[-4],
               nums[0] * nums[1] * nums[-1] * nums[-2])


n = int(input())
l = list(map(int, input().split()))
print(max_product(l))


################################################################
# Дана последовательность положительных чисел длиной N и число x. найти два различных числа а и б из
# последовательности чтобы а+б=x или вернуть 0,0

def find_pair(nums, x):
    seen = set()  # Создаем set для хранения уже просмотренных чисел, set() чтобы числа были различные и не повторялись
    for a in nums:
        b = x - a  # Вычисляем разность между искомой суммой и текущим числом
        if b in seen:  # Если такая разность уже была просмотрена, то значит нашли пару чисел
            return a, b
        seen.add(a)  # Добавляем текущее число в множество просмотренных
    return 0, 0  # Если не найдено пару чисел, возвращаем (0, 0)


sequence = [1, 2, 3, 4, 5]
x = 6
a, b = find_pair(sequence, x)
print(a, b)


################################################################################################
def nums(nums, x):
    previous = set()
    for i in nums:
        if x - i in previous:
            return i, x - 1
        previous.add(i)
    return 0, 0


################################################################
# Дан словарь из N слов. длина каждого не превосходит K.
# В запаиси каждого из M слов текста(каждое длиний до K) может быть пропущена одна буква.
# Для каждого слова сказать входит ли оно (возможно с одной пропущенной буквой) в словарь
# 1/
def find_word(dictionary, text):
    word_set = set(dictionary)

    for word in text:
        for w_indx in range(len(word)):
            word_set.add(word[:w_indx] + word[w_indx + 1:])

    ans = []
    for word in text:
        ans.append(word in word_set)
    return ans


# 2/
def word_in_dictionary(dictionary, word):
    # Проверка, входит ли слово в словарь без пропущенной буквы
    if word in dictionary:
        return True

    # Проверка, входит ли слово в словарь с одной пропущенной буквой
    for i in range(len(word)):
        # Удаление i-й буквы из слова
        edited_word = word[:i] + word[i + 1:]
        if edited_word in dictionary:
            return True

    return False


def check_words_in_dictionary(dictionary, text):
    result = []
    for word in text:
        is_in_dictionary = word_in_dictionary(dictionary, word)
        result.append(is_in_dictionary)
    return result


dictionary = {'apple', 'banana', 'cherry', 'date'}
text = ['apple', 'banan', 'chery', 'data']
result = check_words_in_dictionary(dictionary, text)
print(result)  # [True, False, False, False]


################################################################
# на шахматной доске NxN M ладей. Сколько пар ладей бьют друг друга (ладьи задаются координатами)
# посказка количество пар считается - из общего количества ладей по вертикали / горизонтали минус 1

def count_rook(coords):
    def addcolrow(d_colrow, key):  # запись в столбец/строку ладей
        if key not in d_colrow:
            d_colrow[key] = 0
        d_colrow[key] += 1

    def count_pairs(d_colrow):
        pairs = 0
        for key in d_colrow:
            pairs += d_colrow[key] - 1  # количество пар -1
        return pairs

    d_col = {}
    d_row = {}
    for row, col in coords:
        addcolrow(d_row, row)
        addcolrow(d_col, col)
    return count_pairs(d_col) + count_pairs(d_row)  # сумма по столбцам и строкам


coords = [(2, 4), (2, 3), (4, 5), (7, 7)]
print(count_rook(coords))  # 1


################################################################
# Сгруппировать слова по общим буквам
# вывести в виде сгруппированных списков

def group_words(words):
    groups = {}
    for word in words:
        key_sort_word = ''.join(sorted(word))  # отсортировать каждый раз слово и сравнить с ключом
        if key_sort_word not in groups:
            groups[key_sort_word] = []
        groups[key_sort_word].append(word)

    return list(groups.values())
    # ans = []
    # for sort_word in groups:
    #     ans.append(groups[sort_word])  # добавить значения
    # return ans


# 2/
def group_words(words):
    groups = {}

    def sort_key(word) -> str:  # считает сколько раз каждого символав слове: a1b3d4 из bbbadddd
        symcnt = {}
        for sym in words:
            if sym not in symcnt:
                symcnt[sym] = 0
            symcnt[sym] += 1
        lst = []
        for sym in sorted(symcnt.keys()):
            lst.append(sym)  # a
            lst.append(symcnt[sym])  # 1
        return ''.join(lst)  # 'a1b3d4'

    for word in words:
        key_sort_word = sort_key(word)  # 'a1b3d4'
        if key_sort_word not in groups:
            groups[key_sort_word] = []
        groups[key_sort_word].append(word)

    ans = []
    for sort_word in groups:
        ans.append(groups[sort_word])  #
    return ans


# 2/

################################################################
# Префиксные суммы
# реализация ч/з RAQ
def maked_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    return prefix


################################################################
# последовательность чисел длиной N и M запросов. Запросы:сколько нулей на полуинтервале [L,R]
# подсказка для каждого префикса посчитаем количество нулей
def maked_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = prefix[i - 1]

    return prefix


def countzero(maked_prefix, l, r):
    return maked_prefix(r) - maked_prefix(l)


################################################################
# алгоритм бинарного поиска

def binarysearch(arr, x, left, right):
    if right >= left:
        mid = left + (right - left) // 2  # indx
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, x, left, mid - 1)
        else:
            return binarysearch(arr, x, mid + 1, right)
    else:
        return -1


arr = [2, 3, 5, 6, 7, 3, 4, 5, 6, 7]
x = 7
print(binarysearch(arr, x, left=0, right=len(arr) - 1))  # indx


################################################################
# дана отсортированная последоввательность  длиной N и число K.
# найти количество пар чисел А и В таких что В-А > K.


def cnt_pairs(nums, k):
    pairs = 0
    last = 0
    for i in range(len(nums)):
        while last < len(nums) and nums[last] - nums[i] <= k:
            last += 1
        pairs += len(nums) - last
    return pairs


# 2
def count_pairs(numbers, k):
    count = 0
    i = 0
    j = 1
    while j < len(numbers):
        if numbers[j] - numbers[i] > k:
            count += (len(numbers) - j)
            i += 1
        else:
            j += 1
    return count


# Пример использования
numbers = [1, 3, 5, 7, 9]
k = 2
result = count_pairs(numbers, k)
print(result)


# Вывод: 6
################################################################
# Футбол - команда сплоченная если проф сумма любых двух игроков больше професионализма любого из сильных игроков.
# найти макс суммарный профессионализм коменды из отсртированной последовательности профессионализма


def beast_team(players):
    last, now_sum, best_sum = 0, 0, 0

    for first in range(len(players)):
        while last < len(players) and (first == last or players[first] + players[first + 1] >= players[last]):
            now_sum += players[first] + players[first + 1]
            last += 1
        best_sum = max(best_sum, now_sum)
        now_sum -= players[first]
    return best_sum


l = [1, 1, 3, 3, 4, 8, 9, 10, 12]
print(beast_team(l))


# Операция now_sum -= players[first] выполняется для того, чтобы исключить первого игрока из текущей суммы now_sum и
# перейти к следующему возможному сочетанию игроков.Если мы просто присвоим now_sum = 0, то мы будем начинать
# суммирование с самого начала каждый раз после исключения текущего игрока. Это означает, что мы будем учитывать
# только одиночные игроки, а не все возможные комбинации двух игроков.Поэтому операция now_sum -= players[first]
# позволяет нам "сдвигать" начало суммирования на следующего возможного игрока, чтобы учесть все комбинации двух
# игроков. Это позволяет найти команду с максимальной суммой профессионализма.

################################################################
# даны две отсортированные последоватеотности чисел. Трубуется слить их в одну

def merge(nums_1, nums_2):
    merged = [0] * (len(nums_1) + len(nums_2))
    first_1 = first_2 = 0
    for i in range(len(nums_1) + len(nums_2)):
        if first_1 != len(nums_1) and (first_2 == len(nums_2) or nums_1[first_1] <= nums_2[first_2]):
            merged[i] = nums_1[first_1]
            first_1 += 1
        else:
            merged[i] = nums_2[first_2]
            first_2 += 1

    return merged


# 2.
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)


################################################################
# левый бинарный поиск
def left_binsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2  # скругление вниз
        if check(m, checkparams):
            r = m
        else:
            l = m + 1

    return l


################################################################################
# в управляющий совет входят родители , учителя и учениеки, причём родителей должно быть не менее 1/3.
# Определить сколько родителей минимально нужно добавить чтобы их было не менее трети. Дано N-человек всего
# из них K-родителей.
def bin_search(N, K):
    l = 0
    r = N  # количество родителей, которых необходимо добавить
    while l < r:
        mid = (l + r) // 2  # добавить кол-во родителей
        if (N + mid) <= 3 * (K + mid):  # 3* чтобы избежать деления и получения float при делении на 3
            r = mid
        else:
            l = mid + 1

    return l


N = 100
K = 20
print(bin_search(N, K))  # 20
################################################################
# В первый день К задач а далее на 1 больше. Сколько дней уйдёт на N задач.
n = 10
k = 2


def left_binsearch(l, r, check, n, k):
    while l < r:
        m = (l + r) // 2
        if check(m, n, k):
            r = m
        else:
            l = m + 1
    return l


def check(days, n, k):
    return (k + (k + days - 1)) * days // 2 >= n


print(left_binsearch(0, n, check, n, k))  # 4


# 2/
def not_bi(n, k):
    count = 1
    s = k
    while s <= n:
        k += 1
        s += k
        count += 1

    return count


print(not_bi(n, k))
################################################################
# Сайт поселило N челеовек для каждого t_in t_out включительно. Определить суммарное аремя на сайте хотя бы
# одного человека

def time_visitors(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))  # -1 приход
        events.append((t_out[i], 1))  # 1 выход
    events.sort()  # sort events по t_in , t_out
    online = 0  # кол-во
    note_time = 0  # продолжительность
    for i in range(len(events)):
        if online > 0:  # если кто-то есть
            note_time += events[i][0] - events[i - 1][0]  # добавить промежуток от предыдущего события
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return note_time

################################################################
########################################################################################
# Тренировки по алгоритмам 2.0

################################################################
# Определиьт мин кол-во станций метро туда и обратно при поездках

n, i, j = map(int, input().split())
dist_1 = abc(j - 1) - 1
dist_2 = n - 2 - dist_1
print(min(dist_1, dist_2))

################################################################
# Определить мин суммарное расстояние которое проезжют ученики. Дома по прямой, даны координаты и число учеников
coord = list(map(int, input().split()))
n = int(input())
coord_school = coord[len(coord) // 2]

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################


################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################