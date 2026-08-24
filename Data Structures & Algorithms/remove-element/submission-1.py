class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]==val:
                count+=1
                nums[i]=1000
        nums.sort()
        return n-count
                
        
        

        

        