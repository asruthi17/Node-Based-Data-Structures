'''You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left=head
        right=head
        c1=1
        c2=0
        while c1<k:
            left=left.next
            c1+=1
        temp=head
        n=0
        while temp:
            temp=temp.next
            n=n+1
        while c2<n-k:
            right=right.next
            c2=c2+1
        t=left.val
        left.val=right.val
        right.val=t
        return head
