from ast import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        value = tickets[k]
        total_time = 0

        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] <= value:
                    total_time += tickets[i]
                else:
                    total_time += value
            else:
                if tickets[i] < value:
                    total_time += tickets[i]
                else:
                    total_time += value - 1

        return total_time