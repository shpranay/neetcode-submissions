class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for ind,num in enumerate(nums):
            if ind>0 and nums[ind]==nums[ind-1]:
                continue
            l,r=ind+1,len(nums)-1
            while l<r:
                total=num+nums[l]+nums[r]
                if total==0:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return res