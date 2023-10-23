# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        values = []
        temp = head

        while temp is not None:
            values.append(temp.val)
            temp = temp.next

        values.sort()

        temp = head
        i = 0

        while temp is not None:
            temp.val = values[i]
            i += 1
            temp = temp.next

        return head