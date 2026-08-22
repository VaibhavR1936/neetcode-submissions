class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=len(strs)
        ans=""
        n=len(min(strs,key=len))
        for i in range(n):
            letters=[s[i] for s in strs]
            if letters==[letters[0]]*k:
                ans+=letters[0]
            else:
                return ans
        return ans

        