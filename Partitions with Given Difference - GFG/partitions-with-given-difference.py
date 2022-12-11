#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# def helper(arr,target,index,dp):
    
#     # if target==0:
#     #     return 1
#     m=(10**9)+7
#     if index==0:
#         if target==0 and arr[0]==0:    #### bhai mere constraint ko pad liya karo yha 0 se start hai array 
#             return 2
            
#         if target==0 or target==arr[0]:
#             return 1
#         return 0
        
#     if dp[index][target]!=-1:
#         return (dp[index][target])%m
#         #return arr[index]==target
#         # if arr[index]==target:
#         #     return 1
#         # else:
#         #     return 0
            
#     not_pick=helper(arr,target,index-1,dp)
    
#     pick=0
#     if arr[index]<=target:
#         pick=helper(arr,target-arr[index],index-1,dp)
        
#     dp[index][target]= ((pick%m)+(not_pick%m))%m
#     return dp[index][target]

class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        mod = 1000000007
        totalSum = 0
        for i in range(n):
            totalSum += arr[i]
        if (totalSum < d or (totalSum - d) % 2):
            return 0
        target = (totalSum - d) // 2
        dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if (j >= arr[i - 1]):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - arr[i - 1]]) % mod
        return dp[n][target]
        
#         total_sum=0
        
#         for i in range (n):
#             total_sum+=arr[i]
            
#         if total_sum-d<0 or (total_sum-d)%2!=0:
#             return 0
#         sum=(total_sum-d)//2
            
#         m=(10**9)+7
# 		dp=[[0 for i in range (sum+1)] for j in range (n)]
		
# 		if arr[0]==0 and sum==0:
# 		    dp[0][0]=2
# 		else:
# 		    dp[0][0]=1
		    
# 		if arr[0]!=0 and arr[0]<=sum:
# 		    dp[0][arr[0]]=1
		
		    
		    
		
		    
# 		for index in range (1,n):
# 		    for target in range (0,sum+1):
		        
# 		        not_pick=dp[index-1][target]
# 		        pick=0
# 		        if arr[index]<=target:
# 		            pick=dp[index-1][target-arr[index]]
# 		        dp[index][target]= ((pick%m)+(not_pick%m))%m
		        
#         return (dp[n-1][sum])%m
            
          
        # dp=[[-1 for i in range (target+1)] for j in range (n)]
          
        # return helper(arr,target,n-1,dp)
        
        
'''
bhai sabse phle total sum ko two parts me divide karna hai , means we can say if one part sum is 
s1 and second part sum is s2 than addition of s1 and s2 will be total sum 
s1+s2=total_sum

and second constraint is like s1-s2 must be difference that given 

so s1+s2=total_sum 
s1-s2=d
so s1=total_sum-s2

total_sum-s2-s2=d
total_sum-d=2*s2

s2=(total_sum-d)/2

'''


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends