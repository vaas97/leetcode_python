# By Vasu Davanagere
# Leetcode: https://leetcode.com/problems/add-two-numbers/
# Problem: You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def equals(self, l):
        if self is None and l is None:
            return True
        if self is None or l is None:
            return False
        if self.val != l.val:
            return False
        if self.next is None and l.next is None:
            return True
        return self.next.equals(l.next)

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
      return l2
    if not l2:
      return l1
    carry = 0
    head = ListNode(0)
    curr = head
    while l1 or l2:
      if l1:
        carry += l1.val
        l1 = l1.next
      if l2:
        carry += l2.val
        l2 = l2.next
      curr.next = ListNode(carry % 10)
      curr = curr.next
      carry = carry // 10
    if carry > 0:
      curr.next = ListNode(carry)
    return head.next

# unit tests for add-two-numbers
import unittest
class TestSolution(unittest.TestCase):
  def test(self):
    s = Solution()
    # 342 + 465 = 807
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = ListNode(7, ListNode(0, ListNode(8)))
    added = s.addTwoNumbers(l1, l2)
    self.assertTrue(added.equals(l3))
  
  def test2(self):
    s = Solution()
    # 27 + 199 = 226
    l1 = ListNode(7, ListNode(2))
    l2 = ListNode(9, ListNode(9, ListNode(1)))
    l3 = ListNode(6, ListNode(2, ListNode(2)))
    added = s.addTwoNumbers(l1, l2)
    self.assertTrue(added.equals(l3))
  
  def test3(self):
    s = Solution()
    # 0 + 12 = 12
    l1 = ListNode(0)
    l2 = ListNode(2, ListNode(1))
    l3 = ListNode(2, ListNode(1))
    added = s.addTwoNumbers(l1, l2)
    self.assertTrue(added.equals(l3))

# Run unit tests
if __name__ == '__main__':
  unittest.main()
