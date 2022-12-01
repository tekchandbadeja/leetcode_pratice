def helper(i,j1,j2,grid,r,c,dp):
        
        #### base cas boundary vaala
        if j1<0 or j1>=c or j2<0 or j2>=c:
                
                return -(10**9+7)
        
        ### base case destination vaala 
        
        if i==r-1:
                
                ### do cas banenge 
                #first ke kya pata dono ne same element ko liya ho esliye ek baar he pick karenge 
                
                if j1==j2:
                        return grid[i][j1]
                else:
                        return grid[i][j1]+grid[i][j2]
                
        if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
                
                
        ## we have to explore all 9 paths as i explained below
        maxi=-(10**9+7)
        
        
        ## ye dekh rhe ho jis trh se loop likhe gye hai all ppath ko manage karne ke liye socho maja aa jaeyage a
        for dj1 in range (-1,2):
                
                for dj2 in range (-1,2):
                        value=0
                        
                        if j1==j2:
                                value+=grid[i][j1]
                                                           
                        else:
                                value+=grid[i][j1]+grid[i][j2]
                                
                        value += helper(i+1,j1+dj1,j2+dj2,grid,r,c,dp)
                        
                        maxi=max(maxi,value)

        dp[i][j1][j2]= maxi
        return dp[i][j1][j2]

 #down=grid[i][j1]+grid[i][j2]+helper(i+1,j1,j2,grid,r,c)
                                
# left_dia=grid[i][j1]+grid[i][j2]+helper(i+1,j1-dj1,j2,grid,r,c)
                                
                                
# right_dia=grid[i][j1]+grid[i][j2]+helper(i+1,j1,j2+dj2,grid,r,c)

                                
#down=grid[i][j1]+helper(i+1,j1,j2,grid,r,c)
                                
#left_dia=grid[i][j1]+helper(i+1,j1-dj1,j2,grid,r,c)
                                
#right_dia=grid[i][j1]+helper(i+1,j1,j2+dj2,grid,r,c)
                                
                                
                                
                                
                
        
                
                
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        
        m=len(grid[0])
        
        dp=[[[-1 for i in range (m)] for j in range (m)] for k in range (n)]
        
        return helper(0,0,m-1,grid,n,m,dp)
        
        
'''
question is like fixed starting oint and variable ending point 

according to constraints robot can go in three direction , down ,left digonal and right digonal 

so it is fixed like robot 1 will start from (0,0) point and robot2 from (0,c-1) point 

and second thing is similar that we can not apply here greedy because uniformity not present here 

so my recursion is like 
all path observed by robot 1 + all path observed by robot 2

1.
express everthing in terms (i1,j1) and (i2,j2)
2.
explore all the paths
3.
return maximum 

two base case here 
one is destination base case means i reached at last row 
and second is out of boundary case , always remember , out of boundary base case write first


yha sabse jyda smjhe ka kaam explore all paths me hai 

assume karo robot1 kise (i,j1) pe and robot2 kise (i,j2) if robot go legt digonal than r2 can move in three directions ,possibility there ,same if r1 moves down that time also r2 have three possibilites to move and same for r1 right digonal movement , so total 9 possibiltiy exists 

but dekho in every movement ek baat to common hai ke row increase hoge chayee ld jao chayee rd aur chayee down jao 

so column chage like this +(-1,0,1)



'''
# def helper(i,j1,j2,grid,r,c):
        
#         #### base cas boundary vaala
#         if j1<0 or j1>=c or j2<0 or j2>=c:
                
#                 return -(10**9+7)
        
#         ### base case destination vaala 
        
#         if i==r-1:
                
#                 ### do cas banenge 
#                 #first ke kya pata dono ne same element ko liya ho esliye ek baar he pick karenge 
                
#                 if j1==j2:
#                         return grid[i][j1]
#                 else:
#                         return grid[i][j1]+grid[i][j2]
                
                
#         ## we have to explore all 9 paths as i explained below
#         maxi=-(10**9+7)
        
        
#         ## ye dekh rhe ho jis trh se loop likhe gye hai all ppath ko manage karne ke liye socho maja aa jaeyage a
#         for dj1 in range (-1,2):
                
#                 for dj2 in range (-1,2):
#                         value=0
                        
#                         if j1==j2:
#                                 value+=grid[i][j1]
                                                           
#                         else:
#                                 value+=grid[i][j1]+grid[i][j2]
                                
#                         value += helper(i+1,j1+dj1,j2+dj2,grid,r,c)
                        
#                         maxi=max(maxi,value)

#         return maxi

# time complixity = (O(3**n)*(3**n)),  because there are two robots and every one have three choices to travel 

# space complixity= (O(N)),stack space used 