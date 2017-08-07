import random


def merger(array1,array2):
    index1 = 0
    index2 = 0
    array1Size = len(array1)
    array2Size = len(array2)
    mergeArray = []
    while index1 < array1Size and index2 < array2Size:
        if array1[index1] > array2[index2]:
             mergeArray.append(array2[index2])
             index2+=1
        else:
             mergeArray.append(array1[index1])
             index1+=1

    while index1 < array1Size:
        mergeArray.append(array1[index1])
        index1+=1

    while index2 < array2Size:
        mergeArray.append(array2[index2])
        index2+=1

    return mergeArray


def sort(array):
    if len(array) <= 1:
        return array
    arraySize = len(array)
    midPoint = arraySize // 2
    array1 = array[:midPoint]
    array2 = array[midPoint:]
    a1 = sort(array1)
    a2 = sort(array2)
    return merger(a1,a2)


if __name__ == "__main__":
    testing = 10**3
    while testing:
        array =   [ random.randint(0,1000) for x in range(10)]
        _array = list(array)
        _array.sort()
        array = sort(array)
        if not  array == _array:
            print array
            print _array
            break
        testing -=1
