class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        # for i in range(len(s)):
        #     j = len(s) - i - 1
        #     if (s[i] != s[j]): return False
        #     if (i == j or j-i == 1): break
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1

        return True
        # return s == s[::-1]