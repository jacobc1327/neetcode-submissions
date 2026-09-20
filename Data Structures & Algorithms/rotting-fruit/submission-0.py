class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh +=1
        minutes = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while queue and fresh>0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr>=0 and nc>=0 and nr<ROWS and nc<COLS and grid[nr][nc]==1 
                    ):
                        grid[nr][nc] = 2
                        fresh-=1
                        queue.append((nr,nc))
            minutes+=1
        return minutes if fresh==0 else  -1