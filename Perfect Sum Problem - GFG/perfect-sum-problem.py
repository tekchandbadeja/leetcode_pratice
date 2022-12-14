#User function Template for python3

def helper(arr,target,index,dp):
    
    # if target==0:
    #     return 1
    m=(10**9)+7
    if index==0:
        if target==0 and arr[0]==0:    #### bhai mere constraint ko pad liya karo yha 0 se start hai array 
            return 2
            
        if target==0 or target==arr[0]:
            return 1
        return 0
        
    if dp[index][target]!=-1:
        return (dp[index][target])%m
        #return arr[index]==target
        # if arr[index]==target:
        #     return 1
        # else:
        #     return 0
            
    not_pick=helper(arr,target,index-1,dp)
    
    pick=0
    if arr[index]<=target:
        pick=helper(arr,target-arr[index],index-1,dp)
        
    dp[index][target]= ((pick%m)+(not_pick%m))%m
    return dp[index][target]

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
# 		target=sum
		m=(10**9)+7
		dp=[[-1 for i in range (sum+1)] for j in range (n)]
		
# 		if arr[0]==0 and sum==0:
# 		    dp[0][0]=2
		    
# 		if arr[0]!=0 and arr[0]<=sum:
# 		    dp[0][arr[0]]=1
# 		else:
# 		    dp[0][0]=1
		    
		    
		
		    
# 		for index in range (1,n):
# 		    for target in range (1,sum+1):
		        
# 		        not_pick=dp[index-1][target]
# 		        pick=0
# 		        if arr[index]<=target:
# 		            pick=dp[index-1][target-arr[index]]
# 		        dp[index][target]= ((pick%m)+(not_pick%m))%m
		        
#         return dp[n-1][sum]
		        
		return helper(arr,sum,n-1,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends