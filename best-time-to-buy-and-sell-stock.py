# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You have an array for which the i-th element is the price of a given stock on day i. If you were only permitted to complete
# at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation:
#   Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#   Not 7-1 = 6, as selling price needs to be larger than buying price.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Idea:
#   1.  For each day, calculate what would be the max profit if you sell stock at the current day
#       To do that efficiently, you must know min stock prise you've seen so far in previous days
#       I.e. keep running minimum over stock prises
#   2.  Keep running maximum over calculated profits.


def maxprofit(prices):
    # maxprof: running max of profits
    # minprice: running minimum of prices
    maxprof, minprise = -float('inf'), float('inf')

    for price in prices:
        # price: today's stock price
        # prof: profit we make if we sell stock by today's price
        prof = price - minprise
        # update running maximum of profits
        maxprof = max(maxprof, prof)
        # update running minimum of prices
        minprise = min(minprise, price)

    # edge case:
    # with ever growing prices, maxprofit will be negative;
    # just return 0 in this case.
    if maxprof < 0:
        return 0
    return maxprof

# Test


assert maxprofit([7, 1, 5, 3, 6, 4]) == 5
assert maxprofit([7, 6, 4, 3, 1]) == 0
