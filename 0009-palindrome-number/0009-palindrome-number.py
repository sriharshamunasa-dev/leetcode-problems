class Solution(object):
    def isPalindrome(self, x):
       str1=str(x)
       rev=str1[::-1]
       if str1==rev:
           return True
       return False
        
        
        