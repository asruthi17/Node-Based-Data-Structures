'''Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1=ListNode(0)
        d2=ListNode(0)
        front=d1
        back=d2
        while head!=None:
            if head.val<x:
                front.next=head
                front=front.next
            else:
                back.next=head
                back=back.next
            head=head.next
        back.next=None
        front.next=d2.next
        return d1.next
