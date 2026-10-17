class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
#iterate through character in pattern
#create current word by iterating through chars in s until a space or end of string s 
#if character not in pattern dict, say a -> dog
#if character is in pattern dict, two conditions
# if currentword == patterndict[char] then continue
# else: return false
        patterndict = {}
        listofwords = s.split(" ")
        if len(pattern)!=len(listofwords):
            return False
        for i in range(len(pattern)):
            currentword = listofwords[i]
            if pattern[i] not in patterndict:
                if currentword in patterndict.values():
                    return False
                patterndict[pattern[i]] = currentword
            else:
                if currentword == patterndict[pattern[i]]:
                    continue
                else:
                    return False
        return True