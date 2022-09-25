
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        d={}
        for i in range (len(nums)):
                if nums[i] in d:
                        d[nums[i]]+=1
                else:
                        d[nums[i]]=1
        
        for j in d:
                if (k==0 and d[j]>1):
                        count+=1
                elif (k>0 ):
                        if (j+k) in d:
                                count+=1
        return count

                        
        
