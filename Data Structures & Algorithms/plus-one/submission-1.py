class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digs = len(digits)
        if digits[digs-1]<9:
            digits[digs-1]+=1
            return digits
        else:
            digits[digs-1] = 0
            while digs >= 2:
                if digits[digs-2]<9:
                    digits[digs-2]+=1
                    return digits
                else:
                    digits[digs-2] = 0
                    digs-=1
            digits.insert(0, 1)
            return digits

            
