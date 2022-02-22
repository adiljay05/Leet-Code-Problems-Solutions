class Solution:
    def titleToNumber(self, columnTitle):
        position = 0
        for c in columnTitle:
            position = position*26 + ord(c) - ord("A") + 1
        return position
        