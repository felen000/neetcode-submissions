class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(c.lower() for c in s if c.isalnum())
        # s = ''.join(c.lower() for c in s if c.isalnum())
        # for i in range(len(s)):
        #     j = len(s) - i - 1
        #     if (s[i] != s[j]): return False
        #     if (i == j or j-i == 1): break
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while r>l and not s[r].isalnum():  
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
            # if s[l].isalnum(): 

        return True
        # return s == s[::-1]