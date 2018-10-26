import random

def mergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list

def bubbleSort(list):
    for num in range(len(list)-1, 0, -1):
        for i in range(num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

def quickSort(list):
    quickSortWork(list, 0, len(list)-1)

def quickSortWork(list, first, last):
    if first < last:
        splitpoint = partition(list, first, last)
        quickSortWork(list, first, splitpoint-1)
        quickSortWork(list, splitpoint+1, last)

def partition(list, first, last):
    pivot = list[first]
    left = first+1
    right = last

    check = False
    while not check:
        while left <= right and list[left] <= pivot:
            left += 1

        while list[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            check = True
        else:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp

    temp = list[first]
    list[first] = list[right]
    list[right] = temp

    return right

def makeArray(n):
    array = []
    for i in range(0, n):
        array.append(random.randint(1,101))
    print(array)
    return array


print("\n<Sort Name>")
print("<Original Array>")
print("<Sorted Array>")

print("\nMerge Sort")
array = makeArray(15)
print(mergeSort(array))

print("\nBubble Sort")
array = makeArray(15)
print(mergeSort(array))

print("\nQuick Sort")
array = makeArray(15)
quickSort(array)
print(array)
