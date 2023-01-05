"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
"""


def sortPeople(names, heights):
    return [first for first, second in sorted(list(zip(names, heights)), key=lambda x: x[1], reverse = True)]


print(sortPeople(["Mary","John","Emma"], [180,165,170])) # expected: ["Mary","Emma","John"], Explanation: Mary is the tallest, followed by Emma and John.
print(sortPeople(["Alice","Bob","Bob"], [155,185,150])) # expected: ["Bob","Alice","Bob"], Explanation: The first Bob is the tallest, followed by Alice and the second Bob.