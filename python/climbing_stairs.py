# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n):
        if n < 2:
            return 1
        a = b = 1     
        for i in range(2, n):
            a, b = b, a + b
        return a + b



app = Solution()
print(app.climbStairs(1) == 1)
print(app.climbStairs(2) == 2)
print(app.climbStairs(3) == 3)
print(app.climbStairs(4) == 5)
print(app.climbStairs(5) == 8)
print(app.climbStairs(6) == 13)
print(app.climbStairs(7) == 21)
