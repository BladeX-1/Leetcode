from copy import deepcopy


def subarraysWithSumK(a: [list], k: int) -> [[int]]:
    # Write your code here
    arr = a
    n = len(a)
    full = []
    for i in range(n):
        currentSum = 0
        partial = []
        for j in range(i, n):
            currentSum += a[j]
            partial.append(arr[j])
            if currentSum == k:
                full.append(partial)
                break
            elif currentSum > k:
                break
    return full
