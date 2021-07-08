class Solution:

    """ Given two binary strings a and b, return their sum as a binary string. """

    def addBinary(self, a: str, b: str) -> str:
        print(bin(int(a, 2)+int(b, 2))[2::])
        return bin(int(a, 2)+int(b, 2))[2::]


app = Solution()
app.addBinary("11", "1")
app.addBinary("1010", "1011")
