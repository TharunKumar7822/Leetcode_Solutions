class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 0

        for x in s:

            # x is the beginning of a sequence
            if x - 1 not in s:

                length = 1

                while x + length in s:
                    length += 1

                longest = max(longest, length)

        return longest