class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend/divisor)
        if ans>2147483647:
            return 2147483647
        elif ans<-2147483648:
            return -2147483648
        return ans