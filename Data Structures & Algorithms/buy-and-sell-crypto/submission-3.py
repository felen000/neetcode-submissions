class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]
        
        # for i in range(len(prices)-1, 0, -1):
        #     r = prices[i] - min(prices[:i])
        #     if r > profit:
        #         profit = r
        if len(prices) < 2: return 0
        l, r = 0, 1
        while l<r:
            rp = prices[r]
            lp = prices[l]
            if rp - lp > profit:
                profit = rp - lp

            if rp < lp:
                l = r
                
            r += 1
            if r >= len(prices): break

        return profit