class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=0
        while n > 0:
            n = n//5
            fact+=n

        return fact

        