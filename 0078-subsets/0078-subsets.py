# def helper(arr,index,ds,ans):
        
#         if index==len(arr):
#                 ans.append(ds)
#                 return 
#         ds.append(arr[index])
#         helper(arr,index+1,ds,ans)
        
#         ds.pop()
        
#         helper(arr,index+1,ds,ans)
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
                output=[]
                output.append([])
                return output 
        li=[]
        small_output=self.subsets(nums[1:])
        for i in small_output:
                li.append(i)
                
        for i in small_output:
                li.append([nums[0]]+i)
        return li
                
#         ds=[]
        
        
#         helper(nums,0,ds)
#         return ds
        