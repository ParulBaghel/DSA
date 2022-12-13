class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        m=0
        temp=0
        while(m<=j):
            if nums[m]==0:
                temp=nums[m]
                nums[m]=nums[i]
                nums[i]=temp
                i+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                temp=nums[m]
                nums[m]=nums[j]
                nums[j]=temp
                j-=1
    