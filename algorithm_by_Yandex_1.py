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
    print(l[0] * l[1] * l[-1])
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
