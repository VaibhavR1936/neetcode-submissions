class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=list(set(nums))
        ans.sort()
        j=0
        for i in ans:
            nums[j]=i
            j+=1
        return len(ans)

            