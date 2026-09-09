class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):
            # Remove indices that are outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Window is ready
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans