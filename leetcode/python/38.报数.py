#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (52.73%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    51.7K
# Total Submissions: 97.9K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        l = 1
        while l < n:
            ss = ''
            fact = [s[0]]
            nums = [1]
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    nums[-1] += 1
                else:
                    fact.append(s[i])
                    nums.append(1)
            for i in range(len(nums)):
                ss += str(nums[i]) + fact[i]
            s = ss
            l = l + 1
        return s

        
# @lc code=end

