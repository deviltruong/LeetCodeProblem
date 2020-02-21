"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string
which is formed from the original string by deleting some (can be none) of the characters

Ex: s = "abc", t = "ahbgdc" -> true
    s = "axc", t = "ahbgdc" -> false
"""
from bisect import bisect_left
from collections import defaultdict


class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        index_s = 0
        for index_t in range(0, len(t)):
            if t[index_t] == s[index_s]:
                index_s += 1
            if index_s == len(s):
                return True
        return False

    # If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
    # and you want to check one by one to see if T has its subsequence.
    # In this scenario, how would you change your code?
    # ==> Solution : Use binary search
    #  s = "abc", t = "bahbgdca"
    #  idx = {'a': [0], 'h': [1], 'b': [2], 'g': [3], 'd': [4], 'c': [5]}
    #  i = 0('a'): prev = 0 + 1
    #  i = 1('b'): prev = 2 + 1
    #  i = 2('c'): prev = 5 + 1

    def is_subsequence_binary_search(self, s, t):
        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)
        prev = 0
        for i, c in enumerate(s):
            # locate the insertion point for prev in idx[c] to maintain sorted order
            #
            # idx[c] = [1,2,4,7,10], prev = 5 -> Because idx[c][3] = 7 >= 5 -> insertion = 3
            insertion_point = bisect_left(idx[c], prev)
            # if prev > max(idx[c])
            print(idx[c],prev,insertion_point)
            if insertion_point == len(idx[c]): return False
            prev = idx[c][insertion_point] + 1

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))

    print(s.is_subsequence_binary_search("ahc", "ahbgdc"))
