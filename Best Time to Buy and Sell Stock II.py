class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            dif=prices[i]-prices[i-1]
            if dif>0:
                ans+=dif
        return ans