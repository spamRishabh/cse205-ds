from ast import List
from typing import Deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten_queue = Deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j))

        if fresh_oranges == 0:
            return 0 

        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while rotten_queue:
            for _ in range(len(rotten_queue)):
                x, y = rotten_queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        rotten_queue.append((nx, ny))
            
            minutes += 1

        return minutes - 1 if fresh_oranges == 0 else -1