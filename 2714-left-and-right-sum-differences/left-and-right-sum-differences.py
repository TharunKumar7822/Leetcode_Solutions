from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for num in nums:
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
            
        return answer