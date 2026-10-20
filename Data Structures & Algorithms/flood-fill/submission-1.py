class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalcolor = image[sr][sc]
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==originalcolor and (nr, nc) not in visited:
                    queue.append((nr, nc))
        return image