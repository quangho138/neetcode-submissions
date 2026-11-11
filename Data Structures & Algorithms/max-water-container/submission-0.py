class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        result=min(heights[left],heights[right])*(right-left)
        while left<right:
            if heights[left]<=heights[right]:
                left+=1
                result=max(result,min(heights[left],heights[right])*(right-left))
            else:
                right-=1
                result=max(result,min(heights[left],heights[right])*(right-left))
        return result