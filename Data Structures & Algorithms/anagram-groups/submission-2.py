class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        count={}
        for i in strs:
            ans.append("".join(sorted(i)))
        n=len(strs)
        for i,s in enumerate(ans):
            if s in count:
                count[s].append(strs[i])
            else:
                count[s]=[strs[i]]
        return [x for x in count.values()]
        
        