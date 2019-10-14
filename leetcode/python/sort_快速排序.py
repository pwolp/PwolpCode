# 

import numpy as np
import time
import copy

def QuickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right

    if left < right:
        partitionIndex = partition(arr, left, right)
        QuickSort(arr, left, partitionIndex - 1)
        QuickSort(arr, partitionIndex + 1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index-1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


x = np.random.randint(50, size=30)
print("原序列：", x)
start = time.time()
xs = QuickSort(x)
end = time.time()
print("排序后：", xs)
print("花费时间：%.8f" % (end - start) )

