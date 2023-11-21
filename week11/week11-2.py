class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = haystack
        b = needle

        return a.find(b)