import random

def comp(a,b,reversed=False):
    if reversed:
        return a < b
    else:
        return a > b


def sort(array,reversed=False):
    arraySize = len(array)
    i = 0
    while i < arraySize-1:
        j = 0
        while j < arraySize-i-1:
            if comp(array[j],array[j+1],reversed):
                #swap a,b = b,a
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
            j+=1
        i+=1


if __name__ == "__main__":
    testing = 10**5
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
