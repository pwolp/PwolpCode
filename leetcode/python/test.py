# -*- coding:utf8 -*-
#/usr/bin/env python


class Node(object):
    def __init__(self, item=None):
        self.elem = item
        self.next = None
    
class ChainTable(object):
    def __init__(self, node=None):
        self.head = node
    
    def isEmpty(self):
        '''判断链表是否为空'''
        return self.head == None

    def travel(self):
        '''遍历链表'''
        cur = self.head
        while cur != None:
            print(cur.elem, end='-->')
            cur = cur.next
        print("\n")
    
    def length(self):
        '''链表长度'''
        if self.isEmpty():
            # print("链表长度为：0")
            return 0
        else:
            index = 1
            cur = self.head
            while cur.next != None:
                index += 1
                cur = cur.next
            # print("链表长度为：%d" % (index))
            return index

    def append(self, item):
        '''在链表结尾加元素'''
        node = Node(item)   # 初始化节点类
        if self.isEmpty():   
            self.head = node    # 如果是空链表，把节点添加在表头
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next      # 如果 next 不是空，则指向下一个元素
            cur.next = node     # 在表尾添加节点
    
    def add(self, item):
        '''在链表开始加元素'''
        node = Node(item)
        node.next = self.head
        self.head = node
    
    def insert(self, index, item):
        '''链表中插入元素'''
        length = self.length()
        node = Node(item)
        if index < 0 or index > length - 1:
            return "Out of index !!"
        if index == 0:
            self.add(item)
        else:
            i = 0
            cur = self.head
            while i < index-1:
                cur = cur.next
                i += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
    
    def index(self, item):
        '''查找节点索引'''
        cur = self.head
        i = 0
        while cur != None:
            if cur.elem == item:
                return i
            else:
                cur = cur.next
            i += 1
        
        return "NotFoundError: item not in chain table !!"



if __name__ == '__main__':
    l1 = ChainTable()
    l2 = ChainTable()
    l1.append(3)
    l1.append(2)
    l1.append(1)
    l2.append(7)
    l2.append(8)
    l2.append(1)
    l1.travel()
    l2.travel()

    j = 0
    n = ChainTable(0)
    while l1 or l2 or j:
        x1 = 0
        x2 = 0
        if l1:
            x1 = l1.elem
            l1 = l1.next
        if l2:
            x2 = l2.elem
            l2 = l2.next
        j, val = divmod(x1+x2+j, 10)
        n.elem = val
        n = n.next
    n.travel()