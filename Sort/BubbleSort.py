# Python 实现冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(alist))

# 改进的冒泡排序, 加入一个校验, 如果某次循环发现没有发生数值交换, 直接跳出循环
def modiBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum >= 1 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchange = True
        passnum -= 1
    return alist

def bubbleSort2(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def modiBuddleSort2(array):
    flag = True
    i = 0
    while i!=len(array) and flag:
        flag = False
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                flag = True
        i+=1
    return array

print(modiBuddleSort2(alist))