# https://en.wikipedia.org/wiki/Knapsack_problem
# http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Dynamic/knapsackdyn.htm

# 0-1 Knapsack Problem:
#
# A thief robbing a store and can carry a maximal weight of k into their knapsack.
# There are n items and i-th item weigh wᵢ and is worth vᵢ dollars. What items should thief take?
# The items may not be broken into smaller pieces, so thief may decide either to take an item or to leave it.
#
# Optimal Substructure:
#
# Let f(i, k) be the solution for items 0,1,2,..,i and knapsack's weight limit of k. Then f(i, k) defines optimal substructure of the problem as follows:
#
#           │ ƒ(i - 1, k)                                 if wᵢ > k
# ƒ(i, k) = │
#           │ max(vᵢ + ƒ(i - 1, k - wᵢ), ƒ(i - 1, k))     if wᵢ ≤ k
#
# There are 2 fundamental cases:
#
#   1. wᵢ > k - i-th item is too heavy, so we can't put it into the knapsack, i.e. the solution definitely doesn't include i-th item.
#   2. wᵢ ≤ k - i-th item is lighter then k (knapsack weight limit), i.e. the solution might or might not include 0-th item. So we choose max of 2 cases:
#       a. The solution includes i-th item, in which case it is vᵢ + a subproblem solution for i - 1 items and the weight limit - wᵢ,
#       b. The solution doesn't include i-th item, in which case it is just a subproblem solution for i - 1 items and the same weight limit.

from functools import lru_cache


def knapsack01(w, v, k):

    # top-down recursion
    @lru_cache(maxsize=None)
    def f(i, k):
        # base case:
        # no items to consider?
        if i < 0:
            # empty knapsack is the solution, hence 0 is the value
            return 0

        # i-th item is too heavy?
        if w[i] > k:
            # the solution definitely doesn't include i-th item,
            # it is just a subproblem solution for i - 1 items and the same weight limit
            return f(i - 1, k)

        return max(v[i] + f(i - 1, k - w[i]), f(i - 1, k))

    # return the solution for all the given items and weight limit of k
    return f(len(w) - 1, k)

# Tests


assert knapsack01([1, 12, 2, 1, 4], [2, 4, 2, 1, 10], 15) == 15
assert knapsack01([10, 20, 30], [60, 100, 120], 50) == 220
