class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        sum_=0
        for f in freq:
            if freq[f]==1:
                sum_+=f
        return sum_