from ast import List
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        sorted_nums = sorted(nums)
        return sorted_nums[1]