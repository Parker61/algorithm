# ______________2.1 Статический массив
################################################################
# Подвиг 5. Пусть некоторый статический массив с именем ar_d хранит наборы чисел:
ar_d = [1, 2, -5, 0, 100, 1, 5, 20]
# Выберите правильный вариант записи оператора для обращения к числу 100 этого массива.
ar_d[4]
############################################
# Подвиг 6. Пусть имеется следующий статический массив с именем ar_s, который хранит строку:
# ar_s = "Структуры данных"# Какому символу соответствует адрес: ar_s + 7
# p_j = ar + j ∙ k

ar_s = "Структуры данных"
print(ar_s[7])  # р

# ______________________  стек  _____типа LIFO_____________________
# Пример использования стека ч/з list.append() / list.pop()

a = input("Введите строку: ")
stack = []
flVerify = True

for lt in a:
    if lt in "([{":
        stack.append(lt)
    elif lt in ")]}":
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:  # стек по итогам проверок должен быть пустым
    print("Yes")
else:
    print("No")

################################################################
# __________________4.2 Очередь collections.deque____FIFO________________
# Подвиг 4. Создайте пустую очередь с именем q как объект класса deque. Добавьте справа (в конец) очереди q
# последовательно данные lst_in, прочитанные из входного потока:lst_in = list(map(int, input().split()))
# Извлеките слева (с начала) очереди первые три элемента и выведите их в консоль в одну строчку через пробел в
# порядке считывания.

from collections import deque

q = deque()
lst_in = list(map(int, input().split()))
q.extend(lst_in)
[print(q.popleft(), end=' ') for i in range(3)]
################################################################
lst_in = list(map(int, input().split()))
q = __import__("collections").deque(lst_in)
print(*[q.popleft() for i in range(3)])
################################################################
# Подвиг 5. Создайте очередь с именем q как объект класса deque и следующими начальными данными:
# lst_in = list(map(str.strip, input().split()))
# Данные в очереди q должны идти в том же порядке, что и в списке lst_in (это равносильно тому, что значения из
# списка lst_in добавляются в конец (справа) очереди q).Вставьте в очередь q элемент со строкой "run" в третью
# позицию (позиции отсчитываются с единицы). Удалите из этой очереди первый найденный элемент со строкой "edit".
from collections import deque

q = deque()
lst_in = list(map(str.strip, input().split()))
[q.append(i) for i in lst_in]
q.insert(3, "run")
q.remove("edit")
################################################################
# Подвиг 6. С помощью класса deque создайте объект очереди с именем fifo. Затем реализуйте в программе очередь типа
# FIFO, добавляя в нее новые элементы в начало (слева).Поместите по порядку следования значения из data в очередь
# fifo, прочитанные из входного потока:data = list(map(int, input().split()))Извлеките из очереди три объекта
# (три целых числа) и выведите их на экран в одну строчку через пробел в порядке извлечения.
from collections import deque

fifo = deque()
data = list(map(int, input().split()))
[fifo.appendleft(i) for i in data]
for i in range(3):
    print(fifo.pop(), end=' ')
################################################################
fifo.extend(data)
print(*[fifo.pop() for _ in range(3)])
################################################################
fifo = deque(data[::-1])
[print(fifo.pop()) for _ in range(3)]
################################################################
# Подвиг 7. С помощью класса deque создайте объект очереди с именем lifo. Затем реализуйте в программе очередь типа
# LIFO, добавляя в нее новые элементы в конец (справа).Поместите по порядку следования значения из data в очередь
# lifo, прочитанные из входного потока:data = list(map(int, input().split()))Извлеките из очереди три объекта
# (три целых числа) и выведите их на экран в одну строчку через пробел в порядке извлечения.
from collections import deque

lifo = deque()
data = list(map(int, input().split()))
[lifo.append(i) for i in data]
for i in range(3):
    print(lifo.pop(), end=' ')
# Скажем, вы ввели "1 2 3 4 5". В этом случае цикл для разделения печатает "5 4 3", потому что их значения извлекаются
# в последовательности LIFO (последний вошел, первый вышел).
################################################################
lifo.extend(data)
print(*[lifo.pop() for _ in range(3)])
################################################################
# Подвиг 8. С помощью класса deque создайте буфер с именем buff для приема информации (целых чисел) с максимальным
# размером в 10 элементов. Буфер должен быть реализован по принципу очереди FIFO, причем добавление новых данных
# должно осуществляться в начало очереди (слева), а извлечение - справа (с конца очереди).Поместите в этот буфер
# данные data, прочитанные из входного потока:data = list(map(int, input().split()))Извлеките из буфера три элемента
# (три числа) и выведите их в консоль в порядке считывания из буфера в одну строчку через пробел.

