class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        nums.sort()
        for i in range(0,len(nums)):
            if a[i]==target:
                lst.append(i)
        return lst