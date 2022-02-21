class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for item in arr:
            if item!=0:
                if (((item*2) in arr)==True) | (item/2==0):
                    return True
            elif arr.count(item)==2:
                return True
        return False