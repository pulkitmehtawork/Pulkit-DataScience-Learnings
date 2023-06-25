##https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums:list[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res


if __name__ == "__main__":
    s = Solution()
    nums1 = [2,2,1]
    nums2 = [4,1,2,1,2]
    nums3 = [1]
    for i in [nums1 , nums2, nums3]:
        res = s.singleNumber(i)
        print(res)
