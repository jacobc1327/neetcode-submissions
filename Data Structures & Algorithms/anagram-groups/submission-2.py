class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #hashmap canonical tuple key -> list of append() strings

        groups = defaultdict(list)
        result = []

        for word in strs:
            key = [0] * 26
            for char in word:
                index = ord(char)-ord('a')
                key[index] +=1
            groups[tuple(key)].append(word)

        for value in groups.values():
            result.append(value)
        return result