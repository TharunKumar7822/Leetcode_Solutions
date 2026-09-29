class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new = []
        for i in nums:
            new.append(i**2)
        return sorted(new)