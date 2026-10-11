class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = {char for word in words for char in word}
        adj = {c:set() for c in chars}
        indegree = {c:0 for c in chars}

        for w1, w2 in zip(words, words[1:]):
            for a, b in zip(w1, w2):
                if a!=b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indegree[b]+=1
                    break
            else:

                if len(w1)>len(w2):
                    return ""
        q = deque(c for c in chars if indegree[c]==0)
        toposort = []

        while q:
            char = q.popleft()
            toposort.append(char)

            for nextchar in adj[char]:
                indegree[nextchar]-=1
                if indegree[nextchar]==0:
                    q.append(nextchar)

        return "".join(toposort) if len(toposort) == len(chars) else ""