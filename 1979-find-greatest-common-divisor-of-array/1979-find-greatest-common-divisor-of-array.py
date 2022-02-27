class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        div = 0
        for i in range(1,min_+1):
            if min_%i==0 and max_%i==0 and i>div:
                div = i
        return div