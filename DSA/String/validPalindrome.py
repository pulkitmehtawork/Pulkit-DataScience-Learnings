#https://leetcode.com/problems/valid-palindrome/

# extra memory solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        return newStr == newStr[::-1]

# O(1) Memory 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) - 1        
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while r > l and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1 , r-1
        return True
        
        
        
        
