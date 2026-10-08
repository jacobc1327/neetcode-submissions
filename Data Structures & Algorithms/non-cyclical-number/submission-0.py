class Solution:
    def isHappy(self, n: int) -> bool:
#make hashset recording all numbers in the cycle
#if found in hashset, repeating, return False

        def sumofSquares(number):
            totalsum = 0
            while number>0:
                totalsum += (number%10)**2
                number = number//10
            return totalsum
#exit when it finds 1 where it returns False
        hashset = set()
        while (sumofSquares(n)) != 1:
            if sumofSquares(n) in hashset:
                return False
            
            hashset.add(sumofSquares(n))
            n = sumofSquares(n)

        return True
