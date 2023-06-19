#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		ans=[]
		for i in range (1,n+1):
		    
		    if arr[i-1]==i:
		        ans.append(i)
		return ans 
		  
# 		if n==0:
# 		    return 0
# 		first=1
# 		for i in range (1,n+1):
# 		    if arr[i-1]==i:
# 		        return i
		        
# 		ans=[]
# 		for i in range (1,n+1):
# 		    if arr[i-1]==i:
# 		        ans.append(i)
# 		return ans
		
		         


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends