import random

def comp(a,b,reversed=False):
    if reversed:
        return a > b
    else:
        return a < b

def sort(array,reversed=False):
    index = 0
    arraySize = len(array)
    while index < arraySize -1:
            if comp(array[index+1],array[index],reversed):
                subIndex = index+1
                while subIndex > 0 and comp(array[subIndex],array[subIndex-1],reversed):
                    temp = array[subIndex]
                    array[subIndex] = array[subIndex-1]
                    array[subIndex-1] = temp
                    subIndex -= 1
                    del temp
            index +=1





if __name__ == "__main__":
    testing = 10**3
    while testing:
        array =   [ random.randint(0,1000) for x in range(10)]
        _array = list(array)
        if not _array.sort() == sort(array):
            print array
            print _array
            break
        testing -=1
