class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1

        freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse = True))
        for f in freq:
            k-=1
            ans.append(f)
            if k==0:
                break
        return ans