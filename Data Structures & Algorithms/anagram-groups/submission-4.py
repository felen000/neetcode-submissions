class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = {}
        d = defaultdict(list)
        for i in range(len(strs)):
            s_sorted = ''.join(sorted(strs[i]))
            # print(s_sorted)
            d[s_sorted].append(strs[i])
            # d[s_sorted] = [strs[i]] + d.get(s_sorted, [])
        
        return list(d.values())
        