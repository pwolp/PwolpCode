# 堆排序（Heap Sort）：
# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
# 堆积是一个近似完全二叉树的结构，
# 并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
# 步骤：
# 1. 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
# 2. 将堆顶元素R[1]与最后一个元素R[n]交换，
#    此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
# 3. 由于交换后新的堆顶R[1]可能违反堆的性质，
#    因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，
#    然后再次将R[1]与无序区最后一个元素交换，
#    得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。
#    不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

def  HeapSort(lst):
    def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
        temp=arr[start]
        son=2*start+1
        while son<=end:
            if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                son+=1
            if temp>=arr[son]:       #判断是否为大顶堆
                break
            arr[start]=arr[son]     #子节点上移
            start=son                     #继续向下比较
            son=2*son+1
        arr[start]=temp             #将原堆顶插入正确位置
#######
    n=len(lst)
    if n<=1:
        return lst
    #建立大顶堆
    root=n//2-1    #最后一个非叶节点（完全二叉树中）
    while(root>=0):
        heapadjust(lst,root,n-1)
        root-=1
    #掐掉堆顶后调整堆
    i=n-1
    while(i>=0):
        (lst[0],lst[i])=(lst[i],lst[0])  #将大顶堆堆顶数放到最后
        heapadjust(lst,0,i-1)    #调整剩余数组成的堆
        i-=1
    return lst


import numpy as np

x = np.random.randint(50, size=20)
print(x)
xs = HeapSort(x)
print(xs)

