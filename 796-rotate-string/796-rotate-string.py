class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
        return False