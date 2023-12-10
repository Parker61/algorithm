#_from _Balakirev_learning__
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