class Solution:
  def maxArea(self, height: list[int]) -> int:
    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      res = max(res, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return res