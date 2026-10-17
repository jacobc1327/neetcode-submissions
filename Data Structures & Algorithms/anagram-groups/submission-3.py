class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #hashmap canonical tuple key -> list of append() strings
        hashmap = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                key[index]+=1
            hashmap[tuple(key)].append(word)
        
        result = []
        for array in hashmap.values():
            result.append(array)

        return result