from collections import deque

data = list(map(int, input().split()))
buff = deque(maxlen=10)  # maxlen уже позволяет переписывать значения если очередь заполнена.
[buff.appendleft(i) for i in data]

print(*[buff.pop() for _ in range(3)])
################################################################
# Подвиг 9. Вам в браузере нужно реализовать кнопку back (<, назад). Для этого решено воспользоваться очередью типа
# LIFO, которая бы хранила историю посещения страниц пользователем (история URL-адресов).Создайте вначале в программе
# объект с именем back_url класса deque, который бы содержал максимум 20 URL-адресов. Данные предполагается добавлять
# и извлекать с конца очереди (справа).Добавьте в очередь back_url по порядку URL-адреса, прочитанные из входного потока
import sys
from collections import deque

lst_in = list(map(str.strip, sys.stdin.readlines()))

back_url = deque(lst_in, maxlen=20)
print(back_url.pop())
################################################################
# Подвиг 10 (на повторение). Вам нужно реализовать очередь типа LIFO, используя динамический массив (как это мы делали
# ранее в этом курсе). Для этого вначале создается объект lifo как динамический массив. Затем, в конец этого массива
# последовательно добавьте числа, прочитанные из входного потока:data = list(map(int, input().split()))
# Извлеките (также с конца) два значения и выведите их в консоль в порядке их считывания в одну строчку через пробел.

lifo = [i for i in data]
for i in range(2):
    print(lifo.pop(), end=' ')
################################################################
data = list(map(int, input().split()))
lifo = []
lifo.extend(data)
print(*[lifo.pop() for _ in range(2)])
################################################################
# ___________5.2 Способы обхода и удаления вершин бинарного дерева
# __ __________алгоритмом обхода его  в ширину (слева на право):
p = root
v = [p]
while v:
    vn = []
    for x in v:
        print(x.data)
        if x.left:
            vn += [x.left]
        if x.right:
            vn += [x.right]
    v = vn
################################################################
# __ алгоритмом обхода его  в ширину (слева на право):
p = root
v = [p]
while v:
    vn = []
    for x in v:
        print(x.data)
        if x.right:  # (с справа на лево):
            vn += [x.right]
        if x.left:
            vn += [x.left]
    v = vn


################################################################
# Алгоритм обхода в глубину
def show_tree(self, node):
    if node is None:
        return
    show_tree(self, node.left)
    print(node.data)
    show_tree(self, node.right)


################################################################
# Реализация бинарного дерева в Python.

class Node:  # Создаём класс для объекта (вершины дерева) каждая вершина определяется ч/з class Node
    def __init__(self, data):  # В инициализаторе передаём данные, которые будут храниться в вершине.
        self.data = data
        self.left = self.right = None  # В каждой вершине указатели left и right по умолчанию None.


class Tree:  # Создаём класс для работы со всем деревом.
    def __init__(self):
        self.root = None  # Указатель root по умолчанию None.

    # Т.о. создано пустое бинарное дерево, для которого еще нужно определить методы для работы с ним.

    def __find(self, node, parent, value):  # Метод для поиска вершины, к кот. будет цепляться нов.объект
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True  # True - нашли значение кот. хотим добавить

        if value < node.data:  # Рекурсия для прохождения по левой ветви.
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:  # Рекурсия для прохождения по правой ветви.
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False  # False не нашли вершину со значением value,
        # node - узел к кот. мы добавляем новый узел, parent- родительский узел для node

    def append(self, obj):  # Метод для добавления новых вершин. В метод передаём объекты класса Node.
        if self.root is None:  # Проверка наличия объектов в дереве. Если root принимает значение None,
            # значит в бинарном дереве нет ни одного объекта.
            self.root = obj  # В этом случае новая вершина добавляется как корневая.
            return obj
        # Иначе нам надо добавить объект к существующей вершине:
        s, p, fl_find = self.__find(self.root, None, obj.data)  # Ищем вершину к которой добавляем obj.
        # node=self.root т.к. начинаем обход
        # s-объект (node) к которому мы добавляем вершину, parent- родительский узел для node

        if not fl_find and s:  # fl_find=False значит добавить новую вершину и s-объект к которому мы добавляем вершину
            if obj.data < s.data:  # Если значение меньше значения в s, добавляем его слева.
                s.left = obj
            else:
                s.right = obj  # Иначе - добавляем значение справа.

        return obj

    def show_tree(self, node):  # Отображение бинарного дерева в глубину.
        if node is None:
            return
        # алгоритм в глубину
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):  # Отображение бинарного дерева в ширину.
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):  # Удаление листовой вершины:
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):  # Удаление вершины с одним потомком:
        if p.left == s:
            if s.left is None:  # (Переопределяем вершины)
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):  # Метод находит минимальное значение в правом поддереве:
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):  # Метод удаляет вершину. Key определяет значение вершины.
        s, p, fl_find = self.__find(self.root, None, key)  # Ищем вершину, которую будем удалять.
        # s -удаляемая вершина, p-родительская вершина
        if not fl_find:  # удалять нечего т.к. вершина со знач key не найдена
            return None

        if s.left is None and s.right is None:  # В случае удаления листовой вершины:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:  # В случае наличия одного потомка:
            self.__del_one_child(s, p)  # s -удаляемая вершина, p-родительская вершина
        else:  # В случае наличия двух потомков:
            sr, pr = self.__find_min(s.right, s)
            # sr -min знач в правом поддереве на левой ветви, на кот заменяем после удаления s, pr -parent sr,
            # s-удаляемая вершина
            s.data = sr.data
            self.__del_one_child(sr, pr)  # удаляем вершину sr


v = [10, 5, 7, 16, 13, 2, 20]
# v = [20, 5, 24, 2, 16, 11, 18]

t = Tree()
for x in v:
    t.append(Node(x))
t.show_tree(t.root)  # отображение от корня
t.del_node(5)
t.show_wide_tree(t.root)


################################################################
# Реализация бинарного дерева в Python.- no comments
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def fl_find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.fl_find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.fl_find(node.right, node, value)
        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.fl_find(self.root, None, obj.data)
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, parent)
        return node, parent

    def del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def del_node(self, key):
        s, p, fl_find = self.fl_find(self.root, None, key)
        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.del_one_child(sr, pr)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn


# v = [10, 5, 7, 16, 13, 2, 20]
v = [20, 5, 24, 2, 16, 11, 18]

t = Tree()
for x in v:
    t.append(Node(x))
t.show_tree(t.root)  # отображение от корня
t.del_node(5)
t.show_wide_tree(t.root)


################################################################
# Подвиг 1. Ниже (в текстовом поле) приведена программа, как пример реализации бинарного дерева на языке Python.
# Внимательно разберитесь в этой программе и модифицируйте ее так, чтобы при обходе вершин в глубину сначала
# перебиралось правое поддерево, затем отображалось значение текущей вершины, а потом перебиралось левое поддерево.
# (То есть, нужно реализовать алгоритм обхода RNL).
def show_tree(self, node):
    if node is None:
        return

    self.show_tree(node.right)
    print(node.data, end=" ")
    self.show_tree(node.left)

    ################################################################
    # Подвиг 2. Ниже (в текстовом поле) приведена программа, как пример реализации бинарного дерева на языке Python.
    # Модифицируйте ее так, чтобы при обходе вершин в ширину вершины отображались по уровням справа-налево, начиная от
    # корневой вершины.
    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.right:
                    vn += [x.right]
                if x.left:
                    vn += [x.left]
            v = vn


################################################################
# Подвиг 3. Ниже (в текстовом поле) приведена программа, как пример реализации бинарного дерева на языке Python.
# Модифицируйте ее так, чтобы при обходе вершин в глубину сначала перебиралось правое поддерево, затем - левое
# поддерево, а потом отображалось значение текущей вершины.
def show_tree(self, node):
    if node is None:
        return

    self.show_tree(node.right)
    self.show_tree(node.left)
    print(node.data, end=" ")


################################################################
# Подвиг 4. Ниже (в текстовом поле) приведена программа, как пример реализации бинарного дерева на языке Python.
# Модифицируйте ее так, чтобы при обходе вершин в ширину вершины отображались по уровням слева-направо
# начиная с нижних (последних) уровней. Вывод должен быть в одну строку через пробел.
from collections import deque


class Tree:

    def __init__(self):
        self.root = None
        self.q = deque()

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                self.q.appendleft(x.data)
                if x.right:
                    vn += [x.right]
                if x.left:
                    vn += [x.left]
            v = vn
        print(*self.q)
        # print(*[i for i in self.q])


v = [20, 5, 24, 2, 16, 11, 18]
t = Tree()
for i in v:
    t.append(Node(i))

