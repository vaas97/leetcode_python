# By Vasu Davanagere
# Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Problem: Given a string, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
          return 0
        if len(s) == 1:
          return 1
        substring_dict = {}
        max_length = 0
        start = 0
        for i in range(len(s)):
          if s[i] in substring_dict:
            start = max(start, substring_dict[s[i]] + 1)
          substring_dict[s[i]] = i
          max_length = max(max_length, i - start + 1)
        return max_length

# unit tests for longest-substring-without-repeating-characters
import unittest
class TestSolution(unittest.TestCase):
  def test(self):
    s = Solution()
    self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3) # abc
    self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3) # "wke"
    self.assertEqual(s.lengthOfLongestSubstring(""), 0) # empty string
    self.assertEqual(s.lengthOfLongestSubstring("bbbbb"), 1) # b
    self.assertEqual(s.lengthOfLongestSubstring("abcdefg"), 7) # "abcdefg"
    self.assertEqual(s.lengthOfLongestSubstring("aab"), 2) # "ab"
    self.assertEqual(s.lengthOfLongestSubstring("dvdf"), 3) # "vdf"
    # repetitions are case sensitive
    self.assertEqual(s.lengthOfLongestSubstring("aA"), 2) # "aA"
    self.assertEqual(s.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 52)

# Run unit tests
if __name__ == '__main__':
  unittest.main()
