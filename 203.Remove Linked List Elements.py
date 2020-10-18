# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        cur = head
        pre = None
        
        while cur:
            if cur.val == val:
                if pre:
                    pre.next = cur.next
                else:
                    head = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head