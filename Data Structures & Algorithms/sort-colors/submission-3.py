
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=Counter(nums)
        i=min(count.keys())
        k=0
        while i<3 and k<len(nums):
            if i in count.keys() and count[i]!=0:
                nums[k]=i
                count[i]-=1
                k+=1
            if count[i]==0 or i not in count.keys():i+=1


        
        