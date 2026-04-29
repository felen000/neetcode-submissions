class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            if nums.count(a) != 0:
                for j in range(i+1, len(nums)):
                    if nums[j] == a:
                        return [i, j]
            
        