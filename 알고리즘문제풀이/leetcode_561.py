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


# 재호
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums = sorted(nums)

        for i in range(len(nums)):
            if i % 2 == 0 :
                tmp = nums[i]
            else :
                answer = answer + min(tmp, nums[i])
        return answer