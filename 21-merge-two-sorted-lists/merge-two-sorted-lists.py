# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         list3=[]
#         while list1.val and list2.val:
#             if list1.val>list2.val:
#                 list3.append(list2.val)
#                 list2.next
#             else:
#                 list3.append(list1.val)
#                 list1.next
#         return list3
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the merged list
        current = dummy  # Pointer to the current node in the merged list
        
        # Iterate through both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists is exhausted, append the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next  # Return the merged list starting from the next node of dummy
