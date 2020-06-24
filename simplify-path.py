# https://leetcode.com/problems/simplify-path/

# Given an absolute Unix-style path, convert it to the canonical path.

# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.

# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

# Input: "/a/./b/../../c/"
# Output: "/c"

# Input: "/a/../../b/../c//.//"
# Output: "/c"

# Input: "/a//b////c/d//././/.."
# Output: "/a/b/c"


def canonical(path):

    # edge case
    if not path:
        return path

    # transform input: tokenize by / and remove all the empty and '.' elements
    path = filter(lambda el: el and el != '.', path.split('/'))

    # result stack
    result = []

    # for each element in the path
    for el in path:
        if el == '..':
            if result:
                result.pop()
        else:
            # add to the stack
            result.append(el)

    # transform result stack into required presentation
    return '/' + '/'.join(result)

# Test


assert canonical('/home/') == '/home'
assert canonical('/../') == '/'
assert canonical('/home//foo/') == '/home/foo'
assert canonical('/a/./b/../../c/') == '/c'
assert canonical('/a/../../b/../c//.//') == '/c'
assert canonical('/a//b////c/d//././/..') == '/a/b/c'
