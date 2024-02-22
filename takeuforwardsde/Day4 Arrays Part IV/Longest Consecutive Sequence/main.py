class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        thisCount = 0
        if(len(nums)==0):
            return 0
        elif(len(nums)==1):
            return 1
        finalCount = 1
        for i in range(len(nums)):
            if(i-1>=0 and nums[i-1]+1==nums[i]):
                thisCount+=1
                finalCount = max(finalCount,thisCount)
            elif(i-1>=0 and nums[i-1]==nums[i]):
                continue
            else:
                thisCount = 1
        return finalCount