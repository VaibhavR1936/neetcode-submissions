
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=[0,0,0]
        for i in nums:
            k[i]+=1
        l=0
        for i in range(0,3):
            while k[i]!=0:
                nums[l]=i
                l+=1
                k[i]-=1



        
        