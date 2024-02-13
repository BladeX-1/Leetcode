from typing import List


def generateString(N: int) -> List[str]:
    full = []
    f(0, N, [], full)
    return full


def f(i, n, partial, full):
    if i == n:
        full.append("".join(partial))
        return True
    else:
        if len(partial) == 0 or partial[-1] != "1":
            partial.append("1")
            f(i + 1, n, partial, full)
            partial.pop(-1)
        partial.append("0")
        f(i + 1, n, partial, full)
        partial.pop(-1)
