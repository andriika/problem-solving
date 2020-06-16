# https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside
# the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer. You may assume that the
# input string is always valid; No extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the
# original data does not contain any digits and that digits are only for those repeat numbers, k.  For example, there won't be input
# like 3a or 2[4].


# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

def decode(a):
    chars, k = [], 0
    stack = []
    for c in a:
        if c.isalpha():
            # append to current chars
            chars.append(c)
        elif c.isdigit():
            # append to current k
            k = k * 10 + int(c)
        elif c == '[':
            # store current (chars, k) pair in stack so we can append 
            # ongoing k[..] part to the chars once it's decoded
            stack.append((chars, k))
            # cuurent (chars, k) pair has been stored in the stack,
            # init new pair
            chars, k = [], 0
        elif c == ']':
            # decode current chars:
            # 1. pop parent (chars, k) pair
            pchars, pk = stack.pop()
            # 2. decode current chars
            chars = chars * pk
            # 3. append decoded current chars to the parent chars
            pchars.extend(chars)
            # 4. child chars have been decoded and added to the parent chars,
            # continue parent chars decoding
            chars = pchars
        else:
            raise Exception('invalid character')

    return "".join(chars)

# Test

assert decode('3[a]2[bc]') == 'aaabcbc'
assert decode('3[a2[c]]') == 'accaccacc'
assert decode('2[abc]3[cd]ef') == 'abcabccdcdcdef'
assert decode('abc3[cd]xyz') == 'abccdcdcdxyz'

assert decode('abc') == 'abc'
assert decode('') == ''
