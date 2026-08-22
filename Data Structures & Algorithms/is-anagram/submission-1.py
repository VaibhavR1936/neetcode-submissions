class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount=collections.Counter(s)
        tcount=collections.Counter(t)
        if len(s)!=len(t):return False
        try:
            for key,value in scount.items():
                if tcount[key]!=value:
                    return False
        except:
            return False
        return True
