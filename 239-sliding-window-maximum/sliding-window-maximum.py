class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        ans = []

        for i in range(k):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])

        for i in range(k,len(nums)):
            if q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans