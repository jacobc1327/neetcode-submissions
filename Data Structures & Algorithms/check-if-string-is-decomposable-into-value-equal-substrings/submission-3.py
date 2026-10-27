class Solution:
    def isDecomposable(self, s: str) -> bool:
        lengths = []
        length = 1
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                length +=1
                if i == len(s)-1:
                    lengths.append(length)
            else:
                lengths.append(length)
                length = 1
         # Convert each run length to its remainder modulo 3
        remainders = [length % 3 for length in lengths]

        # Remainder 1 cannot be formed using groups of 3 and one group of 2
        if 1 in remainders:
            return False

        # Exactly one run must contribute a group of length 2
        return remainders.count(2) == 1