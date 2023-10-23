class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        sorted_counts = sorted(counts.values(), reverse=True)
        
        total = 0 
        result = 0  

        for count in sorted_counts:
            total += count
            result += 1
            if total >= len(arr) // 2:
                break

        return result