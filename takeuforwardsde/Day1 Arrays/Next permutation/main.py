class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rightPeak = None
        for i in reversed(range(1,n)):
            if(nums[i-1]<nums[i]):
                rightPeak = i
                break
        if(rightPeak==None):
            nums.reverse()
            return
        toSwitch1 = rightPeak - 1
        for i in reversed(range(toSwitch1+1,n)):
            if(nums[toSwitch1]<nums[i] and (i==n-1 or nums[i]!=nums[i+1])):
                toSwitch2 = i
                break
        nums[toSwitch1],nums[toSwitch2] = nums[toSwitch2],nums[toSwitch1]
        l = toSwitch1+1
        r = n-1
        while(l<r):
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return