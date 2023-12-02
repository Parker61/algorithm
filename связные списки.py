
################################################################
 #Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, а
# формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:Для этого объявите в программе
# класс ListObject, объекты которого создаются командой:obj = ListObject(data) Каждый объект класса ListObject должен
# содержать локальные свойства:next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет,
# то next_obj = None);data - данные объекта в виде строки.В самом классе ListObject должен быть объявлен метод:
# link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj
# объекта self должен ссылаться на obj).Прочитайте список строк из входного потока командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))Затем сформируйте односвязный список, в объектах которых
# (в атрибуте data) хранятся строки из списка lst_in (первая строка в первом объекте, вторая - во втором и  т.д.).
# На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.
# #Нужно создать экземпляры класса ListObject в количестве равном числу строк в переменной lst_in. Имя имеет только
# первый экземпляр. Остальные существуют в виде ссылки, которая прописана в предыдущем экземпляре. Ну это если совсем
# грубо. Получается такая конструкция, в которой к экземплярам (кроме первого) нельзя обратиться напрямую, а только
# вызвав из предыдущего экземпляр

# создать пустой список , потом циклом пройтись по lst_in и наполнить тот наш пустой список обьектами класса(то есть
# нужно их тут создать). Далее другим циклом пройтись по этому нашему списку(в котором теперь у нас лежат наши обьекты)
# , вызывая при этом метод link для каждого нашего обьекта( и передавая соответственно нужные ему аргументы), другими
# словами наполняя ссылками сами обьекты: l[i].link(l[i+1]) , где l это как раз таки наш список с обьектами, но будьте
# внимательными чтобы индекс не выходил за пределы списка, а так же, что нужно оставить последнему обьекту ссылку на
# None(проще говоря делайте цикл на количество строк в этом списке и потом сделайте условие if i < len(l)-1: )
import sys


class ListObject:
    def __init__(self, data: str):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['1. Первые шаги в ООП', '1.1 Как правильно проходить этот курс', '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов', '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del', '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
lst = []
for i in lst_in:
    obj = ListObject(i)
    lst.append(obj)

for i in range(len(lst)):
    if i < len(lst) - 1:
        lst[i].link(lst[i + 1])

head_obj = lst[0]
########################################################################
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):  # если будет срез - то большие затраты памяти тк создаётся копия lst
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)  # obj_new добавляем в конец объекта obj
    obj = obj_new


########################################################################
class ListObject:
    def __init__(self, data: str):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj.link(ListObject(lst_in[i]))
    obj = obj.next_obj
########################################################################
objects = [ListObject(x) for x in lst_in]
for i in range(len(lst_in) - 1):
    objects[i].link(objects[i + 1])

head_obj = objects[0]
########################################################################
lst = [ListObject(i) for i in lst_in]
for i in range(len(lst_in) - 1):
    lst[i].link((lst[i + 1]))
head_obj = lst[0]

################################################################


# Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке
# Python), когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:
# Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:

class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;        """
        if self.tail:
            self.tail.set_next(obj)  # связывание старого объекта self.tail с новым объектом obj (self.__next = obj)
            obj.set_prev(self.tail)  # связка нового объекта obj,здесь  self.__prev = self.tail
        self.tail = obj  # переместить указатель self.tail на новый объект obj,
        # self.tail будет равен всегда послед добаленому объекту
        if not self.head:  # если добавляем только самый первый объект
            self.head = obj

    def remove_obj(self):
        """удаление последнего объекта из связного списка;        """
        if self.tail is None:
            return  # ничего не делать
        prev = self.tail.get_prev()  # -> self.__prev
        if prev:  # если предыдущий существует
            prev.set_next(None)  # последний объект self.next указывает на None
        self.tail = prev  # переместить tail на предпоследний prev объект
        if self.tail is None:  # если мы удаляем единственный объект то tail будет указывать на None
            self.head = None

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.        """
        lst = []
        h = self.head
        while h:
            lst.append(h.get_data())  # ->self.__data
            h = h.get_next()  # переход на след объект связного списка,
        return lst


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:    """

    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None

    def set_next(self, obj):  # связывание с новым объетом класса ObjList
        """изменение приватного свойства __next на значение obj;        """
        self.__next = obj

    def set_prev(self, obj):  # obj -> self.tail, к новому объекту привязка предыдущего значения self.tail
        """изменение приватного свойства __prev на значение obj;        """
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next;        """
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;        """
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data;        """
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data.        """
        return self.__data


# ob = ObjList("данные 1")
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
print(res)


################################################################
class LinkedList:
    '''в каждом объекте этого класса должны создаваться локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None)
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None)'''

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj) -> None:
        '''добавление нового объекта obj класса ObjList в конец связного списка'''
        if self.head is None:  # Если объект первый и указателя начала head не существует..
            self.head = obj  # head будет указывать на передаваемый объект, все, уходим...
            return
        last_obj = self.head  # Если это не так, пусть последним будет head
        while (last_obj.get_next()):  # Пока укатель next не станет указывать на None
            last_obj = last_obj.get_next()  # У предпоследнего объекта проходим по ссылке get_next() получаем последний
        last_obj.set_next(obj)  # У последнего объекта ставим указатель _nex на передаваемый объект
        obj.set_prev(last_obj)  # У передаваемого объекта ставим указатель _prev на бывший последним объект
        self.tail = obj

    def remove_obj(self) -> None:
        '''удаление последнего объекта из связного списка'''
        if self.head is not None:
            if self.head.get_next() is None:
                self.head = None
                return
            self.head = self.head.get_next()
            self.head.set_prev(None)

    def get_data(self):
        '''получение списка из строк локального свойства __data всех объектов связного списка'''
        if self.head is None:
            return []
        if self.head.get_next() is None:
            return [self.head.get_data()]
        data = []
        last_obj = self.head
        while (last_obj != self.tail):  # До предпоследнего объекта переходим по ссылке _next, аппендим
            data.append(last_obj.get_data())
            last_obj = last_obj.get_next()  # Последний объект все равно получен, тк мы перешли у предпоследнего по ссылке :)
        data.append(last_obj.get_data())
        return data


class ObjList:
    '''__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None)
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None)
    __data - строка с данными'''

    def __init__(self, data=None) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj) -> None:
        '''изменение приватного свойства __next на значение obj'''
        self.__next = obj

    def set_prev(self, obj) -> None:
        '''изменение приватного свойства __prev на значение obj'''
        self.__prev = obj

    def get_next(self):
        '''получение значения приватного свойства __next'''
        return self.__next

    def get_prev(self):
        '''получение значения приватного свойства __prev'''
        return self.__prev

    def set_data(self, data: str) -> None:
        '''изменение приватного свойства __data на значение data'''
        self.__data = data

    def get_data(self) -> str:
        '''получение значения приватного свойства __data'''
        return self.__data


###############################################################
class LinkedList:

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def remove_obj(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        data_list = []
        obj = self.head
        while obj:
            data_list.append(obj.get_data())
            obj = obj.get_next()
        return data_list


################################################################
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def remove_obj(self):
        if self.head:
            if self.head != self.tail:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)
            else:
                self.head = self.tail = None

    def get_data(self) -> list:
        result = []
        obj = self.head
        while obj:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result


###############################################################
###############################################################
# Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов),
# когда один объект ссылается на следующий и так по цепочке до последнего:Для этого объявите в программе два класса:
# StackObj - для описания объектов односвязного списка;Stack - для управления односвязным списком.
# Объекты класса StackObj предполагается создавать командой:obj = StackObj(данные)Здесь данные - это строка с
# некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:
# __data - ссылка на строку с данными, указанными при создании объекта;__next - ссылка на следующий объект класса
# StackObj (при создании объекта принимает значение None).Также в классе StackObj должны быть объявлены
# объекты-свойства:next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.При записи необходимо реализовать
# проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит,
# то __next остается без изменений.Класс Stack предполагается использовать следующим образом:
# st = Stack() # создание объекта односвязного спискаВ объектах класса Stack должен быть локальный публичный атрибут:
# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).
# А в самом классе Stack следующие методы:
# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data
# каждого объекта в порядке их добавления, или пустой список, если объектов нет).

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            # if isinstance(next, (StackObj, type(None))):
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if not self.top:
            self.top = obj

    def pop(self):
        data = self.top
        if data is None:
            return
        while data and data.next != self.tail:
            data = data.next
        if data:
            data.next = None
        last = self.tail  # извлечение последнего объекта перед удалением
        self.tail = data

        if self.tail is None:
            self.top = None
        return last

    def get_data(self):
        lst = []
        h = self.top
        while h:
            lst.append(h.data)
            h = h.next
        return lst


###############################################################
class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
            self.top.next = None
        else:
            self.tail.next = obj
        self.tail = obj
        self.tail.next = None

    def pop(self):
        d = self.tail
        if self.top == self.tail:
            self.top = None
        else:
            n = self.top
            while n.next.next != None:
                n = n.next
            n.next = None
            self.tail = n
        return d


################################################################
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if any((isinstance(obj, StackObj), obj is None)):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):  # при добавлении нового элемента
        if not self.top:  # если отсутствует головной элемент
            self.top = obj  # присваиваем объект в переменную головного элемента
        else:  # иначе (если имеется головной элемент)
            mark = self.top  # вспомогательной переменной присваиваем значение топ
            while mark.next:  # пока у текущего значения вспомогательной переменной есть ссылка на след. элемент
                mark = mark.next  # присваиваем вспомогательной переменной след. элемент (доходим до крайнего эл)
            mark.next = obj  # если больше нет ссылок на следующий элемент, присваиваем этому атрибуту объект

    def pop(self):  # при изъятии элемента
        if not self.top:  # если отсутствует головной элемент (значит ни один элемент не был добавлен)
            return  # выход из метода
        if not self.top.next:  # если у головного элемента нет следующего(в списке только один элемент)
            poper = self.top  # вспомогательной переменной присваиваем значение топ
            self.top = None  # само значение топ меняем на None (удаляем из списка)
            return poper  # возвращаем изъятое значение
        else:  # иначе (если есть следующий элемент)
            mark = self.top  # вспомогательной переменной присваиваем значение топ
            while mark.next.next:  # пока у следующего значения есть следующее значение
                mark = mark.next  # вспомогательная переменная становвится следующим значением (нашли предпоследний эл)
            poper = mark.next  # определяем переменную для возврата последнего элемента
            mark.next = None  # удаляем последний элемент
            return poper  # возвращаем последний элемент

    def get_data(self):
        data = []  # заводим пустой список
        mark = self.top  # отмечаем начало списка
        while mark:  # пока существует текущий элемент
            data.append(mark.data)  # добавляем его данные в список
            mark = mark.next  # переходим к следующему элементу у текущего
        return data  # как только текущий элемент == None - выход из цикла, возвращаем список данных


###############################################################
class StackObj:
    """ для описания объектов стека """

    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if type(next_) is StackObj or not next_:
            self.__next = next_

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @classmethod
    def check_data(cls, data):
        pass


class Stack:
    """ для управления стек-подобной структурой """

    def __init__(self):
        self.top = None

    def push(self, obj):
        """ Если стэк пустой - просто добавляем элемент.
        Если не пустой - проходимся по стэку, ищем последний элемент и вставляем после него новый"""
        if not self.top:
            self.top = obj
            return
        tmp = self.top
        while tmp.next:
            tmp = tmp.next
        tmp.next = obj

    def pop(self):
        """ Если стэк пуст - ничего не делаем с ним
         Если в стэке 1 элемент, удалвяем его
         Если больше одного - ищем предпоследний и у него свойство __next устанавливаем в None"""
        if not self.top:
            return
        if not self.top.next:
            self.top = None
            return
        tmp1 = self.top
        tmp2 = self.top.next
        while tmp2.next:
            tmp1, tmp2 = tmp2, tmp2.next
        tmp1.next = None
        return tmp2

    def get_data(self):
        """ проходим по всему стэку и добавляем в список res значение data каждого объекта стэка """
        res = []
        tmp = self.top
        if self.top:
            while tmp.next:
                res.append(tmp.data)
                tmp = tmp.next
            else:
                res.append(tmp.data)
        return res

################################################################################################

# Большой подвиг 8. Требуется реализовать программу по работе с решающими деревьями:Здесь в каждом узле дерева делается
# проверка (задается вопрос). Если проверка проходит, то осуществляется переход к следующему объекту по левой стрелке
# (с единицей), а иначе - по правой стрелке (с нулем). И так до тех пор, пока не дойдем до одного из листа дерева
# (вершины без потомков).В качестве входных данных используется вектор (список) с бинарными значениями:
# 1 - да, 0 - нет. Каждый элемент этого списка соответствует своему вопросу (своей вершине дерева), например:
# Далее, этот вектор применяется к решающему дереву, следующим образом. Корневая вершина "Любит Python" с ней связан
# первый элемент вектора x и содержит значение 1, следовательно, мы переходим по левой ветви. Попадаем в вершину
# "Понимает ООП". С ней связан второй элемент вектора x со значением 0, следовательно, мы переходим по правой ветви и
# попадаем в вершину "будет кодером". Так как эта вершина конечная (листовая), то получаем результат в виде строки
# "будет кодером". По аналогии выполняется обработка вектора x с другими наборами значений 0 и 1.Для реализации
# решающих деревьев в программе следует объявить два класса:
# TreeObj - для описания вершин и листьев решающего дерева;
# DecisionTree - для работы с решающим деревом в целом.В классе DecisionTree должны быть реализованы (по крайне мере)
# два метода уровня класса (@classmethod):def predict(cls, root, x) - для построения прогноза
# (прохода по решающему дереву) для вектора x из корневого узла дерева root.
# def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево (метод должен возвращать
# добавленную вершину - объект класса TreeObj);В методе add_obj параметры имеют, следующие значения:
# obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
# node - ссылка на объект дерева, к которому присоединяется вершина obj;left - флаг, определяющий ветвь дерева
# (объекта node), к которой присоединяется объект obj (True - к левой ветви; False - к правой).В классе TreeObj
# следует объявить инициализатор:def __init__(self, indx, value=None): ...где indx - проверяемый в вершине дерева
# индекс вектора x; value - значение, хранящееся в вершине (принимает значение None для вершин, у которых есть потомки
# - промежуточных вершин).При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться
# следующие локальные атрибуты:indx - проверяемый индекс (целое число);value - значение с данными (строка);
# __left - ссылка на следующий объект дерева по левой ветви (изначально None);__right - ссылка на следующий объект
# дерева по правой ветви (изначально None).Для работы с локальными приватными атрибутами __left и __right необходимо
# объявить объекты-свойства с именами left и right.

class TreeObj:
    """для описания вершин и листьев решающего дерева;"""

    def __init__(self, indx, value=None):
        """ indx - проверяемый в вершине дерева индекс вектора x;
        value - значение, хранящееся в вершине
        (принимает значение None для вершин, у которых есть потомки - промежуточных вершин)."""
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        """__left - ссылка на следующий объект дерева по левой ветви (изначально None);"""
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    """для работы с решающим деревом в целом."""

    @classmethod
    def predict(cls, root, x):
        """для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root"""
        # DecisionTree.predict(root, [1, 1, 0])
        if x[0] == 1:
            c = root.left
            if x[1] == 1:
                return c.left.value  # [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
            else:
                return c.right.value
        else:
            c = root.right
            if x[2] == 1:
                return c.left.value
            else:
                return c.right.value
        # var_2
        current = root
        while current.value == None:
            if x[current.indx]:
                current = current.left
            else:
                current = current.right
        return current.value

        # var_3
        current = root
        while not current.value:
            current = current.left if x[current.indx] == 1 else current.right
        return current.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj)
            obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
            node - ссылка на объект дерева, к которому присоединяется вершина obj; предыдущий объект
            left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj
            (True - к левой ветви; False - к правой)."""

        # DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
        if node:
            if left:  # left=True
                node.left = obj  # v_11         ###- value : "будет программистом" / "будет кодером"
            else:
                node.right = obj  # v_12        ###- value : "не все потеряно" / "безнадежен"
        return obj


root = DecisionTree.add_obj(TreeObj(0))  # root
v_11 = DecisionTree.add_obj(TreeObj(1), root)  # v_11
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)  # v_12
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)

assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree,
                                                    'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(
    TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"


################################################################################################
class DecisionTree:  # var_3

    @classmethod
    def predict(cls, root, x):
        current = root
        while not current.value:
            current = cls.get_next(current, x)
        return current.value

    @classmethod
    def get_next(cls, current, x):
        if x[current.indx] == 1:
            return current.left
        return current.right

    ################################################################################################
    class DecisionTree:
        @classmethod
        def predict(cls, root, x):
            current = root
            while current is not None:
                left, right = current.left, current.right

                # if not (left and right):
                if left is None or right is None:
                    break
                current = current.left if x[current.indx] else current.right
            return current.value

        @classmethod
        def add_obj(cls, obj, node=None, left=True):
            if node:
                setattr(node, 'left' if left else 'right', obj)  # settatr(obj,name,value)
            return obj


################################################################################################
class DecisionTree:
    STEP = {1: 'left', 0: 'right'}

    @classmethod
    def predict(cls, root, x):
        node = root
        while node.indx != -1:
            node = getattr(node, cls.STEP[x[node.indx]])
        return node.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            setattr(node, cls.STEP[left], obj)
        return obj




################################################################

# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:Здесь создается список
# из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие
# локальные атрибуты:__data - ссылка на строку с данными;__prev - ссылка на предыдущий объект связного списка
# (если объекта нет, то __prev = None);__next - ссылка на следующий объект связного списка (если объекта нет,
# то __next = None).В свою очередь, объекты класса LinkedList должны создаваться командой:linked_lst = LinkedList()
# и содержать локальные атрибуты:head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
# А сам класс содержать следующие методы:add_obj(obj) - добавление нового объекта obj класса ObjList в конец
# связного списка;remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру
# (индексу); индекс отсчитывается с нуля.Также с объектами класса LinkedList должны поддерживаться следующие операции:
# len(linked_lst) - возвращает число объектов в связном списке;linked_lst(indx) - возвращает строку __data, хранящуюся
# в объекте класса ObjList, расположенного под индексом indx (в связном списке).Пример использования классов
#  Длина обычного списка лимитирована. Связного - нет.
# Все объекты будут храниться в цепочке.Сборщик мусора их не будет трогать так как остаются ссылки на них.
class ObjList:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            # if isinstance(obj,(ObjList,type(None))):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_next(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj_next(indx)
        if obj is None:
            return
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        h = self.head
        n = 0
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx):
        obj = self.__get_obj_next(indx)
        return obj.data if obj else None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev


#######################################################################
class Description:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'  # Чтоб дескриптор работал, в set_name нужно так прописать чтобы
        # прошли проверки в assert
        # self.name = '__' + name

    # если пишут атрибуты __attr имеется в виду приватный атрибут. если через set_name задавать имя
    # как "__" + name это будет не приватный атрибут а именно, как бы это странно не выгладело, тупо
    # атрибут с двумя подчеркиваниями. попробуйте создать приватный атрибут вообще без десрипторов и
    # проперти и посмотрите как он отображается в __dict__, вот точно с таким же именем и должен
    # создаваться атрибут в вашей программе чтобы прошли тесты, т.к. тесты рассчитаны на приватные
    # атрибуты
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, ObjList) and value is not None:
            raise TypeError("ObjList objects can only be assigned to ObjList objects")
        setattr(instance, self.name, value)


class ObjList:
    data = Description()
    prev = Description()
    next = Description()

    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


########################################################################
class ObjList:

    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

    def __setattr__(self, attr, value):
        if attr == 'data' and isinstance(value, str):
            object.__setattr__(self, '_ObjList__' + attr, value)
        elif attr in ('prev', 'next') and isinstance(value, (ObjList, type(None))):
            object.__setattr__(self, '_ObjList__' + attr, value)

    def __getattribute__(self, attr):
        if attr in ('data', 'prev', 'next'):
            return object.__getattribute__(self, '_ObjList__' + attr)
        return object.__getattribute__(self, attr)


class LinkedList:
    def chek_index(self, index):
        if not isinstance(index, int):
            raise TypeError('list indices must be integers, not str')
        if index >= self.len or index < 0:
            raise IndexError('list index out of range')

    def __init__(self):
        self.head = self.tail = None
        self.len = 0

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            obj.prev = self.tail
            if self.tail:
                self.tail.next = obj
            else:
                self.head = obj
            self.tail = obj
            self.len += 1

    def remove_obj(self, index):
        obj = self(index, data=False)
        self.len -= 1
        if obj.prev:
            obj.prev.next = obj.next
        else:
            self.head = obj.next
        if obj.next:
            obj.next.prev = obj.prev
        else:
            self.tail = obj.prev

    def __len__(self):
        return self.len

    def __call__(self, index, data=True):
        self.chek_index(index)
        obj = self.head
        index -= 1
        while index != -1:
            obj = obj.next
            index -= 1
        if data:
            return obj.data
        return obj


