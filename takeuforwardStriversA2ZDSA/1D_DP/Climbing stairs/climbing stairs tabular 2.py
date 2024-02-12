class Solution:
    def climbStairs(self, n: int) -> int:
        return helper(n)


def helper(n):
    if n in [1, 2]:
        return n
    a = 1
    b = 2
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c
