# 冒泡排序：
    # 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
    # 它重复地走访过要排序的数列，一次比较两个元素，
    # 如果他们的顺序错误就把他们交换过来。
    # 走访数列的工作是重复地进行直到没有再需要交换，
    # 也就是说该数列已经排序完成。
    # 这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

import numpy as np
import copy

def BubbleSort(nums):
    numlist = copy.copy(nums)
    for i in range(1, len(numlist)):
        for j in range(len(numlist)-i):
            if numlist[j] > numlist[j+1]:
                numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
    return numlist


x = np.random.randint(20, size=10)
print(x)
xs = BubbleSort(x)
print(xs)
print(x)

