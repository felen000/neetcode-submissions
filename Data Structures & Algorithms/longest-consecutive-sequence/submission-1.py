class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        nums = sorted(list(set(nums)))
        b = [[] for i in range(len(nums))]
        m = 0
        b[0].append(nums[0])
        print(nums)
        for i in range(1, len(nums)):
            # if nums[i] - nums[i-1] != 1:
            #     b.append([c, nums[i-1]])
            #     if i <= len(nums)-1:
            #         c = nums[i]
            if nums[i] - nums[i-1] == 1:
                b[m].append(nums[i])
            else:
                m+=1
                b[m].append(nums[i])
        max_len = 0
        for l in b:
            print(len(l))
            if len(l) > max_len:
                max_len = len(l)
        print(b)
        # print(d)
        return max_len