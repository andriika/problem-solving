# https://leetcode.com/problems/two-city-scheduling/

# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
# and the cost of flying the i-th person to city B is costs[i][1]. Return the minimum cost to fly every person to a city
# such that exactly N people arrive in each city.

# Example:

# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

from functools import lru_cache

# DP Solution. Optimal Substructure:
# Let f(n, a, b) be an otimal solution for the first n-th people and city A with capacity a and city B with capacity b.
# Then f(n, a, b) defined as:
# f(n, a, b) =
#               │ 0                                  if n ≤ 0
#            a: │ acost[n] + f(n - 1, a - 1, b)      if a > 0 and b ≤ 0
#            b: │ bcost[n] + f(n - 1, a, b - 1)      if b > 0 and a ≤ 0
#               │ min(a, b)
#
# Where acost[n] and bcost[n] is the costs of flying the n-th person to city A and city B respectively


def mincostDP0(costs):

    @lru_cache(maxsize=None)
    def f(n, a, b):
        if n < 1:
            return 0

        # n-th person costs:
        # acost, bcost - costs of flying to city A and city B respectively
        acost, bcost = costs[n - 1]

        ra = acost + f(n - 1, a - 1, b) if a > 0 else float('inf')
        rb = bcost + f(n - 1, a, b - 1) if b > 0 else float('inf')

        return min(ra, rb)

    # single city capacity (half of people)
    city = len(costs) // 2
    # return minimum cost to fly every person to either A or B cities with equals capacity
    return f(len(costs), city, city)

# Optimized version of mincostDP0. Apparently we do not need to maintain both cities capacity in function "f" arguments.
# City B capacity can always be derived from n (total people to process) and a (city A capacity). Since a + b = n,
# b = n - a


def mincostDP1(costs):

    @lru_cache(maxsize=None)
    def f(n, a):
        if n < 1:
            return 0

        # n-th person costs:
        # acost, bcost - costs of flying to city A and city B respectively
        acost, bcost = costs[n - 1]

        # a + b = n, so b = n - a
        b = n - a  # city B capacity

        # ra - total cost of first n people flying if n-th person flies to city A
        ra = acost + f(n - 1, a - 1) if a > 0 else float('inf')
        rb = bcost + f(n - 1, a) if b > 0 else float('inf')

        return min(ra, rb)

    return f(len(costs), len(costs) // 2)

# Test


def mincostGreedy(costs):
    # Sort input array by "city A saving" cost (city A cost - city B cost)
    # Persons with expensive city B costs have good city A saving cost (the less, the better)
    # and will be placed in the first part of array
    costs.sort(key=lambda e: e[0] - e[1])

    # send first part to city A (good city A saving cost)
    # send last part to city B (good city B saving cost)
    n = len(costs) // 2
    res = 0
    for i in range(n):
        res += (costs[i][0] + costs[i + n][1])
    return res


# Test

costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
assert mincostDP1(costs) == mincostGreedy(costs) == 110


costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
assert mincostDP1(costs) == mincostGreedy(costs) == 1859
