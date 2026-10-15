from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = []
        c = Counter(nums)
        for i in c:
            if  c[i] > 1:
                seen.append(i)
        return seen
        