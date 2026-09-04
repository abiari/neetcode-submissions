class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            target = nums[i] * -1
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[start] + nums[end]
                if total == target:
                    output.append(sorted([nums[i], nums[start], nums[end]]))
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                if total > target:
                    end -= 1
                if total < target:
                    start += 1
            i += 1
        return output