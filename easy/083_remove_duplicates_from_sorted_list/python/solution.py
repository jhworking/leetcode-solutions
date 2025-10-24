# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
            
        newList = ListNode()
        current = newList

        current.next = ListNode(head.val)
        head = head.next
        current = current.next

        while head:
            temp = head.val
            if current.val == temp:
                head = head.next
            else:
                current.next = ListNode(temp)
                current = current.next
            
        return newList.next