class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}
        result = []
        for string in strs:

            group = [0]*26

        #for each string which is string
            for j in range(len(string)):
                index = ord(string[j]) - 97
                group[index]+=1
            dicti.setdefault(tuple(group), []).append(string)
        
        for values in dicti.values():
            result.append(values)
        return result

