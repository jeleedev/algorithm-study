class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        self.area = result = 0

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col:
                return False

            if grid[x][y] == 1:
                grid[x][y] = 0
                self.area += 1

                dfs(x, y-1)
                dfs(x, y+1)
                dfs(x-1, y)
                dfs(x+1, y)
                return True

            return False

        for i in range(row):
            for j in range(col):
                if dfs(i, j):
                    result = self.area if result < self.area else result
                    self.area = 0

        return result
