class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        mul=nums[0]
        without_zero=nums[0]
        count=0
        if mul==0:count+=1
        for i in range(1,len(nums)):
            mul=mul*nums[i]
            if nums[i]!=0:
              if without_zero!=0:
                without_zero=without_zero*nums[i]
              else:
                without_zero=nums[i]
            else: count+=1
        for i in nums:
            if count>1:
                ans.append(0)
            elif i!=0:
                ans.append(mul//i)
            else:
                ans.append(without_zero)
        return ans