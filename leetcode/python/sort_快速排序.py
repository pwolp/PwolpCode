# 快速排序：
# 快速排序的名字起的是简单粗暴，
# 因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！
# 它是处理大数据最快的排序算法之一了。
# 算法步骤:
#  1. 从数列中挑出一个元素，称为 “基准”（pivot）;
#  2. 重新排序数列，所有元素比基准值小的摆放在基准前面，
#     所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
#     在这个分区退出之后，该基准就处于数列的中间位置。
#     这个称为分区（partition）操作；
#  3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

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

