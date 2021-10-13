class Solution:
    def romanToInt(self, s: str) -> int:
        self.s=s
        dicts={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sums=0
        p=0
        for i in range(len(s)-1,-1,-1):
            h=dicts.get(s[i])
            if h>=p:
                sums+=h
            else:
                sums-=h
            p=h
        return (abs(sums))
