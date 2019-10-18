# 归并排序（Merge Sort）
# 归并排序是建立在归并操作上的一种有效的排序算法。
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
# 将已有序的子序列合并，得到完全有序的序列；
# 即先使每个子序列有序，再使子序列段间有序。
# 若将两个有序表合并成一个有序表，称为2-路归并。
# 步骤：
#   1. 把长度为n的输入序列分成两个长度为 n/2 的子序列；
#   2. 对这两个子序列分别采用归并排序；
#   3. 将两个排序好的子序列合并成一个最终的排序序列。



def MergeSort(arr):
    def merge(arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1

        for i in range(left, right+1):
            arr[i] = temp[i-left]
        
    
    def mSort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mSort(arr, left, mid)
        mSort(arr, mid+1, right)
        merge(arr, left, mid, right)
    
    
    n = len(arr)
    if n <= 1:
        return arr
    mSort(arr, 0, n-1)
    return arr


import numpy as np
x = np.random.randint(50, size=20)
print(x)
xs = MergeSort(x)
print(xs)

