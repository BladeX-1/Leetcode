from copy import deepcopy


def subarraysWithSumK(a: [list], k: int) -> [[int]]:
    # Write your code here
    arr = a
    n = len(a)
    return f(a, 0, len(a) - 1, k)


def f(arr, l, r, target):
    if l > r:
        return []
    m = (l + r) // 2
    left = f(arr, l, m - 1, target)
    mid = []
    right = f(arr, m + 1, r, target)

    toFillLeft = m - 1
    partial = [arr[m]]
    currentSum = arr[m]
    while toFillLeft >= l and currentSum < target:
        partial.append(arr[toFillLeft])
        currentSum += arr[toFillLeft]
        toFillLeft -= 1
    toRemoveLeft = toFillLeft + 1
    partial.reverse()
    if currentSum == target:
        mid.append(partial[:])
    toFillRight = m + 1
    while True:
        if toFillRight <= r:
            # fill right
            partial.append(arr[toFillRight])
            currentSum += arr[toFillRight]
            toFillRight += 1
        else:
            break
        # remove enough from left
        while toRemoveLeft < m and currentSum > target:
            partial.pop(0)
            currentSum -= arr[toRemoveLeft]
            toRemoveLeft += 1
        # check
        if currentSum == target:
            mid.append(partial)
        if toRemoveLeft < m:
            break
    return [*left, *mid, *right]


arr = [1, 2, 3, 1, 1, 1]
k = 3
