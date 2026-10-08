class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        startingcolor = image[sr][sc]
        if startingcolor == color:
            return image
        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=startingcolor:
                return
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)


        dfs(sr, sc)
        return image