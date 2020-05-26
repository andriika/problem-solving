# https://leetcode.com/problems/coin-change/

# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 (5 + 5 + 1)
#
# Optimal Substructure:
#
# Let f(n) be the fewest number of coins to make up amount of n. Then f(i, k) defines optimal substructure of the problem as follows:
# f(n) =
#       │ 0                                       if n = 0
#       │ -1                                      if n < 0
#       │ min({f(n - c₀), ..., f(n - cᵢ)}) + 1    if n > 0

from functools import lru_cache


def coinChange(coins, amount):
    inf = float('inf')

    @lru_cache(maxsize=None)
    def f(n):

        # base case 1:
        # make up 0 amount?
        if n == 0:
            # we need no coins to make up 0 amount
            return 0

        # base case 2:
        # make up negative amount?
        if n < 0:
            # negative amount cannot be made up by any combination of the coins
            return -1

        r = inf  # running minimum of the subproblem solutions
        for c in coins:
            cr = f(n - c)  # subproblem solution for the current coin "c"

            # validate the subproblem solution:
            # does it exist?
            if cr > -1:
                # update running minimum
                r = min(r, cr)

        # valid subproblem solutions not found?
        if r == inf:
            return -1
        else:
            return r + 1

    return f(amount)

# Tests


assert coinChange([1, 2, 5], 11) == 3
assert coinChange([2, 5], 11) == 4
assert coinChange([2, 5], 3) == -1
assert coinChange([3, 5], 7) == -1
assert coinChange([186, 419, 83, 408], 6249) == 20
