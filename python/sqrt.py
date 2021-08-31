class Solution:

    """ Given a non-negative integer x, compute and return the square root of x. """

    def mySqrt(self, x):
        if x == 0:
            return x
        r = 1
        while True:
            if (r + 1) * (r + 1) > x:
                return r
            r += 1


app = Solution()
app.mySqrt(4)
app.mySqrt(8)
app.mySqrt(16)
