class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result, path = [], []
        
        def backtrack(i):
            if len(path) == 4:
                if i == len(s):
                    result.append(".".join(path))
                return
            for length in range(1, 4):
                if i+length>len(s):
                    break
                segment = s[i:i+length]
                if (length > 1 and segment[0] == '0') or int(segment) > 255:
                    break # No need to check longer lengths if this one fails
                path.append(segment)
                backtrack(i+length)
                path.pop()
        backtrack(0)
        return result