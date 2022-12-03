#User function Template for python3
    
    
    
class Solution:
	def minDifference(self, arr, n):
		# code here
		
		### sabse phle total sum dekht hai array ke elemnt ka 
		
		total_sum=0
		for i in range (n):
		    total_sum+=arr[i]
		k=total_sum   
		dp=[[0 for i in range (k+1)] for j in range (n+1)]
		
		for i in range (n):
		    dp[i][0]=True
		    
		if arr[i]<=k:
		    dp[0][arr[0]]=True 
		    
		for i in range (1,n):
		    for target in range (1,k+1):
		        not_take=dp[i-1][target]
		        take=False 
		        if arr[i]<=target:
		            take=dp[i-1][target-arr[i]]
		        dp[i][target]=take or not_take
		
		            
		
		    
	
		mini=(10**9)+7
		
		for s1 in range ((total_sum//2)+1):
		    if dp[n-1][s1]==True:
		        s2=total_sum-s1
		        mini=min(mini,abs(s2-s1))
		return mini 
		        
		    #ans=isSubsetSum (n, arr, s1)
		    
# 		    #ans=sub_set_sum(arr,s1,n)  ### maine eske jariye pata laga liya ke s1 ka sub_set possible hai ke ne 
		    
# 		    if ans==True:    ### yadi possible hai na mere bhai tab bacha hua s2 dusra sub set bana lega 
# 		        s2=total_sum-s1
# 		        mini=min(mini,abs(s2-s1))   ##3 mere ko difference minimum karna hai 
		            
# 		return mini 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends