def helper(index,arr,target,dp):
        
        if target==0:
                return True 
        if index==0:
                return  arr[0]==target
        
        if dp[index][target]!=-1:
                return dp[index][target]
        
        not_take=helper(index-1,arr,target,dp)
        
        take=False 
        
        take=helper(index-1,arr,target-arr[index],dp)
        
        dp[index][target]=(not_take or take)
        return dp[index][target]
                
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ### smjho isko ham subsequence se find karne ka try karenge 
        
        sum=0
        n=len(nums)
        
        for i in range (len(nums)):
                sum+=nums[i]
                
        if sum%2!=0:
                return False 
        else:
                target=sum//2
                dp=[[-1 for i in range (target+1)] for j in range (n)]
                return helper(n-1,nums,target,dp)
                
        
#  '''      
#         bhai mere ko ek array ko do equal sum vaale part me divide karna hai bhai ek baat btaoo yadi 
#         array ka sum dd hai maan lo 21 hai than how can you divide it in two eual part , i say no , not possiblr , so by this I found a small conclusion that if my array sum is even than only i can divide it two eual sum 
# ''' 