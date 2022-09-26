class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left_sum=sum(cardPoints[0:k])
        right_sum=0
        max_sum=left_sum
        for i in range (k):
                left_sum-=cardPoints[k-i-1]
                right_sum+=cardPoints[-i-1]
                max_sum=max(max_sum,left_sum+right_sum)
        return max_sum
                
#         front_sum=0
#         last_sum=0
#         max_sum=0
#         i=0
#         j=len(cardPoints)-1
        
#         step=1
#         while step<=k:
#                 front_sum=front_sum+cardPoints[i]
#                 last_sum=last_sum+cardPoints[j]
#                 if front_sum>last_sum:
#                         i+=1
#                 else:
#                         j-=1
#                 max_sum=max(front_sum,last_sum)
#                 front_sum=max_sum
#                 last_sum=max_sum
#                 step+=1
#         return max_sum
                
        