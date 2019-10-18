# 简单选择排序（Select Sort）：
# 步骤：
#   1. 初始状态：无序区为R[1..n]，有序区为空；
#   2. 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
#      该趟排序从当前无序区中-选出关键字最小的记录 R[k]，
#      将它与无序区的第1个记录R交换，
#      使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
#   3. n-1趟结束，数组有序化了。


def SelectSort(arr):
    for i in range(len(arr)-1):
        k = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] and arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr


import numpy as np
x = np.random.randint(50, size=20)
print(x)
xs = SelectSort(x)
print(xs)

