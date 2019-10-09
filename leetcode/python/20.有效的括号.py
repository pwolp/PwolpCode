#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.67%)
# Likes:    1109
# Dislikes: 0
# Total Accepted:    133.5K
# Total Submissions: 336.3K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        left = ['(', '[', '{']
        right = [')', ']', '}']
        state = []
        for i in range(len(s)):
            if i == 0 and s[i] in right:
                return False
            if s[i] in left:
                state.append(left.index(s[i]))
            elif s[i] in right:
                if right.index(s[i]) == state[-1]:
                    state.pop()
                else:
                    return False
            else:
                return False
        if len(state) == 0:
            return True
        else:
            return False

        

# @lc code=end

