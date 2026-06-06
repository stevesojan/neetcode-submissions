class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0

        l = 0
        r = len(heights) - 1

        while l<r:

            length = min(heights[l], heights[r])
            breadth = r-l

            water = length * breadth

            max_water = max(max_water, water)

            # to maximise the values of l and r

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_water

