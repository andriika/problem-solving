# https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Example:
# Input: 4
# Output: [
#   [
#       ".Q..",  // Solution 1
#       "...Q",
#       "Q...",
#       "..Q."
#   ],
#   [
#       "..Q.",  // Solution 2
#       "Q...",
#       "...Q",
#       ".Q.."
#   ]
# ]


def isvalid(state, i):
    '''
    Validates i-th element in a given state based on previous elements of the state.
    The state is an integer array representing queens placement. For example, let state be [3,0,1,2]. 
    This means we have following 4x4 board:

        . . . Q
        Q . . .
        . Q . .
        . . Q .

    Let's validate a second row (i=1). It is valid, because no queens above second row (i.e. first row queen) 
    can attack. The function returns True.

    Now, let's validate third row placement (i=2). It's invalid. First row queen can't attack, but 
    second row queen attacks. The function returns False.
    '''
    pos = state[i]
    ld, rd = pos - 1, pos + 1
    for j in range(i - 1, -1, -1):
        jpos = state[j]
        if jpos == pos or jpos == ld or jpos == rd:
            return False
        ld -= 1
        rd += 1
    return True


def nqueens(n: int):

    state = [0] * n  # current state, see isvalid function docs

    def f(i, cb):
        '''
        Backtracing recursion. Goes over problem's state space tree.
        '''
        # have placed all n queens?
        if i == n:
            # state constructed, i.e. all n rows of the board are populated
            cb(state)
            return

        # placing i-th queen
        # let j be a possible placement
        for j in range(n):
            # place i-th row queen on j-th column
            state[i] = j
            # is current placement valid?
            if isvalid(state, i):
                # place next row queen
                f(i + 1, cb)

    res = []

    def onstate(state):
        '''
        Helper state callback function. Transforms given state into required presentation and 
        addds it to the result list
        '''
        r = []
        for p in state:
            r.append(('.' * p) + 'Q' + ('.' * (n - p - 1)))
        res.append(r)

    # start state space tree traversal from the first row
    f(0, onstate)
    return res


# Test

assert nqueens(4) == [['.Q..', '...Q', 'Q...', '..Q.'],
                      ['..Q.', 'Q...', '...Q', '.Q..']]
