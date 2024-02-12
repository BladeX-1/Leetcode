class Solution:
    def climbStairs(self, n: int) -> int:
        return helper(n, dict())


def helper(n, memo):
    if n in memo:
        return memo[n]
    if n in [1, 2]:
        return n
    # the last step was either 1 or 2
    memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
    return memo[n]
