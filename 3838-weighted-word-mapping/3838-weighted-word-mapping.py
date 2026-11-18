class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []

        for s in words:
            cnt = 0
            for i in range(len(s)):
                cnt += weights[ord(s[i]) - ord('a')]
            ans.append(chr(ord('a') + (25 - (cnt % 26))))
        return "".join(ans)

        