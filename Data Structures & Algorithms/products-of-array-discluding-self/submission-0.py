class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            product = 1
            nums2 = nums.copy()
            nums2.remove(num)
            for n in nums2:
                product = n * product
            output.append(product)
        return output