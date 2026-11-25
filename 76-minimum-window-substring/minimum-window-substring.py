from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_ch = s[left]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start : best_start + best_len]