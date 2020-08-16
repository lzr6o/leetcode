class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        c1, c2 = float('inf'), float('inf')
        p1, p2 = 0, 0
        for price in prices:
            c1 = min(c1, price)
            p1 = max(p1, price - c1)
            c2 = min(c2, price - p1)
            p2 = max(p2, price - c2)
        return p2