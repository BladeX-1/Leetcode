class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        maxVal = arr[-1]
        n = len(arr)

        memo=dict()
        for i,x in enumerate(arr):
            memo[x] = i

        ans= []
        for i1 in range(n):
            if(i1>0 and arr[i1-1]==arr[i1]):
                continue
            x1 = arr[i1]
            low = x1*4 # low will increase only
            if(target<low):
                break
            high = maxVal*3 +x1
            if(target>high):
                continue
            for i2 in range(i1+1,n):
                if(i2>i1+1 and arr[i2-1]==arr[i2]):
                    continue
                x2 = arr[i2]
                low = x1+x2*3
                if(target<low):
                    break
                high = maxVal*2 +x2+x1
                if(target>high):
                    continue
                for i3 in range(i2+1,n):
                    if(i3>i2+1 and arr[i3-1]==arr[i3]):
                        continue
                    x3 = arr[i3]
                    low = x1+x2+x3*2
                    if(target<low):
                        break
                    high = maxVal*1 +x3+x2+x1
                    if(target>high):
                        continue
                    x4 = target-x1-x2-x3
                    if(x4<x3):
                        break
                    if(x4 in memo and memo[x4]>i3):
                        ans.append([x1,x2,x3,x4])
        return ans



def f(arr,n,target,level,memo,lastI,partial,full):
    if(level == 4-1):
        if(target in memo and lastI<memo[level]):
            full.append([*partial,target])
            return
        else:
            return
    for i in range(lastI+1,n):
        x = arr[i]
        low = x*(4-level)
        high = ...