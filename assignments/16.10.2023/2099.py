class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tuple_heap = [] 
        for i, val in enumerate(nums):
            if len(tuple_heap) == k:
                heappushpop(tuple_heap, (val, i))
            else:
                heappush(tuple_heap, (val, i))
	
        tuple_heap.sort(key=lambda x: x[1])
        ans = []
        for i in tuple_heap:
            ans.append(i[0])
        return ans