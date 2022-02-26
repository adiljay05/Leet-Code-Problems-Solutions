class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {} 
        for item in arr: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        max_ = 0
        for item in freq:
            if freq[item]==item:
                if item>max_:
                    max_ = item
        if max_>0:
            return max_
        return -1