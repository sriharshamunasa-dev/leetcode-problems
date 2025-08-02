class Solution(object):
    def isPalindrome(self, s):
     res =""
     for char in s:
        if char.isalpha():
            res=res+char.lower()
     print(res)  
     return res==res[::-1]
        