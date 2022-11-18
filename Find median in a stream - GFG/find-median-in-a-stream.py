#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''
import heapq




class Solution:
    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        
        if self.max_heap and self.min_heap and (-1*self.max_heap[0]>self.min_heap[0]):
            
            value=-1*heapq.heappop(self.max_heap)
            
            heapq.heappush(self.min_heap,value)
            
        if len(self.max_heap)>len(self.min_heap)+1:
            value=-1*heapq.heappop(self.max_heap)
            
            heapq.heappush(self.min_heap,value)
            
        if len(self.min_heap)>len(self.max_heap)+1:
            value=heapq.heappop(self.min_heap)
            
            heapq.heappush(self.max_heap,-1*value)
            
        
        
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        
        if len(self.max_heap)>len(self.min_heap):
            return -1*self.max_heap[0]
            
        if len(self.min_heap)>len(self.max_heap):
            return self.min_heap[0]
            
        return ((-1*self.max_heap[0])+(self.min_heap[0]))/2
        
        
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        
        heapq.heappush(self.max_heap,-1*x)
        
        self.balanceHeaps()
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends