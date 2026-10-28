class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            if guess(m) == 1:
                l = m + 1
            else:
                r = m - 1