# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from pyparsing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node

        return prev 