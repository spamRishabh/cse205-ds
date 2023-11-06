from ast import List
import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=collections.Counter(nums)
        pq=[]
        heapq.heapify(pq)
        ans=[]
        for i,j in hmap.items():
            heapq.heappush(pq,[-1*j,i])
        while k>0:
            ans.append(heapq.heappop(pq)[1])
            k-=1
        return ans