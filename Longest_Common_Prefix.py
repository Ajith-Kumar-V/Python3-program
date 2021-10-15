class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.strs=strs
        s=""
        length=[]
        for i in strs:
            length.append(len(i))
            mini=min(length)
        for i in range(mini):
            k=[]
            for j in strs:
                k.append(j[i])
            if (k.count(j[i]))==len(k):
                s=s+j[i]
            else:
                break
        return s
