class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        final_max_water=0
        
        while left<right:
                curr_max_water=(min(height[left],height[right]))*(right-left)
                final_max_water=max(curr_max_water,final_max_water)
                
                if height[left]<height[right]:
                        left+=1
                else:
                        right-=1
        return final_max_water
        
        