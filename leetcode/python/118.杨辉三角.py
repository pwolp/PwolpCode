#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (64.16%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    40K
# Total Submissions: 62.3K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        yh = [[1], [1, 1]]
        while len(yh) < numRows:
            te = [1, 1]
            flag = 0
            for i in range(len(yh)-1):
                te.insert(-1, yh[-1][flag] + yh[-1][flag+1])
                flag += 1
            yh.append(te)
        return yh

# @lc code=end

