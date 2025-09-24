# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or head.next is None:
            return head

        next=head.next
        head.next=None
        if next.next is None:
            next.next=head
            head=next
            next=None


        while next:
            tmp_next=next.next
            next.next=head
            head=next
            next=tmp_next

        return head