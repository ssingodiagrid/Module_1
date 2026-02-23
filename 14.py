# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxf = 0
        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            maxf = max(maxf, count[s[i]])

            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1

        return res