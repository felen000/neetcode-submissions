class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            s_sorted = ''.join(sorted(strs[i]))
            d[s_sorted] = [strs[i]] + d.get(s_sorted, [])
        
        return list(d.values())
        