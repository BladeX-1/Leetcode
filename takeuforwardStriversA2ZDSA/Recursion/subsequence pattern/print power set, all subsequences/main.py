class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return f(nums, 0, len(nums), [], [])


def f(arr, i, n, partial, full):
    if i == n:
        full.append(partial[:])
        return full
    # include
    partial.append(arr[i])
    f(arr, i + 1, n, partial, full)
    partial.pop(-1)
    # exclude
    f(arr, i + 1, n, partial, full)
    return full
