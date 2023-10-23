class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)

        sorted_counts = sorted(num_counts.items(), key=lambda x: x[1])

        result = [x[0] for x in sorted_counts[-k:]]

        return result