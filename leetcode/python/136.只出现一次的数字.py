#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (63.63%)
# Likes:    872
# Dislikes: 0
# Total Accepted:    108.9K
# Total Submissions: 170.9K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key

    # def singleNumber2(self, nums):
    #     res = 0
    #     for num in nums:
    #         res ^= num
    #     return res
        
    # def singleNumber3(self, nums):
    #     return 2*sum(set(nums))-sum(nums)
        
    # def singleNumber4(self, nums):
    #     return reduce(lambda x, y: x ^ y, nums)
        
    # def singleNumber(self, nums):
    #     return reduce(operator.xor, nums)


# @lc code=end

