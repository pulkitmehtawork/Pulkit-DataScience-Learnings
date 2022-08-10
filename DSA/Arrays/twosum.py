#https://leetcode.com/problems/two-sum/submissions/

# 1. 0(n^2) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] ==  target:
                    return [i,j]
# 1. 0(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if nums[i] in nums_map:
                return [nums_map[nums[i]],i]
            nums_map[rem] =  i
