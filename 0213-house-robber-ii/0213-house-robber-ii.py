def solve_helper(nums,index,dp):
        
        if index>=len(nums):
                return 0
        if dp[index]!=-1:
                return dp[index]
        
        pick=nums[index]+solve_helper(nums,index+2,dp)
        
        not_pick=0+solve_helper(nums,index+1,dp)
        
        dp[index]=max(pick,not_pick)
        return dp[index]
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
                return nums[0]
        dp1=[-1 for i in range (n) ]
        
        dp2=[-1 for i in range (n)]
        
        ans1=solve_helper(nums[0:n-1],0,dp1)
        
        ans2=solve_helper(nums[1:],0,dp2)
        
        return max(ans1,ans2)
        
        
        
        
        #### this question is very much similar to part 1 like house robbery , here onl difference come that 
        ## one and last also djacent due to circle and we can not take bot of them at a sme time 
        
        ### so what do you think , is still we need new logic to solve this question , i say no 
        
        ### we will solve it using our first  part of robbery problem and see 
        