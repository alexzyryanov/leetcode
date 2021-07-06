class Solution:

    """Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer."""

    def plusOne(self, digits):

        # int all digits [1, 2, 3] --> 123 + 1 = 124
        x = int("".join(str(i) for i in digits)) + 1

        # str int x append in new list x = str(124) --> [1, 2, 3, 4]
        print([int(i) for i in str(x)])
        return [int(i) for i in str(x)]


app = Solution()
app.plusOne([1, 2, 3])
app.plusOne([4, 3, 2, 1])
app.plusOne([0])
app.plusOne([9])
app.plusOne([9, 9])
