class Solution(object):
    def hammingWeight(self, n): -> int:
        ans = 0

        while n>0:
            ans += n%2
            n = n // 2

        return ans
        