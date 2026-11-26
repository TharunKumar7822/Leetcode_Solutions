class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start, max_len = 0, 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            curr_len = right - left - 1
            if curr_len > max_len:
                max_len = curr_len
                start = left + 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return s[start : start + max_len]