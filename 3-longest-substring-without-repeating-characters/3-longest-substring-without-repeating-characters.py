class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        non_repeating_string = ""
        for s1 in s:
            if s1 not in non_repeating_string:
                # keep concatenating until no repeated character
                non_repeating_string += s1
                max_ = max(max_, len(non_repeating_string))
            else:
                #if a character is repeating, start from next char again
                non_repeating_string = non_repeating_string.split(s1)[1] + s1
            # print(non_repeating_string)
        return max_