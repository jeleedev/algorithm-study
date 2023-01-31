'''
https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        node = head
        prev = None
        while node:
            node.next, next = prev, node.next
            prev, node = node, next
        return prev

'''
---------------------------
('result => ', ListNode{val: 1, next: None})
('node => ', ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}})
---------------------------
('result => ', ListNode{val: 2, next: ListNode{val: 1, next: None}})
('node => ', ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}})
---------------------------
('result => ', ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}})
('node => ', ListNode{val: 4, next: ListNode{val: 5, next: None}})
---------------------------
('result => ', ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}})
('node => ', ListNode{val: 5, next: None})
---------------------------
('result => ', ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}})
('node => ', None)
'''