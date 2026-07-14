class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []                          # indices, heights increasing bottom→top
        maxArea = 0
        
        for i, h in enumerate(heights + [0]):    # sentinel 0 flushes the stack
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1     # boundary below = left wall
                width = i - left - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        
        return maxArea