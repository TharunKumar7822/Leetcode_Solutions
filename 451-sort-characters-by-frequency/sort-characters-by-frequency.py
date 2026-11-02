from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        ans = ""

        for ch, freq in count.most_common():
            ans += ch * freq

        return ans