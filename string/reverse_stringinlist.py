class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        Input: ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
