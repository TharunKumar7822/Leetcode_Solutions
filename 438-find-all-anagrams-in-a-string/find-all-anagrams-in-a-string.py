class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        window = [0] * 26

        ans = []
        k = len(p)

        for i in range(len(s)):
            
            window[ord(s[i]) - ord('a')] += 1

            if i >= k:
                window[ord(s[i - k]) - ord('a')] -= 1

            if window == p_count:
                ans.append(i - k + 1)

        return ans