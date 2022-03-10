class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=len(nums)-1
        while i>=0:
            k-=1
            if k == 0:
                return nums[i]
            i-=1
        return -1