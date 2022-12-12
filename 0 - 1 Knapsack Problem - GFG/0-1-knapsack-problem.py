#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp= [[0 for x in range(W + 1)] for x in range(n + 1)]
        
        
        for i in range (wt[0],W+1):
            if wt[0]<=W:
                
                dp[0][i]=val[0]
                
            else:
                dp[0][i]=0
                
        for index in range (1,n):
            
            for w in range (W+1):
                
                not_take=dp[index-1][w]
                
                take=float('-inf')
                
                if wt[index]<=w:
                    take=val[index]+dp[index-1][w-wt[index]]
                    
                dp[index][w]=max(not_take,take)
                
        return dp[n-1][W]
                
        
 
    
    
    '''see here bag capacity is W means i can tak max imum w weight in my bag 
    there is given two array value array and weight array , the constranit is like that you want maximum value but 
    weight not exceed the given capacity 
    
    for eg 
    w=8
    value=[30,50,60]
    weight=[3,4,5]
    
    so one case = 3+4<=8 so ok but value become 30+50=80
    
    second case 3+5<=8, so ok but value become 30+60=90
    
    third case 4+5>8 so not possible 
    
    N = 3
    W = 4
    values[] = {1,2,3}
    weight[] = {4,5,1}
    
    take this one , first case , 4<=4 so value become 1
    
    take second case , 1<=4 so value become 3    SEE now after took 1 i can not take it again '''
    
    
    ''''question arise , can we use grredy here ,i will say no because no uniformity present 
    
    see N=3
    w=6
    values=[30,40,60]
    weight=[3,2,5]
    
    according to greedy i will ick most optimal at present time so i will take weight 5 that have maximum value 
    means answr will come 60 according to greedy 
    but If i used my mind than first i pick weight 3 and than weight 2 this will make 70  this give me more maxi
    mum answer 
    
    so greedy not work because a lots of un uniformity here'''
    
    
    
    
    
    '''def solve(W,wt,val,index,dp):
    
    if index==0:
        if wt[0]<=W:
            ### aisa hai to pick karo na bhai 
            return val[0]
        
        else:
            return 0   ### nhi le skte na bhya
    if dp[index][W]!=-1:
        return dp[index]
            
    ### bhai mere 2 he case ban skte hai ya to us weight ko lu ya na lu 
    
    not_pick=0+solve(W,wt,val,index-1,dp)
    
    pick=float('-inf')
    
    if wt[index]<=W:
        pick=val[index]+solve(W-wt[index],wt,val,index-1,dp)
        
    dp[index][W] = max(pick,not_pick)
    return dp[index][W]
    
    
    time complixity is 2**n and space complixity is recursion space (without dp )
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp=[[-1 for i in range (W+1) ] for j in range (n+1)]
        
        ans=solve(W,wt,val,n-1,dp)
        
        
        
        if ans==float('-inf'):
            return 0
            
        return ans '''
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends