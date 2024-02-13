class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        full = []
        f(0, 0, n, [], full)
        return full


def f(openCount, closeCount, n, partial, full):
    if openCount > n or openCount < closeCount:
        return False
    if openCount == closeCount == n:
        full.append("".join(partial))
        return True

    partial.append("(")
    f(openCount + 1, closeCount, n, partial, full)
    partial.pop(-1)
    partial.append(")")
    f(openCount, closeCount + 1, n, partial, full)
    partial.pop(-1)
