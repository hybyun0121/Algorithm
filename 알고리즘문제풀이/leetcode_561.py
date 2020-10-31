# 민채
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 오름차순 정렬
        nums.sort()
        i = 0
        temp = 0
        # 짝수 인덱스만 더하면 된다
        while i <= len(nums):
            try:
                temp += nums[i]
                i += 2
            except:
                break
        return temp