# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        """错误的思路：前面一半和后面的次数相同则返回，但是没有考虑前面和后面的次数一样但是顺序不一样的情况"""
        """但是也能通过89/93"""
        count = 10 * [0]

        n = 0
        copy_head = head
        while head:
            n += 1
            head = head.next

        head = copy_head
        for i in range(n / 2):
            count[head.val] += 1
            head = head.next
        if n % 2 == 1:
            i = n / 2 + 2
            head = head.next
        else:
            i = n / 2 + 1
            # head=head.next

        while i <= n:
            print(head.val, i)
            count[head.val] -= 1
            head = head.next
            i += 1

        for c in count:
            if c != 0:
                return False
        return True


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        """反转链表之后判断是否相同，相同则返回True"""
        "但是这个做法空间是O（N），因为用了数组。可以试着直接修改原来的链表为两个链表进行判断"
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next

        n=len(nums)
        for i in range(n):
            if nums[i]!=nums[n-i-1]:
                return False
        return True

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        """直接修改原来的链表为两个链表进行判断，沿着中心点断开，其中一个反转，空间O（1）"""
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next

        cur=head
        for i in range(n/2):
            cur=cur.next

        if n%2==1:
            cur=cur.next

        prev=None
        cur=cur

        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next

        while cur:
            if cur.val!=head.val:
                return False
            cur=cur.next
            head=head.next
        return True