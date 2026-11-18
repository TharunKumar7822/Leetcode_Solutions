class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new =0
        ans=[]
        for i in range(len(nums)):
            new = new+nums[i]
            ans.append(new) 

        return ans
        