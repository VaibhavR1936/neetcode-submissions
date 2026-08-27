
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=set()
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        values=list(count.values())
        values.sort()
        print(values)
        for i in range(k):
            temp=values[-i-1]
            for key,val in count.items():
                if val==temp:
                    ans.add(key)
                    
        return list(ans)