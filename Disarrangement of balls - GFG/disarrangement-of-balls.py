#User function Template for python3

# def solve(n,dp):
#     m=(10**9)+7
    
#     if n==1:
#         return 0
        
#     if n==2:
#         return 1
        
#     if dp[n]!=-1:
#         return dp[n]
        
#     dp[n]=((n-1)%m)*((solve(n-1,dp)%m)+(solve(n-2,dp)%m))
    
#     return dp[n]

class Solution:
    def disarrange(self, N):
        # code here
        m=(10**9)+7
        
        dp=[-1 for i in range (N+1)]
        
        dp[1]=0
        
        dp[2]=1
        
        for i in range (3,N+1):
            
            ans1=dp[i-1]%m
            
            ans2=dp[i-2]%m
            
            sum=ans1+ans2
            
            dp[i]=(((i-1)%m)*sum)%m
            
        return dp[N]
            
        
        
        #return solve(N,dp)
        
    #     m=(10**9)+7
        
    #     if N==1:        ### yadi ek he ball hai ya ek he number hai to uske indexing change karne k jgh he nhu hai 
    #         return 0  
        
    #     if N==2:    ##[0,1] ko [1,0] he bana skte hai ek he possibility hai
    #         return 1
            
            
    # [0,1,2] asumme karo ke 3 balls hai 0,1 and 2 indexing per hai ab dekho maine 0 ko liya to uske 
    #  ## kitne tab (n-1) means 1 and 2 bacha hai jisko aur derangments karna hai 
    #  ## means n-1 elemnt ya ball 
    #  #3 ab baat aaye ke maano 0 second position per chla gya and 2 , first means 0 vaale jhj per aa gya  tab keval n-2 element ko 
    #  ## derangment karna hai aur yadi 0 to second position per chla gya but 2 0 ke position pr ne aaya tab n-1 ko rearrange karna padega 
     
    #     ans=((N-1)%m)*((self.disarrange( N-1)%m)+(self.disarrange(N-2)%m))
    
        
        
        
        
        
        
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.disarrange(N))
# } Driver Code Ends