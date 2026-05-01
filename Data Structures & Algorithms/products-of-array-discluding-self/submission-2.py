class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]
        p = 1
        zero_f = False
        for n in nums:
            if n!=0:
                p *= n
            else:
                zero_f = True
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = p
            elif zero_f:
                res[i] = 0
            else:
                res[i] = int(p / nums[i])
        return res