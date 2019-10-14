#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target - nums[i]], i]
            m[nums[i]] = i

        return [-1,-1]
        # map = {}
        # for i in range(len(nums)):
        #     if nums[i] not in map:
        #         map[target - nums[i]] = i
        #     else:
        #         return map[nums[i]], i

        # return -1, -1

        # 暴力搜索
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        



# @lc code=end

