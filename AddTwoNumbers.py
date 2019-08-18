"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a
single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      l3 = ListNode()
      carry_over = 0
      while l1.next is None and l2.next is None:

         l3.val = l1.val + l2.val + carry_over
         carry_over = 0
         if l3.val >= 10:
            l3.val -= 10
            carry_over = 1
         l1 = l1.next
         l2 = l2.next

      return l3