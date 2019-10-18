# 插入排序:
# 插入排序是一种最简单直观的排序算法，
# 它的工作原理是通过构建有序序列，对于未排序数据，
# 在已排序序列中从后向前扫描，找到相应位置并插入。
# 步骤：
#   1. 从第一个元素开始，该元素可以认为已经被排序；
#   2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
#   3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
#   4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
#   5. 将新元素插入到该位置后；
#   6. 重复步骤2~5


import numpy as np
import time

def InsertSort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i
        while j > 0 and k < arr[j-1]:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = k

    return arr


x = np.random.randint(50, size=20)
print("原序列：", x)
start = time.time()
xs = InsertSort(x)
end = time.time()
print("排序后：", xs)
print("花费时间：%.8f" % (end - start) )

