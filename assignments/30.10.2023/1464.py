from ast import List
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        heap = [-num for num in nums]
        heapq.heapify(heap)

        max1 = -heapq.heappop(heap)
        max2 = -heapq.heappop(heap)

        return (max1 - 1) * (max2 - 1)