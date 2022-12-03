# def helper(index,arr,target,dp):
        
#         if target==0:
#                 return True 
#         if index==0:
#                 return  arr[0]==target
        
#         if dp[index][target]!=-1:
#                 return dp[index][target]
        
#         not_take=helper(index-1,arr,target,dp)
        
#         take=False 
#         if arr[index]<=target:
#                 take=helper(index-1,arr,target-arr[index],dp)
        
#         dp[index][target]=(not_take or take)
#         return dp[index][target]
def isSubsetSum (N, arr, sum):
        

        dp=[[0 for i in range (sum+1)] for j in range (N)]  
        ### abhi sab jgh 0 hai 
        
        ## first base case 
        
        for i in range (N):
            
            dp[i][0]=True 
        
        ### second base case 
        if arr[0]<=sum:
                dp[0][arr[0]]=True 
        
        
        for i in range (1,N):
            
            for target in range (1,sum+1):
                
                not_take=dp[i-1][target]
                
                take=False 
                
                if arr[i]<=target:
                    
                    take=dp[i-1][target-arr[i]]
                    
                dp[i][target]=take or not_take 
                
        return dp[N-1][sum]

# def sub_set_sum(arr,target,n):
#         dp=[[0 for i in range (target+1)] for j in range (n+1)]
#         for i in range (n):
#                 dp[i][0]=True 
#         if arr[0]<=target:
#                 dp[0][arr[0]]=True 
#         for i in range (1,n):
#                 for j in range (1,target+1):
#                         not_take=dp[i-1][j]
#                         take=False 
#                         if arr[i]<=target:
#                                 take=dp[i-1][target-arr[i]]
#                         dp[i][j]=not_take or take 
#         return dp[n-1][target]
                        
                
        
        
                
        
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
                #dp=[[-1 for i in range (target+1)] for j in range (n)]
                #return sub_set_sum(nums,target,n)
                return isSubsetSum (n,nums,target)
        
                
        
#  '''      
#         bhai mere ko ek array ko do equal sum vaale part me divide karna hai bhai ek baat btaoo yadi 
#         array ka sum dd hai maan lo 21 hai than how can you divide it in two eual part , i say no , not possiblr , so by this I found a small conclusion that if my array sum is even than only i can divide it two eual sum 
# ''' 

# we will prefer tabulation 