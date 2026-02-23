# 647. Palindromic Substrings

class Solution(object):
    def expandAroundIndex(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def countSubstrings(self, s):
        count = 0

        for i in range(len(s)):
            # odd length palindromes
            count += self.expandAroundIndex(s, i, i)

            # even length palindromes
            count += self.expandAroundIndex(s, i, i + 1)

        return count