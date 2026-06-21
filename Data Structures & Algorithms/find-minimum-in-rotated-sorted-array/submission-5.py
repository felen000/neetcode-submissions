class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = (r+l)//2
        res = nums[mid]
        while l <= r:
            res = min(res, nums[mid])
            rv, lv, mv = nums[r], nums[l], nums[mid]
            if lv > mv and mv < rv:
                r = mid
            else:
                if nums[r] < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            mid = (r+l)//2

        return res