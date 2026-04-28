class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # d = {}
        # for n in nums:
        #     if n in d.keys(): 
        #         return True
        #     d[n] = 1
        # return False
        if len(nums) == len(set(nums)):
            return False
        return True