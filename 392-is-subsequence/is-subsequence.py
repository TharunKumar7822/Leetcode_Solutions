class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        
        for ch in t:
            if i == n:
                return True
            if s[i] == ch:
                i += 1
                
        return i == n