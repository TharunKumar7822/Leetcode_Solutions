from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_counts = [0] * k
        rem_counts[0] = 1
        curr_rem = 0
        count = 0
        
        for num in nums:
            curr_rem = (curr_rem + num) % k
            count += rem_counts[curr_rem]
            rem_counts[curr_rem] += 1
            
        return count