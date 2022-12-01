## VARIABE START TO VARIABLE END 

# def helper(row,col,matrix,n,dp):
        
#         if col<0 or col>=n:    ##33 aisa ho skta hai first row pe aane ke baad vo usse uper vaale row me to nhi ja paayega kyuki maine row 0 ka base case likh diya but digonally to move karne ka try maarega 
#                 return float('inf')
        
#         if row==0:   ### # mai first row per punch gya tu uske element ke sath vapas chl do 
                
#                 return matrix[row][col]
#         if dp[row][col]!=-1:
#                 return dp[row][col]
        
#         up=matrix[row][col]+helper(row-1,col,matrix,n,dp)
        
#         left_digonal=matrix[row][col]+helper(row-1,col-1,matrix,n,dp)
        
#         right_digonal=matrix[row][col]+helper(row-1,col+1,matrix,n,dp)
        
#         dp[row][col]= min(up,left_digonal,right_digonal)
        
#         return dp[row][col]
                

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n=len(matrix)
        dp=[[0 for i in range (n)] for j in range (n)]
        
        for j in range (n):
                dp[0][j]=matrix[0][j]    ### base case main first row ko matrix ke element se fill kar diya 
                
        for i in range (1,n):
                
                for j in range (n):
                        
                        up=matrix[i][j]+dp[i-1][j]
                        
                        # left_dia=float('inf')
                        # right_dia=float('inf')
                        
                        ###left digonal
                        
                        left_dia=matrix[i][j]
                        
                        if j-1>=0:
                                left_dia+=dp[i-1][j-1]
                        else:
                               left_dia+=float('inf') 
                        
                        ### right digonal 
                        
                        right_dia=matrix[i][j]
                        if j+1<n:
                                right_dia+=dp[i-1][j+1]
                        else:
                                right_dia+=float('inf')
                        
                        dp[i][j]=min(up,left_dia,right_dia)
                        
        min_ans=float('inf')
        for j in range (n):
                min_ans=min(min_ans, dp[n-1][j])
        return min_ans 
        
        
                
        
#         n=len(matrix)
#         min_ans=float('inf')
#         dp=[[-1 for i in range (n)] for j in range (n)]
        
#         for j in range (0,n):
                
#                 ans=helper(n-1,j,matrix,n,dp)        ##### kyuki mere ko last row ke har element se possible case dekhna padega 
#                 min_ans=min(min_ans,ans)
#         return min_ans 
        
        
'''
we can not apply greedy hre because uniformity not present 
 
we have to check all possible path , and we alwats know when come situation to figure out all possile path we always uses recursion 

we have to figure out minimum sum from any cell of first row to any cell in last row 

1. epress every term in array (i,j) and bas case 
2. explore all the move
3. maximum / minimum among all paths 


def helper(row,col,matrix,n):
        
        if col<0 or col>=n:    ##33 aisa ho skta hai first row pe aane ke baad vo usse uper vaale row me to nhi ja paayega kyuki maine row 0 ka base case likh diya but digonally to move karne ka try maarega 
                return float('inf')
        
        if row==0:   ### # mai first row per punch gya tu uske element ke sath vapas chl do 
                
                return matrix[row][col]
        
        up=matrix[row][col]+helper(row-1,col,matrix,n)
        
        left_digonal=matrix[row][col]+helper(row-1,col-1,matrix,n)
        
        right_digonal=matrix[row][col]+helper(row-1,col+1,matrix,n)
        
        return min(up,left_digonal,right_digonal)
                

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n=len(matrix)
        min_ans=float('inf')
        
        for j in range (0,n):
                
                ans=helper(n-1,j,matrix,n)        ##### kyuki mere ko last row ke har element se possible case dekhna padega 
                min_ans=min(min_ans,ans)
        return min_ans 
        
time complexity : 3**n bcasue at every row it have three choice to go 

space compllixity = recursion space (O(N))


'''
        