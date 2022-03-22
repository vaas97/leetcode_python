# By Vasu Davanagere
# Leetcode: https://leetcode.com/problems/two-sum/
# This code includes the solution to the problem as well as test cases I wrote.
# Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]

# unit tests for two-sum
import unittest
class TestSolution(unittest.TestCase):
  def test(self):
    s = Solution()
    self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
    self.assertEqual(s.twoSum([3, 1, 5], 6), [1, 2])
    self.assertEqual(s.twoSum([2, 2], 4), [0, 1])
    self.assertEqual(s.twoSum([4, 4], 9), None)

# Run unit tests
if __name__ == '__main__':
  unittest.main()
