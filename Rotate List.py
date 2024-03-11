'''Given the head of a linked list, rotate the list to the right by k places.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        length=1
        curr=head
        while curr.next:
            length=length+1
            curr=curr.next
        curr.next=head
        k=k%length
        rotate=length-k
        while rotate:
            curr=curr.next
            rotate=rotate-1
        head=curr.next
        curr.next=None
        return head
