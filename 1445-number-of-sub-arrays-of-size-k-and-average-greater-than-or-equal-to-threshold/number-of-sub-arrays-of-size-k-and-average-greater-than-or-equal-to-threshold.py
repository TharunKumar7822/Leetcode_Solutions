from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        curr_sum = sum(arr[:k])
        count = 1 if curr_sum >= target else 0
        
        for i in range(k, len(arr)):
            curr_sum += arr[i] - arr[i - k]
            if curr_sum >= target:
                count += 1
                
        return count