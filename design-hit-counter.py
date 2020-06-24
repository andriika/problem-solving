# https://leetcode.com/problems/design-hit-counter

# Design a hit counter which counts the number of hits received in the past 5 minutes (300 seconds).
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the
# system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
# counter.hit(1); // hit at timestamp 1.
# counter.hit(2); // hit at timestamp 2.
# counter.hit(3); // hit at timestamp 3.
# counter.getHits(4); // get hits at timestamp 4, should return 3.
# counter.hit(300); // hit at timestamp 300.
# counter.getHits(300); // get hits at timestamp 300, should return 4.
# counter.getHits(301); // get hits at timestamp 301, should return 3.


class HitCounter:

    def __init__(self, timerange=300):
        self.timerange = timerange
        # hits and times
        self.hits, self.times = [0] * timerange, [0] * timerange

    def hit(self, timestamp: int) -> None:
        # fit given timestamp into timerange
        i = timestamp % self.timerange

        # did we receive a hit at the given timestamp before?
        if self.times[i] == timestamp:
            self.hits[i] += 1
        else:
            # we either:
            # 1. never hit at i-th index before
            # 2. hit at some time in the past, but that def happened before current timestamp - timerange,
            #    so it's fine to over write that old hit
            self.hits[i] = 1
            self.times[i] = timestamp

    def getHits(self, timestamp: int) -> int:

        timestamp -= self.timerange

        # find all hits whose time > timestamp - timerange
        # and add theirs hits to the resulting totla
        res = 0
        for i in range(len(self.times)):
            if self.times[i] > timestamp:
                res += self.hits[i]
        return res

# For example, let timerange = 10

# > hit: 1, 4, 4, 6

#           0 1 2 3 4 5 6 7 8 9
#           . . . . . . . . . .
#           ^     ^   ^
# hits :    1     2   1
# times:    1     4   6


# > hit 12, 16, 19, 19

#           0 1 2 3 4 5 6 7 8 9
#           . . . . . . . . . .
#           ^ ^   ^   ^     ^
# hits :    1 1   2   1     2
# times:    1 12  4   16    19

# > getHits 18, i.e. find all hits with time > 18 - 10

#           0 1 2 3 4 5 6 7 8 9
#           . . . . . . . . . .
#           ^ ^   ^   ^     ^
# hits :    1 1   2   1     2
# times:    1 12  4   16    19
# res  :      ^       ^     ^    = 1 + 1 + 2 = 4
