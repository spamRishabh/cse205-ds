from ast import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_cost = float('inf')
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                total_cost = prices[i] + prices[j]
                if total_cost <= money:
                    min_cost = min(min_cost, total_cost)
        
        if min_cost == float('inf'):
            return money
        else:
            return money - min_cost