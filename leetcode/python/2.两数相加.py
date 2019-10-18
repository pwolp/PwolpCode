#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        j = 0
        root = n = ListNode(0)
        while l1 or l2 or j:
            x1 = 0
            x2 = 0
            if l1:
                x1 = l1.val
                l1 = l1.next
            if l2:
                x2 = l2.val
                l2 = l2.next
            j, val = divmod(x1+x2+j, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
    

# @lc code=end

