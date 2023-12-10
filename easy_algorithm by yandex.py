#https://new.contest.yandex.ru/42734/problem?id=215/2022_11_08/wGEXsFgrcB
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
#2.
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
































