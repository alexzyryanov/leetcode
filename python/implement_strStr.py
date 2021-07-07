class Solution:

    """Return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack."""

    def strStr(self, haystack, needle):
        if needle == "":
            print(0)
            return 0
        elif needle not in haystack:
            print(-1)
            return -1

        # return index
        elif needle in haystack:
            print(haystack.find(needle))
            return haystack.find(needle)


app = Solution()
app.strStr("hello", "ll")
app.strStr("aaaaa", "bba")
app.strStr("", "")
app.strStr("a", "a")
