# 时间复杂度 最好是O(n) 最差是O(n^2)

def insertionSort(alist):
    for key, item in enumerate(alist):
        index = key
        while index > 0 and alist[index-1] > item:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = item
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(insertionSort(alist))

def insertionSort2(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue

    return alist

def insertSort3(array):
    for i  in range(1,len(array)):
        cur = array[i]
        index = i

        while index>0 and array[index-1]>cur:
            array[index-1] = array[index]
            index-=1
        array[index] = cur
    return array

print(insertionSort2(alist))
