#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (50.82%)
# Likes:    251
# Dislikes: 0
# Total Accepted:    42.6K
# Total Submissions: 83.6K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0 or len(b) == 0:
            return a if len(b)==0 else b
        ad = eval('0b' + a) 
        bd = eval('0b' + b)
        return str(bin(ad + bd))[2:]
            
        
# @lc code=end

