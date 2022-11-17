#User function Template for python3


import heapq

class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        
        start_point,end_point=float('-inf'),float('inf')
        max_value=float('-inf')
        
        ### initially I make a empty heap
        heap=[]
        
        ##### by this now I am adding first element of every array
        for i in range (k):
            element=KSortedArray[i][0]
            max_value=max(max_value,element)
            
            ### making heap
            heapq.heappush(heap,(element,i,0))
            
        while len(KSortedArray)==len(heap):
            
            ### pop top element of a heap
            
            value,arr_pos,col_pos=heapq.heappop(heap)
            
            if (max_value-value)<(end_point-start_point):
                start_point=value
                end_point=max_value
                
            #### jis array se top element nikala tha uske next elmet ko ab jodenge and dekhengr ke ab kya pata 
            ### range kam ho jaaye 
            
            ### but usse phle check karenge ke kahi ye out oo range to nhi ho gya
            if col_pos+1>=len(KSortedArray[arr_pos]):
                break 
            
            num=KSortedArray[arr_pos][col_pos+1]
            max_value=max(max_value,num)
            
            heapq.heappush(heap,(num,arr_pos,col_pos+1))
            
        return [start_point,end_point]
            
            
            
            
            
        
        # ###3 Brute Force 
        # ans=[]
        # i=0
        # j=0
        # while i<k:
        #     curr_arr=[]
        #     curr_arr.append(KSortedArray[i][j])
        #     while j<k or j<n:
        #         curr_arr.append(KSortedArray[i][j])
                
        #         j=j+1
        #     ans.append(curr_arr)
                
        #     i=i+1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends