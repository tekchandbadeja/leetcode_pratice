def helper_new(index,nums,dp):
        if index>=len(nums):
                return 0
        
        if dp[index]!=-1:
                return dp[index]
        
        pick=nums[index]+helper_new(index+2,nums,dp)
        
        not_pick=0+helper_new(index+1,nums,dp)
        dp[index]=max(pick,not_pick)
        return dp[index]
# def helper(index,nums,dp):
        
#         ### base case 
#         if index==0:
                
#                  #### ye tabhee possible hai jab me pichle 2 index se aaya hu to ye mere ko lena padega 
#                 return nums[0]
        
#         if index<0:
#                 return 0
#         if dp[index]!=-1:
#                 return dp[index]
#         pick=nums[index]+helper(index-2,nums,dp)
        
#         not_pick=0+helper(index-1,nums,dp)
        
#         dp[index]=max(pick,not_pick)
        
#         return dp[index]
                
                
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        #### mere ko 0 se last indx tak ka maxium sum chiyeee 
        
        ### so i am giving from last indx 
        
        dp=[-1 for i in range (n+1)]
        
        # return helper(n-1,nums,dp)
        
        return helper_new(0,nums,dp)
        