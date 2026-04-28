class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n,m = [],[]
        for i in range(len(s)):
            n.append(s[i])
            m.append(t[i])
        m.sort()
        n.sort()
        return "".join(n) == "".join(m)