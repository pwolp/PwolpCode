# 希尔排序：
# 希尔排序是插入排序的高效实现，对简单插入排序减少移动次数优化而来。
# 简单插入排序每次插入都要移动大量数据，前后插入时的许多移动都是重复操作，
# 若一步到位移动效率会高很多。
# 若序列基本有序，简单插入排序不必做很多移动操作，效率很高。
# 希尔排序将序列按固定间隔划分为多个子序列，
# 在子序列中简单插入排序，先做远距离移动使序列基本有序；
# 逐渐缩小间隔重复操作，最后间隔为1时即简单插入排序。
# 步骤：
#    1. 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
#    2. 按增量序列个数k，对序列进行k 趟排序；
#    3. 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，
#       分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，
#       表长度即为整个序列的长度。

def ShellSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    d = n // 2
    while d >= 1:
        shellinsert(arr, d)
        d = d // 2
    return arr

def shellinsert(arr, d):
    n = len(arr)
    for i in range(d, n):
        j = i - d
        temp = arr[i]
        while (j >= 0 and arr[j] > temp):
            arr[j + d] = arr[j]
            j = j - d
        if j != i - d:
            arr[j+d] = temp
    

import numpy as np

x = np.random.randint(50, size=20)
print(x)
xs = ShellSort(x)
print(xs)

