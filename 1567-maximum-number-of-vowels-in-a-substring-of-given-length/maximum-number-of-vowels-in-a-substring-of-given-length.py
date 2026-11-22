class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr = sum(1 for c in s[:k] if c in vowels)
        ans = curr
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1
            if curr > ans:
                ans = curr
                
        return ans