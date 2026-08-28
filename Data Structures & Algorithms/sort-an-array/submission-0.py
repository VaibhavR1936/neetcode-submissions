class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

    
        def merge(L,M,R,nums):
            left,right=nums[L:M+1],nums[M+1:R+1]
            i,j,k=L,0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    nums[i]=left[j]
                    j+=1
                else:
                    nums[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                nums[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                nums[i]=right[k]
                k+=1
                i+=1

         
        def mergesort(left,right,nums):
            if left==right:
                return nums
            mid=(left+right)//2
            mergesort(left,mid,nums)
            mergesort(mid+1,right,nums)
            merge(left,mid,right,nums)
            return nums
        return mergesort(0,len(nums)-1,nums)
        
        