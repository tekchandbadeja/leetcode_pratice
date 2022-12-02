#User function Template for python3


class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        ### iam taking a dp
        dp=[[0 for i in range (sum+1)] for j in range (N+1)]   ### abhi sab jgh 0 hai 
        
        ## first base case 
        
        for i in range (N):
            
            dp[i][0]=True 
        
        ### second base case     
        dp[0][arr[0]]=True 
        
        for i in range (1,N):
            
            for target in range (1,sum+1):
                
                not_take=dp[i-1][target]
                
                take=False 
                
                if arr[i]<=target:
                    
                    take=dp[i-1][target-arr[i]]
                    
                dp[i][target]=take or not_take 
                
        return dp[N-1][sum]
            
        


# time complixity= O(N*target)

# space complixity=(N*target)+recursion space (O(N))
'''
 what you think how can we solve this problem very much obvious that 
 we try to find out all the subset or subsequences 
 but this we really ned to generate all subsequences when we ant only one , so we think in something different manner 
 
 
 so now how we approach rcursion and direct try to get with target
 
1.express in terms of (index , target)
 
2.explore possibilites of that index , a[index] part o the subsequence or a[index] not be a part
 
3. and finally return True or False 
 
 in case of subset or subsequnces arraays contigous  or non contigous does not matter 
 
 
 __________*************___________________( without dp)
 def helper(index,arr,target):
    
    if target==0:
        return True ##### means hamko mil gya target very simple base case 
        
    if index==0:   ### bhai last point p bollean type bana liya ke ab to bhai last value bachee hai ye equal
                  ## ho gyee than ok otherwise we not get output from our function 
        
        return arr[0]==target
        
    not_take=helper(index-1,arr,target)
    
    take=False 
    
    if arr[index]<=target:
        
        take=helper(index-1,arr,target-arr[index])
        
    return take or not_take

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        
        return helper(N-1,arr,sum)
    
time complixity = exponential (2**n)
space complixity=rcursion /stack space 


________________________********************____________________________________(with dp)
def helper(index,arr,target,dp):
    
    if target==0:
        return True ##### means hamko mil gya target very simple base case 
        
    if index==0:   ### bhai last point p bollean type bana liya ke ab to bhai last value bachee hai ye equal
                  ## ho gyee than ok otherwise we not get output from our function 
        
        return arr[0]==target
        
    if dp[index][target]!=-1:
        return dp[index][target]
        
    not_take=helper(index-1,arr,target,dp)
    
    take=False 
    
    if arr[index]<=target:
        
        take=helper(index-1,arr,target-arr[index],dp)
        
    dp[index][target]= take or not_take
    return dp[index][target]

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        ### iam taking a dp
        dp=[[-1 for i in range (sum+1)] for j in range (N+1)]
        return helper(N-1,arr,sum,dp)
'''
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends