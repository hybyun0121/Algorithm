# 민채

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s

# HY
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s:
            k = s[0]
            s[0] = s[-1]
            s[-1] = k
            for i in range(1, len(s)//2):
                k = s[i]
                s[i] = s[-1*i-1]
                s[-1*i-1] = k

# jh
class Solution:
    class Solution:
        def reverseString(self, s: List[str]) -> None:
            s.reverse()
