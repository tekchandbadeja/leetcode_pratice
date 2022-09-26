class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_so_far=prices[0]
        
        for i in range (len(prices)):
                min_so_far=min(min_so_far,prices[i])
                profit=prices[i]-min_so_far
                max_profit=max(profit,max_profit)
        return max_profit
        