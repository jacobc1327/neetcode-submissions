class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == "#"
            ):
                return

            char = board[r][c]

            if char not in node.children:
                return

            nextNode = node.children[char]

            # complete word found
            if nextNode.word:
                result.append(nextNode.word)
                nextNode.word = None

            # mark visited
            board[r][c] = "#"

            dfs(r + 1, c, nextNode)
            dfs(r - 1, c, nextNode)
            dfs(r, c + 1, nextNode)
            dfs(r, c - 1, nextNode)

            # undo
            board[r][c] = char

        # start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result