class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        cl = ")]}"
        a = []
        if s[0] in cl: return False
        for c in s:
            if c in op:
                a.append(c)
            elif c in cl and len(a) > 0:
                if a[-1] == op[cl.find(c)]:
                    a.pop()
                else:
                    return False 
            elif c in cl and len(a) == 0:
                return False
        return len(a)==0