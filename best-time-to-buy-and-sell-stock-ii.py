# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# You have an array prices for which the ith element is the price of a given stock on day i. Design an algorithm to find
# the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation:
#   Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#   Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Input: [1,2,3,4,5]
# Output: 4
# Explanation:
#   Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#   Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#   engaging multiple transactions at the same time. You must sell before buying again.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Idea: We buy stock at bottoms and sell at peaks.
# E.g. [1,2,3,4,3,1,2,5,2,6] - peaks are marked with '^', bottoms with '-'
#       -     ^   -   ^ - ^


def maxprofit(p):
    # sum of profits
    res = 0

    # min price (bottom)
    minp = p[0]
    for i in range(len(p) - 1):
        # look into the future:
        # will tommorow's price be bigger?
        if p[i + 1] > p[i]:
            # do not sell, wait for tommorow
            continue

        # we'r at peak today, it's time to sell a stock
        prof = p[i] - minp
        res += prof

        # we just sold a stock, so we need to find a new min prise (i.e. buy a new stock)
        # Let it be tomorrow's price. Notice, it's not an issue if tommorow's price is bigger
        # then price on day after tommorow - in that case, on next day, we will sell stock by
        # the same price as we just bought it (i.e. we buy and sell stock at the same day)
        minp = p[i + 1]

    # edge case: perform "last day sell" (notice, it will always be positive)
    res += p[-1] - minp
    return res

# Test


assert maxprofit([7, 1, 5, 3, 6, 4]) == 7
assert maxprofit([1, 2, 3, 4, 5]) == 4
assert maxprofit([7, 6, 4, 3, 1]) == 0
