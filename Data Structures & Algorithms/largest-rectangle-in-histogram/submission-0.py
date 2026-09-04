class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestRectangle = 0
        n = len(heights)

        for i in range(n):
            height = heights[i]
            rightBiggerOrEqual = i + 1
            while rightBiggerOrEqual < n and heights[rightBiggerOrEqual] >= heights[i]:
                rightBiggerOrEqual += 1

            leftBiggerOrEqual = i
            while leftBiggerOrEqual >= 0 and heights[leftBiggerOrEqual] >= heights[i]:
                leftBiggerOrEqual -= 1
            
            rightBiggerOrEqual -= 1
            leftBiggerOrEqual += 1

            largestRectangle = max(largestRectangle, height * (rightBiggerOrEqual - leftBiggerOrEqual + 1))
        return largestRectangle
