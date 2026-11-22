from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        curr_sum = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            curr_sum += 1 if num == 1 else -1
            if curr_sum in first_seen:
                max_len = max(max_len, i - first_seen[curr_sum])
            else:
                first_seen[curr_sum] = i
                
        return max_len