from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        usabledict = Counter(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] in usabledict:
                if usabledict[ransomNote[i]]==0:
                    return False
                else:
                    usabledict[ransomNote[i]]-=1
            else:
                return False
        return True