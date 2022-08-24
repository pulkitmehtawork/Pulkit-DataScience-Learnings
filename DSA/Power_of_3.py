# Leet code problem 
#https://leetcode.com/problems/power-of-three/

#Given an integer n, return true if it is a power of three. Otherwise, return false.

#An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n% 3 == 0:
            n = n//3
        return True if n == 1 else False
