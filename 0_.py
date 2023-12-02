
if __name__ == '__main__':

    
def quickselect(arr, k):
    if len(arr) == 1:
        assert k == 0
        return arr[0]
    pivot = arr[random.randint(0,len(array)-1)]
    # pivot = arr[len(arr) // 2]
    less, equal, greater = segregate(arr, pivot)
    if k < len(less):
        return quickselect(less, k)
    elif k > len(less) + len(equal):
        return quickselect(greater, k - len(less) - len(equal))
    else:
        return equal[0]


def segregate(arr, pivot):
    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot:

        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return less, equal, greater


try:
    array = [4, 2, 9, 1, 7, 5]
except:
    pass
k = 2
result = quickselect(array, k)
print(f"{k + 1}-я статистика в списке {array} равна {result}")
