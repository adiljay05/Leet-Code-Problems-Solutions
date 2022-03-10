class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.findLarge()
    def findLarge(self):
        self.nums.sort()
        k = self.k
        i=len(self.nums)-1
        while i>=0:
            k-=1
            if k == 0:
                return self.nums[i]
            i-=1
        return -1

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)