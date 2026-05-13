class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = -1000
        while l < r:
            lv = heights[l]
            rv = heights[r]
            area = rv * (r-l) if lv > rv else lv * (r-l)
            if area > max_area:
                max_area = area

            r -= 1
            if r == l:
                l +=1
                r = len(heights) - 1
            
        return max_area


        