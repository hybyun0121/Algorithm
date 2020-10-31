#[leetcode 125] : 앞뒤가 똑같은 전화번호~ Palindrome(ABB|BBA, ToDoT 이런 것들)

#Hoyoon
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        s_list = [i for i in s]

        half_s = []
        for i in range(len(s_list)//2):
            half_s.append(s_list.pop())

        if len(s) % 2 == 1:
            s_list.pop()

        print(len(s_list), len(half_s))
        assert len(s_list) == len(half_s)

        if half_s == s_list:
            return True
        else:
            return False

S = Solution()
S.isPalindrome("0P")

s = "A man, a plan, a canal: Panama"

s = s.lower()
s
s=re.sub('[^a-zA-Z0-9]','',s)
s

