class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        p = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count+=1
                if zero_count > 1:
                    return res
            if n!=0:
                p *= n
            else:
                zero_f = True
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = p
            elif zero_count > 0:
                res[i] = 0
            else:
                res[i] = int(p / nums[i])
        return res