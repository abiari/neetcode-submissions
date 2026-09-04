class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {num:index for index, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target - num in numsDict and i is not numsDict[target - num]:
                return [i, numsDict[target - num]]