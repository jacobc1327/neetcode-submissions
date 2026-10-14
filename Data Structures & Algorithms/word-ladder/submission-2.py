class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #make adjacency list of wordList words

        words = set(wordList)

        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            currentword, count = q.popleft()
            if currentword == endWord:
                return count
            for i in range(len(currentword)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    nxt = currentword[:i] + char + currentword[i+1:]
                    if nxt in words and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, count+1))
        return 0