from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_counts:
                count += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
            
        return count