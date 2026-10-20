class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagrams = defaultdict(list)
        for word in strs:
            key = [0]*26
            for i in range(len(word)):
                index = ord(word[i])-ord("a")
                key[index]+=1
            dictAnagrams[tuple(key)].append(word)
        
        return [listofanagram for listofanagram in dictAnagrams.values()]