#User function Template for python3
# def helper(n,x,y,z,dp):
    
#     if n==0:   ###3 base case last point pr aa gya ke ab isse aage nhi cut kar skta 0 ho gya 
#         return 0
        
#     if dp[n]!=-1:
#         return dp[n]
     
#     ##### maximum chiyee esliye sub ko minium value se initiliaze kar deta hu    
#     op1=float('-inf')   
#     op2=float('-inf')
#     op3=float('-inf')
    
#     if n>=x:        ###### yadi aisa  hai tabhee cut karna possible hai 
#         op1=helper(n-x,x,y,z,dp)
        
#     if n>=y:
#         op2=helper(n-y,x,y,z,dp)
        
#     if n>=z:
#         op3=helper(n-z,x,y,z,dp)
        
#     dp[n]= 1+max(op1,op2,op3)   ###3 1 esliye plus kiya kyuki mere ko 0 bnane vaala output mila tha 
#     return dp[n]
class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        
        dp=[-10000000 for i in range (n+1)]
        
        dp[0]=0
        
        for i in range (1,n+1):
            
            if i-x>=0:
                dp[i]=max(dp[i],dp[i-x]+1)
                
            if i-y>=0:
                dp[i]=max(dp[i],dp[i-y]+1)
                
            if i-z>=0:
                dp[i]=max(dp[i],dp[i-z]+1)
                
        if dp[n]<0:
            return 0
        else:
            return dp[n]
        
        #code here
        
        # dp=[-1 for i in range (n+1)]
        
        # ans=helper(n,x,y,z,dp)
        
        # if ans<0:    #### matlb mere ko ek bhee segment cut nhi mila jisse puree rod cut jaaye 
        #     return 0
            
        # return ans 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends