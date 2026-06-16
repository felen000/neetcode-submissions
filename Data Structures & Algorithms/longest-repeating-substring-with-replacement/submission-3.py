class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        count = defaultdict(int)
        
        for r in range(len(s)):
            count[s[r]] += 1
            winLen = r-l+1
            maxc = max(count.values())
            if winLen - maxc <= k:
                res = max(res, winLen)
            else:
                count[s[l]] -= 1
                l += 1
        return res