# Given a list of words, return the k most frequent words. Answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.
# Try to solve it in O(n log k) time and O(n) extra space.
#
# Example: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output:  ["i", "love"]
#
# Example: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]

import heapq
from collections import Counter



def topk(words, k):
    # transform input words into counter dictionary (e.g. {word: count...}) and present it
    # as a list of key-value tuples (e.g. [(word, count)...])
    wordcounts = Counter(words).items()

    # use python's heapq.nsmallest to find smallest elements among (-count, word) tuples. 
    # I.e find biggest among non negated count tuples (count, word).
    res = heapq.nsmallest(k, wordcounts, lambda e: (-e[1], e[0]))
    # Beware, using heapq.nlargest on (count, word) tuples will give invalid result, as
    # per description, result must be sorted by count in DES order and by word in ASC. That is,
    # negate count trick changes count sorting order to ASC, so thagt we have the same sorting order
    # for both count and words elements.

    # map result into the required type: list[string]
    return list(map(lambda e: e[0], res))


# Test

assert topk(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
assert topk(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
