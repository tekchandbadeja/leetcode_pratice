#always see this constraint triangle[i].length == triangle[i - 1].length + 1

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n=len(triangle)
        dp=[[-1 for i in range (n)] for j in range (n)]
        
        for j in range (n):                 #### base case ye to fix hoga 
                dp[n-1][j]=triangle[n-1][j]
                
        ### ab mai last se second row se chna start karta hu 
        
        for i in range (n-2,-1,-1):  ### uper vaale row tak aa gya 
                
                for j in range (i,-1,-1):   ### i th row he element possible hai 
                        
                        down=triangle[i][j]+dp[i+1][j]
                        
                        down_digonal=triangle[i][j]+dp[i+1][j+1]
                        
                        
                        dp[i][j]=min (down,down_digonal)
        ### where we get answr when i come on top 
        
        return dp[0][0]
                        
                        
                
                
        
        
        
''' befor this we did unique path , and grid type question , theree a fix type entering and xisiting point but in there question like triangle there is no fix pont 
like in example you can clearly see in first row only on element , in second row 2 , in third 3 and so on 
depend on so now 
kuch naya sochenge bhai , kaise kara jaaye , ye thoda alag concept hai 


first question , can we apply Greedy here - I say NO  , i think reason is same that uniformity not present here greedy only take optimal at that point so may be possiblity that some another path give good answer 


so we have to explore all the path and find minimum sum so only one solution first come in my mind that is recursion so now i will se how to apply recursion here 

and when we solve any question using recursion we have to think always about three points 
1. represent in form of array , and we can say in the way of indexing , here two indx chage (i,j)
2. explore all th paths 
3. and lastly find minimum from all the paths



here i can not start from last element bcause it is not fix but surely i have 0,0 element in my hand 

def helper(row,col,n,triangle):
        
        if row==n-1:   ### base case ek he kyu liya soch skte ho tum , mere bhai reason ye hai ke mai chayee #down jau ya digonal down jau dono case me next row pe o jaaunga ,tabhe mai check kar lunga phle next row ko 
                return triangle[row][col]
        
        down=helper(row+1,col,n,triangle)+triangle[row][col]
        
        down_digonal=helper(row+1,col+1,n,triangle)+triangle[row][col]
        
        return min(down,down_digonal)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n=len(triangle)
        ans=helper(0,0,n,triangle)
        
        return ans 
'''
## time complixity without dp 
# chlo sochte hai first row , 1 element 
# second row ,2 element 
# third row ,3 element .....
# n th row , n element so and at every point 2 choices available go to down or go to digonal down so time complixity near around 2**(1+2+3+....+n)

# and come to space complixity , here recursion space used   


### with dp 
# def helper(row,col,n,triangle,dp):
        
#         if row==n-1:   ### base case ek he kyu liya soch skte ho tum , mere bhai reason ye hai ke mai chayee #down jau ya digonal down jau dono case me next row pe o jaaunga ,tabhe mai check kar lunga phle next row ko 
#                 return triangle[row][col]    
#         if dp[row][col]!=-1:
#                 return dp[row][col]
#         down=helper(row+1,col,n,triangle,dp)+triangle[row][col]
        
#         down_digonal=helper(row+1,col+1,n,triangle,dp)+triangle[row][col]
        
#         dp[row][col]= min(down,down_digonal)
#         return dp[row][col]
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         n=len(triangle)
#         dp=[[-1 for i in range (n)] for j in range (n)]
#         ans=helper(0,0,n,triangle,dp)
        
      #  return ans 