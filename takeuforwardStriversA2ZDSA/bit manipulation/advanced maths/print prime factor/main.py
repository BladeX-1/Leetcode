def countPrimes(n: int) -> int:
    ans = [0]
    while n != 0 and n % 2 == 0:
        if ans[-1] != 2:
            ans.append(2)
        n //= 2
    for i in range(3, n + 1, 2):
        if i > n:
            break
        while n != 0 and n % i == 0:
            if ans[-1] != i:
                ans.append(i)
            n //= i
        i += 2
    ans.pop(0)
    return ans
