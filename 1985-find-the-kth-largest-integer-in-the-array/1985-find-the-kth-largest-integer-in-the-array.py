class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = []
        for n in nums:
            num.append(int(n))
        num.sort()
        i=len(num)-1
        while i>=0:
            k-=1
            if k == 0:
                return str(num[i])
            i-=1
        return ""