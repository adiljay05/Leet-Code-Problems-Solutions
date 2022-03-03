class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ""
        if len(num)==0:
            return list(str(k))
        for n in num:
            s+=str(n)
        sum_ = int(s)+k
        return list(str(sum_))