# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not l1 and not l2:
            return []

        array1 = []
        array2 = []

        while l1 is not None:
            array1.append(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            array2.append(l2.val)
            l2 = l2.next

        number1 = "".join(str(num) for num in array1[::-1])
        number2 = "".join(str(num) for num in array2[::-1])

        result = str(int(number1) + int(number2))
        array3 = [int(num) for num in result]
        
        l3 = ListNode(array3[-1])
        current = l3

        for i in range(len(array3) - 2, -1, -1):
            current.next = ListNode(array3[i])
            current = current.next
        
        return l3

