import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        
        #### mai harbaar naye element ko sabse phle max heap me jod dunga 
        #### aage baad me uske position decide kar lunga 
        
        ###### we know insert ke liye max_heap nhi hota so we make it by negative number min heap 
        
        heapq.heappush(self.max_heap,-1*num)
        
        #### hamesha yaad rkho                (max_heap ka top element) <median < (min_heap ke top se )
        
        #### lekin yadi iska ulta ho gya tab fir hata denge max ke top ko aur min me ghusa denge 
        
        if self.max_heap and self.min_heap and (-1*self.max_heap[0]>self.min_heap[0]) :
                value=-1*(heapq.heappop(self.max_heap))
                
                heapq.heappush(self.min_heap,value)
                
        #### dhyan do dono ke length equal ho skte hai 
        ### dono ke length ka difference 1 se max nhi ho skta 
        
        if len(self.max_heap)>len(self.min_heap)+1:
                value=-1*heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,value)
                
        if len(self.max_heap)+1<len(self.min_heap):
                value=heapq.heappop(self.min_heap)
                
                heapq.heappush(self.max_heap,-1*value)
                
                

    def findMedian(self) -> float:
        
        if len(self.max_heap)>len(self.min_heap):
                return -1*self.max_heap[0]
        if len(self.min_heap)>len(self.max_heap):
                return self.min_heap[0]
        
        return ((-1*self.max_heap[0])+(self.min_heap[0]))/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()