###############################################################################################################################################
class Desc:
    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        if __name in ('data', 'prev', 'next', 'head', 'tail'):
            __name = f'_{type(self).__name__}__{__name}'
        return super().__setattr__(__name, __value)

    def __getattr__(self, name):
        return self.__getattribute__(f'_{type(self).__name__}__{name}')


class ObjList(Desc):
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None


class LinkedList(Desc):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_obj(self, obj):
        if self.__head:
            self.__tail.next = obj
            obj.prev = self.__tail
        else:
            self.__head = obj
        self.__tail = obj

    def remove_obj(self, indx):
        n = self.iteration_over_all_elements('cnt < indx', 'n', indx)
        if n.prev:
            n.prev.next = n.next
        else:
            self.__head = self.__head.next
        if n.next:
            n.next.prev = n.prev
        else:
            self.__tail = self.__tail.prev

    def __len__(self):
        return self.iteration_over_all_elements('n', 'cnt')

    def __call__(self, indx):
        return self.iteration_over_all_elements('cnt < indx', 'n.data', indx)

    def iteration_over_all_elements(self, condition, data_to_return, indx=0):
        n = self.__head
        cnt = 0
        while eval(condition):
            n = n.next
            cnt += 1
        return eval(data_to_return)


########################################################################
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def __getattr__(self, name):
        return object.__getattribute__(self, self.__fixname(name))

    def __setattr__(self, name, value):
        self.__dict__[self.__fixname(name)] = value

    def __fixname(self, name):
        return f'_{type(self).__name__}__{name}' if name in ('data', 'prev', 'next') else name

    def __str__(self):
        return self.__data

    def glue(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next


class LinkedList:
    def __init__(self):
        self.__list = []
        self.head = None
        self.tail = None

    def __len__(self):
        return len(self.__list)

    def __call__(self, indx, *args, **kwargs):
        if 0 <= indx < len(self):
            return self.__list[indx].data

    def add_obj(self, obj):
        if not len(self):
            self.head = obj
        else:
            prev = self.__list[-1]
            obj.prev, prev.next = prev, obj
        self.tail = obj
        self.__list.append(obj)

    def remove_obj(self, indx):
        if 0 <= indx < len(self):
            removed = self.__list.pop(indx)
            removed.glue()
            if removed == self.head:
                self.head = removed.next
            if removed == self.tail:
                self.tail = removed.prev


########################################################################
# все на обычном List построено ))
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self): return self.__data


class LinkedList:
    def __init__(self):
        self.__lst = []
        self.__upd()

    def __upd(self):
        if self.__lst:
            self.head = self.__lst[0]
            self.tail = self.__lst[-1]
        else:
            self.head = self.tail = None

    def __len__(self):
        return len(self.__lst)

    def __call__(self, idx):
        try:
            return self.__lst[idx].data
        except:
            return None

    def add_obj(self, obj):
        self.__lst.append(obj)
        self.__upd()

    def remove_obj(self, idx):
        try:
            self.__lst.pop(idx)
            self.__upd()
        except:
            pass











################################################################################################
# Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один
# объект ссылается на следующий и так далее):Давайте снова создадим такую структуру данных. Для этого объявим
# два класса:Stack - для управления односвязным списком в целом;StackObj - для представления отдельных объектов
# в односвязным списком.Объекты класса StackObj должны создаваться командой:obj = StackObj(data)
# где data - строка с некоторыми данными.Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
# __data - ссылка на строку с переданными данными;__next - ссылка на следующий объект односвязного списка
# (если следующего нет, то __next = None).Объекты класса Stack создаются командой:st = Stack()
# и каждый из них должен содержать локальный атрибут:top - ссылка на первый объект односвязного списка
# (если объектов нет, то top = None).Также в классе Stack следует объявить следующие методы:
# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.Дополнительно нужно реализовать следующий
# функционал (в этих операциях копии односвязного списка создавать не нужно):# добавление нового объекта класса
# StackObj в конец односвязного списка stst = st + obj st += obj# добавление нескольких объектов в конец
# односвязного спискаst = st * ['data_1', 'data_2', ..., 'data_N']st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из
# списка (каждый элемент списка для очередного добавляемого объекта).
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    # @property
    # def data(self):
    #     return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        if self.__last:
            self.__last.next = obj
        self.__last = obj

    def pop_back(self):
        h = self.top
        if h is None:
            return
        while h.next and h.next != self.__last:
            h = h.next

        if self.__last == self.top:
            self.__last = self.top = None
        else:
            self.__last = h
            # h.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):  # ['data_1', 'data_2', ..., 'data_N']
        for i in other:
            self.__add__(StackObj(i))  # создать объект StackObj для каждого i
        return self

    def __imul__(self, other):
        return self.__mul__(other)


st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"


###############################################################################################################################################
class Desc:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class StackObj:
    data = Desc()
    next = Desc()

    def __init__(self, data):
        self.data = data
        self.next = None


########################################################################
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if type(value) is StackObj or value is None:
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        if type(other) is list and other:
            for data in other:
                self.push_back(StackObj(data))
        return self

    def push_back(self, obj):
        if type(obj) is StackObj:
            if self.top:
                self.get_last().next = obj
            else:
                self.top = obj

    def pop_back(self):
        if self.top and self.top.next:
            cur_obj = self.top
            while cur_obj.next.next:
                cur_obj = cur_obj.next
            cur_obj.next = None
        else:
            self.top = None

    def get_last(self):
        cur_node = self.top
        while cur_node.next:
            cur_node = cur_node.next
        return cur_node


########################################################################
# Двухсвязный список, чтобы не искать последний елемент.
class DescObj:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class StackObj:
    data, next, prev = DescObj(), DescObj(), DescObj()

    def __init__(self, data):
        self.__data = data
        self.__prev = self.__next = None


class Stack:
    def __init__(self):
        self.top = self.tail = None

    def push_back(self, obj):
        if self.top:
            self.tail.next = obj
            obj.prev = self.tail
        else:
            self.top = obj
        self.tail = obj

    def pop_back(self):
        last = self.tail
        if self.tail is not None and self.tail.prev:
            last = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.__init__()
        return last

    def __add__(self, obj):
        self.push_back(obj)
        return self

    def __mul__(self, data_items):
        [self.push_back(StackObj(data)) for data in data_items]
        return self

################################################################

###############################################################################################################################################
# Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:
# Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:Stack - для представления стека в целом;
# StackObj - для представления отдельных объектов стека.В классе Stack должны быть методы:
# push_back(obj) - для добавления нового объекта obj в конец стека;push_front(obj) - для добавления нового объекта
# obj в начало стека.В каждом объекте класса Stack должен быть публичный атрибут:top - ссылка на первый объект стека
# (при пустом стеке top = None).Объекты класса StackObj создаются командой:obj = StackObj(data)где data - данные,
# хранящиеся в объекте стека (строка).Также в каждом объекте класса StackObj должны быть публичные атрибуты:
# data - ссылка на данные объекта;next - ссылка на следующий объект стека (если его нет, то next = None).
# Наконец, с объектами класса Stack должны выполняться следующие команды:st = Stack()st[indx] = value # замена прежних
# данных на новые по порядковому индексу (indx); отсчет начинается с нуляdata = st[indx]  # получение данных из
# объекта стека по индексу n = len(st) # получение общего числа объектов стека for obj in st: # перебор объектов стека
# (с начала и до конца)    print(obj.data)  # отображение данных в консольПри работе с индексами (indx),
# нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе,
# генерировать исключение командой:raise IndexError('неверный индекс')
class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj  # для связки
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __len__(self):
        # return sum(1 for _ in self.__dict__.keys())
        return sum(1 for _ in self)

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __get_obj_index(self, item):  # взятие объекта по индексу
        if type(item) != int or not (0 <= item < len(self.__dict__)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__get_obj_index(item)
        for i, obj in enumerate(self):  # self является итератором
            # for i, obj in enumerate(self.__dict__.values()):
            if i == item:
                return obj.data

    def __setitem__(self, key, value):
        self.__get_obj_index(key)
        for i, obj in enumerate(self):  # self является итератором
            if i == key:
                obj.data = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


st = Stack()

st[0] = 'value'  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[0]  # получение данных из объекта стека по индексу
n = len(st)  # получение общего числа объектов стека

for obj in st:  # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль


########################################################################
class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj  # для связки
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __len__(self):
        # return sum(1 for _ in self.__dict__.keys())
        return sum(1 for _ in self)

    def __iter__(self):
        self.h = self.top
        return self
        # метод __iter__ должен возвращать объект-итератор, а не просто устанавливать какое-то состояние. При вызове
        # метода __iter__ он инициализирует начальное состояние объекта-итератора и возвращает его. Затем этот объект
        # используется для последующего перебора элементов в цикле for.В данном коде, при создании объекта-итератора
        # в методе __iter__, переменная self.current устанавливается в self.top, то есть на первый элемент стека,
        # таким образом гарантируя, что итерация начнется с начала стека при использовании for obj in st:. Если бы
        # мы установили self.current = self.top в методе __next__ вместо метода __iter__, то каждый раз при переборе
        # элементов стека циклом for, итератор бы начинался с самого начала, что может привести к непредсказуемому
        # поведению в случае измененhа внутри цикла.

    def __next__(self):
        # Метод __next__ теперь использует цикл for, используя переменную self.h как начальное состояние. Цикл
        # выполняется, пока self.h не станет None, и при каждой итерации он возвращает следующий элемент из стека.
        # if self.h:
        #     next = self.h
        #     self.h = self.h.next
        #     return next
        # else:
        #     raise StopIteration()
        while self.h is not None:
            next = self.h
            self.h = self.h.next
            return next
        raise StopIteration()

    def __get_obj_index(self, item):  # взятие объекта по индексу
        if type(item) != int or not (0 <= item < len(self.__dict__)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__get_obj_index(item)
        for i, obj in enumerate(self):  # self является итератором
            if i == item:
                return obj.data

    def __setitem__(self, key, value):
        self.__get_obj_index(key)
        for i, obj in enumerate(self):  # self является итератором
            if i == key:
                if i == 0:
                    obj.data = value

    ########################################################################
    def __iter__(self):
        self.h = self.top
        while self.h is not None:
            yield self.h
            self.h = self.h.next


########################################################################
class StackObj:

    def __init__(self, data):
        self.__next = None
        self.data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    # Метод __getitem__ в данном классе используется для получения значения элемента стека по его индексу. При вызове
    # метода с аргументом get_data=True, он возвращает значение (атрибут data) элемента стека, соответствующего данному
    # индексу. А при передаче аргумента False, метод возвращает сам элемент стека (StackObj), а не его значение.
    # В строке root = self.__getitem__(self.__count - 1, False), метод __getitem__ вызывается с параметрами
    # self.__count - 1 и False. Это означает, что будет получен последний элемент стека (так как индекс последнего
    # элемента равен self.__count - 1), но не его значение. Полученный объект будет присвоен переменной root.
    def __init__(self):
        self.top = None
        self.__count = 0

    @staticmethod
    def check_index(idx, count):
        if not (isinstance(idx, int) and 0 <= idx < count):
            raise IndexError('неверный индекс')

    def __len__(self):
        return self.__count

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            root = self.__getitem__(self.__count - 1, False)
            root.next = obj
        self.__count += 1

    def push_front(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
        self.__count += 1

    def pop(self):
        if self.__count == 1:
            obj = self.top
            self.top = None
        elif self.__count > 1:
            obj = self.__getitem__(self.__count - 1)
            prev = self.__getitem__(self.__count - 2)
            prev.next = None
        self.__count -= 1
        return obj

    def __getitem__(self, idx, get_data=True):
        self.check_index(idx, self.__count)
        if idx == 0:
            return self.top.data if get_data else self.top
        count, root = 0, self.top
        while count < idx:
            count += 1
            root = root.next
        return root.data if get_data else root

    def __setitem__(self, idx, value):
        self.check_index(idx, self.__count)
        if idx == 0:
            next = self.top.next
            self.top.data = value
            self.next = next
        else:
            root = self.__getitem__(idx, False)
            prev = self.__getitem__(idx - 1, False)
            next = root.next
            root.data = value
            root.next, prev.next = next, root

    def __iter__(self):
        for i in range(len(self)):
            yield self.__getitem__(i, False)

