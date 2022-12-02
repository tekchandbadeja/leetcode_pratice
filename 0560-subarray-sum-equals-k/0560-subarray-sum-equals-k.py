# def helper(index,nums,target,count):
        
#         if target==0:
#                 count+=1
#                 return count 
                
#         if index==0:
#                 if nums[0]==target:
#                         count+=1
#                         return count 
                        
#         not_take=helper(index-1,nums,target,count)
        
#         take=False 
        
#         if nums[index]<=target:
#                 take=helper(index-1,nums,target-nums[i],count)
                
#         if take or not_take:
#                 count+=1
#         return count
                
                
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count=0
#         n=len(nums)
        
#         return helper(n-1,nums,k,count)
        
        
# this approach is for subset (non continguous).

# With this approach , for example [1,1,1] and target=2 , we get answer as 3 because there are 3 possible subsets.
class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
                cur_sum, res = 0, 0
                hm = {0: 1}
        
                for num in nums:
                        cur_sum += num
                        if cur_sum - k in hm: 
                                res += hm[cur_sum-k]
                        hm[cur_sum] = hm.get(cur_sum, 0) + 1
         
                return res

# However, this question deals with contiguous subsequence, hence there are only 2 such subsequences possible.
# Hence this won't work here.
# Hope you understood.