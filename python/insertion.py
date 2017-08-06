import random

def comp(a,b,reversed=False):
    if reversed:
        return a < b
    else:
        return a > b

def sort(array,reversed=False):
    index = 0
    arraySize = len(array)
    while index < arraySize:
        subIndex = index-1
        findBigOne = array[index]
        while subIndex >= 0 and comp(array[subIndex],findBigOne,reversed):
                    array[subIndex+1] = array[subIndex]
                    subIndex -= 1
        array[subIndex+1] = findBigOne
        index +=1




if __name__ == "__main__":
    testing = 10**3
    while testing:
        array =   [ random.randint(0,1000) for x in range(10)]
        _array = list(array)
        _array.sort()
        sort(array)
        if not  array == _array:
            print array
            print _array
            break
        testing -=1
