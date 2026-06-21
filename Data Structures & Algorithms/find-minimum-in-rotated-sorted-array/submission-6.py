class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = (r+l)//2
        res = nums[mid]
        while l <= r:
            res = min(res, nums[mid])
            if nums[l] > nums[mid] and nums[mid] < nums[r]:
                r = mid
            else:
                if nums[r] < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            mid = (r+l)//2

        return res