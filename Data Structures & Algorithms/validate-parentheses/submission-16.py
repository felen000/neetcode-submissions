class Solution:
    def isValid(self, s: str) -> bool:
        co = { ")" : "(", "]" : "[", "}" : "{"  }
        a = []
        for c in s:
            if c in co:
                if len(a) > 0 and a[-1] == co[c]:
                    a.pop()
                else:
                    return False 
            else:
                a.append(c)
        return len(a)==0