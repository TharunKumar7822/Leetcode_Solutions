class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        a = list(s)
        i, j = 0, len(a)-1

        while i < j:
            if a[i] in v and a[j] in v:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            else:
                i += a[i] not in v
                j -= a[j] not in v

        return ''.join(a)