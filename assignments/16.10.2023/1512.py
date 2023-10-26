class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        good_pairs = 0

        for count in count_dict.values():
            good_pairs += count * (count - 1) // 2

        return good_pairs
        