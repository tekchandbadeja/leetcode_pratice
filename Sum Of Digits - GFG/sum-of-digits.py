#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        # code here
        sum=0
        small_output=0
        if N<10:
            return N
        while N!=0:
            small_output=small_output+(N%10)
            N=N//10
        return small_output
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends