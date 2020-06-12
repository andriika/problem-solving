# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters. Remove the minimum number of parentheses
# ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"


def validate(a):

    def invalidIndexes(a):
        '''
        Helper. Returns indexes of the invalid parentheses
        '''
        # balance represents how many open '(' vs closed ')' parentheses we've see so far
        # Zero balance means that we've seen equal number '(' and ')'.
        # Negative balance means that we've seen more ')' than '('. 
        # Positive balance means that we've seen more '(' than ')'.
        # If at any point of processing we got negative balance, we immediatly can mark current ')' as invalid.
        
        balance = 0
        for i, c in enumerate(a):
            if c == '(':
                # increase balance on '('
                balance += 1
            elif c == ')':
                # found ')', we are about to decrese balance,
                # are we balanced already?
                if balance == 0:
                    # we are balanced, thus ')' is not allowed (otherwise balance goes negative)
                    # yield an index of the invalid parenthesis
                    yield i
                else:
                    # decrease balance on ')'
                    balance -= 1

        # is balance positive?
        if balance > 0:
            # positive balance means that the string contains extra "(" chars
            # rightmost "(" chars are those extra, lets yield them as invalid
            # until we got balanced state (balance = 0)

            # go over chars backwards
            for i in range(len(a) - 1, -1, -1):
                c = a[i]
                if c == '(':
                    # extra '(' found, yield it and decrease balance
                    yield i
                    balance -= 1

                    # are we balanced now?
                    if balance == 0:
                        return

    # init result as array of input characters
    res = list(a)

    # for each invalid character index
    for i in invalidIndexes(a):
        # replace i-th result character with None marker
        # i.e. mark it as invalid
        res[i] = None

    # transform result into required type and presentation: string w/o None characters
    # remove None characters (they are all invalid)
    res = filter(lambda el: el is not None, res)
    # array to string
    return ''.join(res)

# Test


assert validate("lee(t(c)o)de)") == "lee(t(c)o)de"
assert validate("a)b(c)d") == "ab(c)d"
assert validate("))((") == ""
assert validate("(a(b(c)d)") == "(a(bc)d)"
