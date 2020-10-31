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
<<<<<<< HEAD
        return answer


# 호윤
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(len(nums)//2):
            answer += nums[i*2]

        return answer
=======
        return answer
>>>>>>> 47dcbbcf73b9b4bb78101b6c4c77dab5b83c03dd
