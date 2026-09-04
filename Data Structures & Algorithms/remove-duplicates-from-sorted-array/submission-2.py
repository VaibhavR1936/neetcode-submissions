class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i not in ans:
                ans.append(i)
        j=0
        for i in ans:
            nums[j]=i
            j+=1
        return len(ans)

            