t.show_wide_tree(t.root)  # 11 18 2 16 5 24 20


################################################################
# рекурия
def show_wide_tree(self, node):
    def func(nodes):
        if nodes:
            child_nodes = []
            for node in nodes:
                if node.left:
                    child_nodes.append(node.left)
                if node.right:
                    child_nodes.append(node.right)
            func(child_nodes)
            print(*map(lambda x: x.data, nodes), end=' ')
            # print(*map(lambda x: x.data, child_nodes), end=' ')

    func([node])

    ################################################################
    def show_wide_tree(self, node):
        if node is None:
            return
        v = [node]
        all_node = [[node.data]]
        while v:
            vn = []
            for x in v:
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            all_node.append([x.data for x in vn])
            # all_node += [[x.data for x in vn]]
            #  all_node.extend([map(lambda x: x.data, vn)]) # sequence.extend(iterable) расширяет список другой после.
            v = vn

        while all_node:
            print(*all_node.pop(), end=" ")

    ################################################################
    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        res = []
        while v:
            vn = []
            for x in v:
                res.insert(0, x.data)
                if x.right:
                    vn += [x.right]
                if x.left:
                    vn += [x.left]
            v = vn
        print(*res)

    ################################################################
    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        res = []
        while v:
            vn = []
            for x in v:
                res.append(x.data)
                self.q.appendleft(x.data)
                if x.right:
                    vn += [x.right]
                if x.left:
                    vn += [x.left]
            v = vn
        print(*res[::-1])

    ################################################################
    # Подвиг 5. Ниже (в текстовом поле) приведена программа, как пример реализации бинарного дерева на языке Python.
    # Модифицируйте ее так, чтобы большие значения добавлялись в левое поддерево, а меньшие - в правое поддерево.
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value > node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value < node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data > s.data:
                s.left = obj
            else:
                s.right = obj


################################################################
# Подвиг 7. Программа на Python. Пусть имеется следующий словарь:d = {'one': 1, 'two': 2, 'natural': 1, 'True': 1,
# 'even': 2, 'three': 3, 'False': 0}Сформируйте из него другой словарь d_unique, состоящий из данных с уникальными
# значениями (оставлять нужно последнее значение, остальные отбрасывать).

d = {'one': 1, 'two': 2, 'natural': 1, 'True': 1, 'even': 2, 'three': 3, 'False': 0}  # этот словарь не менять

d_unique = {}

for key2, value in d.items():
    for key in d:
        if value == d_unique.get(key, None):
            del d_unique[key]
            d_unique[key2] = value
        else:
            d_unique[key2] = value
# {'True': 1, 'even': 2, 'three': 3, 'False': 0}
########################################################################
d_unique = {v: k for k, v in d.items()}  # {'True': 1, 'even': 2, 'three': 3, 'False': 0}
################################################################
d_unique = {}
# Перевернем исходный словарь (поменяем местами ключи и значения)
rev_d = {value: key for key, value in d.items()}
# Теперь просто перевернем обратно получившийся словарь
d_unique = {value: key for key, value in rev_d.items()}
################################################################
d_unique = {v: k for k, v in d.items()}
d_unique = {v: k for k, v in d_unique.items()}
################################################################
d_unique = {v: k for k, v in {v: k for k, v in d.items()}.items()}
################################################################

temp_dict = {j: i for i, j in d.items()}
d_unique = {j: i for i, j in temp_dict.items()}
################################################################
d2 = {}
for key, val in d.items():
    d2[val] = key
d_unique = {}
for key, val in d2.items():
    d_unique[val] = key
################################################################

# _from _Balakirev_learning__
# 1. Алгоритм Кнута-Морриса-Пратта (КМП-алгоритм)_______________________________________________________________

t = "лилила"
p = [0] * len(t)
j = 0
i = 1
while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        j += 1
        i += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:  # j>0
            j = p[j - 1]
print(p)  # [0, 0, 1, 2, 3, 0]
a = "лилилось лилилась"
m = len(t)
n = len(a)

i = 0
j = 0
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("образ найден")
            break
    else:
        if j > 0:
            j = p[j - 1]
        else:
            i += 1
if i == n and j != m:
    print("образ не найден")  # образ найден


################################
# рекурсия
def degree(x, y):
    if (y == 0):
        return 1
    if (y == 1):
        return (x)
    # оставшиеся кейсы, когда степень > 1
    if (y != 1):
        return (x * degree(x, y - 1))


x = int(input("Введите число: "))
y = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", degree(x, y))

